#!/bin/sh
# Deploys the site with the Cloudflare account that holds shinsaikou.com. The token and account ID
# come from ~/.config/shinsaikou/cloudflare.env (or the file SAIKOU_CLOUDFLARE_ENV names), so the
# global `wrangler login`, which may belong to another account, is never used.
# Arguments go to `wrangler deploy`, for example --dry-run.
set -eu

env_file=${SAIKOU_CLOUDFLARE_ENV:-$HOME/.config/shinsaikou/cloudflare.env}
if [ ! -r "$env_file" ]; then
	echo "deploy: can't read $env_file (CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID)" >&2
	exit 1
fi

set -a
. "$env_file"
set +a
: "${CLOUDFLARE_API_TOKEN:?missing in $env_file}"
: "${CLOUDFLARE_ACCOUNT_ID:?missing in $env_file}"

cd "$(dirname "$0")/.."
exec wrangler deploy "$@"
