import os
from subprocess import Popen, PIPE

checks_cfg = {
    'pre-commit': {
        # Modify run key to specify which checks should be run.
        'run': ['flake8', 'pydocstyle'],
        # Modify ignore key to specify which rules should be ignored.
        'flake8': {'ignore': ''},
        'pydocstyle': {'ignore': 'D100,D104,D203,D213,D406,D407'},
    }
}


def get_repo_path():
    """Return root path for repository."""
    return os.getcwd()


def run(command):
    """Run specified command."""
    p = Popen(command.split(), stdout=PIPE, stderr=PIPE)
    p.wait()
    stdout = p.stdout.read().decode('utf-8')
    return p.returncode, stdout, p.stderr.read().decode('utf-8')
