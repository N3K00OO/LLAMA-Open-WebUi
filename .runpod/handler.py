from __future__ import annotations

import runpod

PROJECT_NAME = "LLAMA Open WebUI"
PROJECT_MODE = "hub-compatibility-worker"
REPO_URL = "https://github.com/N3K00OO/LLAMA-Open-WebUi"
ISSUES_URL = "https://github.com/N3K00OO/LLAMA-Open-WebUi/issues"
GHCR_URL = "https://github.com/N3K00OO/LLAMA-Open-WebUi/pkgs/container/llama-open-webui"
IMAGE_NAME = "ghcr.io/n3k00oo/llama-open-webui:base-torch2.11.0-cu128"
UPSTREAM_URL = "https://github.com/somb1/Ollama-Open-WebUI-RP"


def base_payload() -> dict[str, object]:
    return {
        "status": "ok",
        "project": PROJECT_NAME,
        "mode": PROJECT_MODE,
        "message": (
            "This RunPod Hub package is a lightweight compatibility worker. "
            "Use the GHCR image for the full Pod, Open WebUI, and llama.cpp runtime."
        ),
        "links": {
            "repo": REPO_URL,
            "issues": ISSUES_URL,
            "ghcr": GHCR_URL,
            "upstream": UPSTREAM_URL,
        },
    }


def handler(job: dict[str, object]) -> dict[str, object]:
    job_input = job.get("input") or {}
    if not isinstance(job_input, dict):
        return {
            "status": "error",
            "error": "Job input must be a JSON object.",
            "supported_actions": ["health", "repo_info"],
        }

    action = str(job_input.get("action", "health")).strip().lower()

    if action in {"", "health", "ping", "status"}:
        return base_payload()

    if action == "repo_info":
        payload = base_payload()
        payload["image"] = IMAGE_NAME
        payload["notes"] = [
            "Primary user path: deploy the GHCR Pod image.",
            "This Hub worker exists so the repository can be indexed and tested by RunPod Hub.",
        ]
        return payload

    return {
        "status": "error",
        "error": f"Unsupported action: {action}",
        "supported_actions": ["health", "repo_info"],
        "repo": REPO_URL,
    }


if __name__ == "__main__":
    runpod.serverless.start({"handler": handler})
