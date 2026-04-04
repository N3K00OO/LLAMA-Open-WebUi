[![Build and Publish GHCR Images](https://github.com/N3K00OO/LLAMA-Open-WebUi/actions/workflows/build.yml/badge.svg)](https://github.com/N3K00OO/LLAMA-Open-WebUi/actions/workflows/build.yml)

# LLAMA Open WebUI

This image is a llama-only RunPod base image:

- `llama.cpp` is built in CI and started as `./llama-server`
- Open WebUI is wired to the local OpenAI-compatible `/v1` endpoint
- JupyterLab is included for notebook and terminal access

GitHub Actions refreshes upstream `llama.cpp` and Open WebUI versions at build time, pushes the images to GHCR, and verifies each published tag before the workflow passes.

## Images

Published package:

```text
ghcr.io/n3k00oo/llama-open-webui
```

Available tags:

| Tag | CUDA |
| --- | --- |
| `base-torch2.11.0-cu124` | 12.4 |
| `base-torch2.11.0-cu125` | 12.5 |
| `base-torch2.11.0-cu126` | 12.6 |
| `base-torch2.11.0-cu128` | 12.8 |
| `base-torch2.11.0-cu130` | 13.0 |

Use the full image name in RunPod:

```text
ghcr.io/n3k00oo/llama-open-webui:base-torch2.11.0-cu128
```

## Runtime

`llama-server` listens on internal port `11434` and Open WebUI connects to:

```text
http://127.0.0.1:11434/v1
```

Place GGUF models in:

```text
/workspace/models
```

Startup behavior:

- if there is exactly one root-level `*.gguf` file in `/workspace/models`, it is auto-detected
- if there are multiple files, split shards, or nested folders, set `LLAMA_MODEL` explicitly
- Open WebUI uses the local llama.cpp endpoint

## Exposed Ports

| Port | Purpose |
| --- | --- |
| `22` | SSH |
| `8081` | Open WebUI |
| `11435` | proxied llama.cpp API |
| `8889` | JupyterLab |

## Environment Variables

| Variable | Description | Default |
| --- | --- | --- |
| `JUPYTERLAB_PASSWORD` | Password for JupyterLab | unset |
| `TIME_ZONE` | Time zone, for example `Asia/Bangkok` | `Etc/UTC` |
| `START_LLAMA_SERVER` | Starts `./llama-server` on boot | `True` |
| `LLAMA_MODEL` | Absolute path to the GGUF file to load | auto-detect |
| `LLAMA_ALIAS` | Model name exposed by `/v1/models` | GGUF filename |
| `LLAMA_CTX_SIZE` | Value passed to `--ctx-size` | `4096` |
| `LLAMA_GPU_LAYERS` | Value passed to `--n-gpu-layers` | `999` |
| `LLAMA_PARALLEL` | Value passed to `--parallel` | `1` |
| `LLAMA_SERVER_API_KEY` | Optional API key for `llama-server` | unset |
| `LLAMA_SERVER_EXTRA_ARGS` | Extra flags appended to `llama-server` | unset |
| `DATA_DIR` | Open WebUI data directory | `/workspace/data` |
| `WEBUI_AUTH` | Enables Open WebUI auth | `False` |
| `RESET_CONFIG_ON_START` | Re-applies provider config on startup | `True` |

Set variables in RunPod under `Edit Pod/Template` > `Add Environment Variable`.

If `WEBUI_AUTH=False` does not take effect, clear the existing Open WebUI data volume first. Open WebUI keeps auth state in its database after first boot.

## Logs

| Component | Log Path |
| --- | --- |
| JupyterLab | `/workspace/logs/jupyterlab.log` |
| llama.cpp | `/workspace/logs/llama-server.log` |
| Open WebUI | `/workspace/logs/open-webui.log` |

## Included Software

| Component | Version / Notes |
| --- | --- |
| Ubuntu | 22.04 |
| Python | 3.11 |
| PyTorch | 2.11.0 |
| CUDA images | 12.4 through 13.0 |
| Inference backend | `llama.cpp` |
| UI | Open WebUI |
| Extras | JupyterLab, `hf`, `nvtop` |

## References

- [Open WebUI llama.cpp quick start](https://docs.openwebui.com/getting-started/quick-start/starting-with-llama-cpp/)
- [Open WebUI environment configuration](https://docs.openwebui.com/reference/env-configuration/)
- [llama.cpp server documentation](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)

Feedback & issues: [GitHub Issues](https://github.com/N3K00OO/LLAMA-Open-WebUi/issues)
