#!/usr/bin/env python3
"""Check installation in isolation: spaces, repeat installs, conflicts and root lookup."""
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
INSTALL = ROOT / 'codex/install-skill.sh'


class InstallTests(unittest.TestCase):
    def test_link_and_repeat_install(self):
        with tempfile.TemporaryDirectory(prefix='codex skill ') as folder:
            dest = Path(folder) / 'my skills'
            for _ in range(2):
                subprocess.run(['sh', str(INSTALL), str(dest)], check=True, capture_output=True)
            skill = dest / 'lemo-opuscar'
            self.assertEqual(skill.resolve(), ROOT / '.agents/skills/lemo-opuscar')
            result = subprocess.run(['sh', str(skill / 'scripts/setup.sh')], cwd=folder,
                                    check=True, capture_output=True, text=True)
            self.assertEqual(result.stdout.strip(), f'LIB={ROOT}')

    def test_existing_skill_is_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            dest = Path(folder)
            existing = dest / 'lemo-opuscar'
            existing.mkdir()
            marker = existing / 'SKILL.md'
            marker.write_text('user skill')
            result = subprocess.run(['sh', str(INSTALL), str(dest)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(marker.read_text(), 'user skill')

    def test_broken_link_is_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / 'lemo-opuscar'
            target.symlink_to(Path(folder) / 'missing')
            result = subprocess.run(['sh', str(INSTALL), folder], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue(target.is_symlink())


if __name__ == '__main__':
    unittest.main()
