#!/usr/bin/env zsh
set -x

# Sort imports one per line, so autoflake can remove unused imports
isort --force-single-line-imports "${@}"

autoflake \
  --remove-all-unused-imports \
  --remove-unused-variables \
  --in-place \
  --exclude=__init__.py \
  --recursive \
  "${@}"

black "${@}"
isort "${@}"