#!/usr/bin/env bash

ACCOUNT_ID="${ACCOUNT_ID:-187914334366}"
MSTAR_ENV="${MSTAR_ENV:-stg}"
if [[ "${MSTAR_ENV}" == "prod" || "${MSTAR_ENV}" == "dr" ]]; then
    ACCOUNT_ID="062740692535"
fi
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd -P)"
TARGET_DIR="$(realpath "$(dirname "${DIR}")/target")"

DEPLOY_ROLE="${DEPLOY_ROLE:-DATASVC-ENGR-Deploy}"
AWS_PROPERTIES="${AWS_PROPERTIES:-${TARGET_DIR}/.credential}"

# clean
[ ! -d "${TARGET_DIR}" ] && mkdir "${TARGET_DIR}"

set +x
RESPONSE="$(aws sts assume-role \
    --role-arn "arn:aws:iam::${ACCOUNT_ID}:role/${DEPLOY_ROLE}" \
    --duration-seconds 900 \
    --role-session-name "${BUILD_TAG:-$(basename "$0")}")" || exit 1
cat <<EOF >"${AWS_PROPERTIES}"
export AWS_ACCESS_KEY_ID=$(echo "$RESPONSE" | jq -r .Credentials.AccessKeyId)
export AWS_SECRET_ACCESS_KEY=$(echo "$RESPONSE" | jq -r .Credentials.SecretAccessKey)
export AWS_SESSION_TOKEN=$(echo "$RESPONSE" | jq -r .Credentials.SessionToken)
EOF