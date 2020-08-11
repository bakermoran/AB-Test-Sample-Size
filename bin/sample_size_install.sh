#!/bin/bash
set -Eeuo pipefail
set -x

rm -rf env

python3 -m venv env

set +u
source env/bin/activate
set -u
