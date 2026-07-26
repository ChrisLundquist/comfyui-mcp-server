"""Shared connection defaults.

ComfyUI Desktop serves on port 8000; the classic standalone `python main.py`
default is 8188. Keeping the fallback in one place is what stops the two from
drifting apart across server.py and the managers, which is the "thor:8188"
class of bug called out in docs/ARCHITECTURE.md. Set COMFYUI_URL to override.
"""

DEFAULT_COMFYUI_URL = "http://localhost:8000"
