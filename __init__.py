# Geiru Context Suite (was Clown Context Suite). Only the names you see changed: the internal node names (H3Clown...)
# are the same, so workflows saved with the old names still load.
from .nodes import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
from .clown_keyframe import NODE_CLASS_MAPPINGS as _KEY_NODES, NODE_DISPLAY_NAME_MAPPINGS as _KEY_NAMES
from .clown_context_noise import NODE_CLASS_MAPPINGS as _NOISE_NODES, NODE_DISPLAY_NAME_MAPPINGS as _NOISE_NAMES
try:
    from .clown_hybrid_windows import NODE_CLASS_MAPPINGS as _HW_NODES, NODE_DISPLAY_NAME_MAPPINGS as _HW_NAMES
except Exception as _e:  # an older ComfyUI (no MiniMax H3 context windows) shouldn't stop the rest of the pack loading
    print(f"[Geiru Context Suite] Geiru Hybrid Windows not loaded (update ComfyUI): {_e}")
    _HW_NODES, _HW_NAMES = {}, {}

NODE_CLASS_MAPPINGS = {**NODE_CLASS_MAPPINGS, **_KEY_NODES, **_NOISE_NODES, **_HW_NODES}
NODE_DISPLAY_NAME_MAPPINGS = {**NODE_DISPLAY_NAME_MAPPINGS, **_KEY_NAMES, **_NOISE_NAMES, **_HW_NAMES}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
