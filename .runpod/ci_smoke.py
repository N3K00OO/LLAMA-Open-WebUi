from __future__ import annotations

import importlib.util
from pathlib import Path


HANDLER_PATH = Path("/handler.py")


def load_handler_module():
    spec = importlib.util.spec_from_file_location("runpod_hub_handler", HANDLER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load handler module from {HANDLER_PATH}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    module = load_handler_module()

    health = module.handler({"input": {"action": "health"}})
    assert health["status"] == "ok"
    assert health["mode"] == "hub-compatibility-worker"
    assert "ghcr" in health["links"]

    repo_info = module.handler({"input": {"action": "repo_info"}})
    assert repo_info["status"] == "ok"
    assert repo_info["image"] == "ghcr.io/n3k00oo/llama-open-webui:base-torch2.11.0-cu128"
    assert any("GHCR Pod image" in note for note in repo_info["notes"])

    invalid = module.handler({"input": {"action": "bogus"}})
    assert invalid["status"] == "error"
    assert invalid["supported_actions"] == ["health", "repo_info"]

    malformed = module.handler({"input": "bad"})
    assert malformed["status"] == "error"
    assert malformed["error"] == "Job input must be a JSON object."

    print("runpod-hub-ci-ok")


if __name__ == "__main__":
    main()
