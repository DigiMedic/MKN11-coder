#!/bin/sh
set -e

if [ -z "$PORT" ]; then
    PORT=8000
fi

curl --fail http://localhost:${PORT}/health || exit 1
