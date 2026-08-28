#!/bin/bash
set -euo pipefail

DB_DIR="/var/lib/microshift/kine"
CRT_DIR="/var/lib/microshift/certs/etcd-signer/etcd-serving"

# Sourced from https://github.com/k3s-io/kine/blob/6fb95f5504de608d96dec5732eee3496f4976d7a/pkg/drivers/sqlite/sqlite.go#L22
PARAMS="_journal_mode=WAL&_busy_timeout=30000&_synchronous=NORMAL&_txlock=immediate&_stmt_cache_size=20&cache=shared"

mkdir -p -m 0700 "${DB_DIR}"
exec /usr/bin/microshift-etcd-kine \
    --endpoint "sqlite://${DB_DIR}/state.db?${PARAMS}" \
    --server-cert-file "${CRT_DIR}/peer.crt" \
    --server-key-file "${CRT_DIR}/peer.key"
