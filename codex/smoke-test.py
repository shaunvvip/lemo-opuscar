#!/usr/bin/env python3
"""Render a two-second moving fixture and mux audio using unchanged upstream tools.
Requires npm dependencies + Playwright browser and FFmpeg, but no TTS/model downloads.
"""
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent


def run(*args):
    return subprocess.run(args, cwd=ROOT, check=True, text=True, capture_output=True).stdout


def main():
    for tool in ('node', 'ffmpeg', 'ffprobe'):
        if not shutil.which(tool):
            raise SystemExit(f'Missing {tool}; see codex/README.md')
    with tempfile.TemporaryDirectory(prefix='lemo smoke ') as folder:
        project = Path(folder)
        (project / 'index.html').write_text('''<!doctype html><meta charset="utf-8">
<canvas id="c"></canvas><script>
const c=document.getElementById('c'); c.width=innerWidth; c.height=innerHeight;
const g=c.getContext('2d'); window.DUR=2;
window.render=t=>{g.fillStyle='#102030';g.fillRect(0,0,c.width,c.height);
g.fillStyle='#ffba08';g.fillRect(20+t*80,50,40,40);};
window.render(0);window.READY=true;
</script>''', encoding='utf-8')
        video, audio, film = [project / n for n in ('video.mp4', 'mix.wav', 'film.mp4')]
        run('node', 'core/render/video.mjs', str(project), '--size', '320x180',
            '--fps', '24', '--workers', '2', '--out', str(video))
        run('ffmpeg', '-v', 'error', '-f', 'lavfi', '-i',
            'sine=frequency=440:sample_rate=48000:duration=2', str(audio))
        run('sh', 'core/render/mux.sh', str(video), str(audio), str(film), '24', '0')
        meta = json.loads(run('ffprobe', '-v', 'error', '-show_streams',
                              '-show_format', '-of', 'json', str(film)))
        v = next(s for s in meta['streams'] if s['codec_type'] == 'video')
        a = next(s for s in meta['streams'] if s['codec_type'] == 'audio')
        assert (v['width'], v['height'], v['codec_name']) == (320, 180, 'h264'), v
        assert v['avg_frame_rate'] == '24/1', v
        assert a['codec_name'] == 'aac', a
        assert abs(float(meta['format']['duration']) - 2) < 0.15, meta
        frames = []
        for t in ('0.1', '1.5'):
            frames.append(subprocess.run(['ffmpeg', '-v', 'error', '-ss', t, '-i',
                str(film), '-frames:v', '1', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                check=True, capture_output=True).stdout)
        assert len(frames[0]) == 320 * 180 * 3
        assert frames[0] != frames[1], 'The rendered fixture did not move'
        print('PASS: 2 s, 320x180, 24 fps, H.264 + AAC, changing frames; temporary files removed.')
        print('This is an integration smoke test, not artistic or audiovisual playback validation.')


if __name__ == '__main__':
    main()
