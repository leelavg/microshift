#!/bin/bash
set -euo pipefail

# Check for flag file to determine backend
if [ -f /var/lib/microshift/.use-etcd ]; then
    exec /usr/bin/microshift-etcd-orig "$@"
else
    exec /usr/bin/microshift-etcd-sqlite "$@"
fi
