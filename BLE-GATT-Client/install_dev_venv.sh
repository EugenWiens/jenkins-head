#!/bin/bash
set -e
set -u
set -x


if [[ -d venv ]]
then
    echo 'venv exists. Did not reinstall'
else
    python -m venv venv
    source venv/bin/activate
    pip install setuptools wheel twine
fi
exit
