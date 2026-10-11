# DevOps INF 345 notes service

## What it does
A tiny HTTP notes service (Python standard library only). Endpoints:
`GET /`, `GET /healthz`, `GET /notes`.

## How to run
```bash
./scripts/run.sh
```
The service listens on the port from the `PORT` environment variable
(default `8080`).

## How to test
```bash
./scripts/test.sh
```
Prints `TESTS: n/n` and exits 0 when everything passes.

## Port
`PORT` (env), default 8080. Example: `PORT=9000 ./scripts/run.sh`.
