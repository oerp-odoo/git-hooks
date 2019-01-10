Git hooks implemented using python
==================================


List of git hooks:

- *pre-commit*: this hook runs :code:`flake8` and :code:`pydocstyle` lints on modified files (that are staged). It is possible to change ignore rules list, so it would ignore different rules than currently set. And it is also possible to specify which checks to run (e.g run only :code:`flake8`).
- *prepare-commit-message*: prepends empty commit message with :code:`[BRANCH] BRANCH_NAME` pattern. In :code:`hooks_cfg.py`, it is possible to define branch names that should ignore this feature.

Usage
=====

Copy contents to your :code:`.git/hooks directory`. :code:`hooks_cfg.py checks_cfg` can be modified in order to run different checks or with different rules.

Also make sure hooks are executable.

