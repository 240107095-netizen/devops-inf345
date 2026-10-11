#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

rc=0
out=$(python3 -m unittest discover -s tests 2>&1) || rc=$?
printf '%s\n' "$out"

total=$(printf '%s\n' "$out" | sed -n 's/^Ran \([0-9]\+\) tests\?.*/\1/p' | tail -n1)
total=${total:-0}

bad=0
failed_line=$(printf '%s\n' "$out" | grep '^FAILED' || true)
for n in $(printf '%s' "$failed_line" | grep -o '[0-9]\+' || true); do
  bad=$((bad + n))
done
if [ "$rc" -ne 0 ] && [ "$bad" -eq 0 ]; then bad=1; fi
if [ "$total" -eq 0 ]; then total=1; fi

passed=$((total - bad))
if [ "$passed" -lt 0 ]; then passed=0; fi
echo "TESTS: ${passed}/${total}"
exit "$rc"
