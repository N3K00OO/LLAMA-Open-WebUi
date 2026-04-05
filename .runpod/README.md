# LLAMA Open WebUI

`LLAMA Open WebUI` is a fork of [somb1/Ollama-Open-WebUI-RP](https://github.com/somb1/Ollama-Open-WebUI-RP), reworked into a `llama.cpp`-focused project with Open WebUI, JupyterLab, and GHCR-based image publishing.

## Important

This RunPod Hub package is a lightweight compatibility worker for Hub indexing and validation.

It is **not** the full Pod runtime. The main product is the GHCR Pod image:

```text
ghcr.io/n3k00oo/llama-open-webui
```

Recommended default tag:

```text
ghcr.io/n3k00oo/llama-open-webui:base-torch2.11.0-cu128
```

## Main Project Links

- GitHub: <https://github.com/N3K00OO/LLAMA-Open-WebUi>
- Issues: <https://github.com/N3K00OO/LLAMA-Open-WebUi/issues>
- GHCR package: <https://github.com/N3K00OO/LLAMA-Open-WebUi/pkgs/container/llama-open-webui>
- Original upstream: <https://github.com/somb1/Ollama-Open-WebUI-RP>

## Full Pod Runtime

The full image provides:

- `llama.cpp` started as `./llama-server`
- Open WebUI wired to the local OpenAI-compatible `/v1` endpoint
- JupyterLab for notebooks and terminal access
- boot-time Hugging Face and `wget` model downloads

Recommended ports for the Pod image:

- `8081` for Open WebUI
- `11435` for the proxied llama.cpp API
- `8889` for JupyterLab

## Hub Worker API

This Hub worker supports two simple actions:

- `health`
- `repo_info`

Example:

```json
{
  "action": "repo_info"
}
```

Use this Hub entry for repository discovery and compatibility. Use the GHCR Pod image for the real WebUI deployment path.
