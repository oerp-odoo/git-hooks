#!/usr/bin/env python3
import os
from subprocess import Popen, PIPE

# Prefix to run python3 module.
python3_prefix = 'python3 -m %s'

checks_cfg = {
    'pre-commit': {
        # Modify run key to specify which checks should be run.
        'run': ['flake8', 'pydocstyle'],
        # Modify ignore key to specify which rules should be ignored.
        'flake8': {'ignore': '', 'cmd_prefix': python3_prefix},
        'pydocstyle': {
            'ignore': 'D100,D104,D203,D213,D406,D407',
            'cmd_prefix': python3_prefix},
    },
    'prepare-commit-message': {
        # Branches that will be ignored and won't trigger
        # prepare-commit-message to update message.
        'exclude_branches': [
            'master', '10.0', '11.0', '12.0', '13.0', '14.0', '15.0'
        ]
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
