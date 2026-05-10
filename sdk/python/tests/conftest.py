from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for path in (ROOT / "src", ROOT / "examples" / "demo-notes" / "src"):
    path_str = str(path)
    if path_str in sys.path:
        sys.path.remove(path_str)
    sys.path.insert(0, path_str)

local_aclip_root = ROOT / "src" / "aclip"
loaded_aclip = sys.modules.get("aclip")
loaded_file = Path(getattr(loaded_aclip, "__file__", "")) if loaded_aclip else None
if loaded_file and not loaded_file.is_relative_to(local_aclip_root):
    for module_name in list(sys.modules):
        if module_name == "aclip" or module_name.startswith("aclip."):
            del sys.modules[module_name]
