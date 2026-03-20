"""Runtime-safe path helpers for source and PyInstaller builds."""

from pathlib import Path
import os
import shutil
import sys

APP_DIR_NAME = "SmartGestureHCI"


def bundle_root() -> Path:
    """Return the base directory where bundled resources are available."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent.parent


def app_runtime_dir() -> str:
    """Return directory of executable in frozen mode, project root in source mode."""
    if getattr(sys, "frozen", False):
        return str(Path(sys.executable).resolve().parent)
    return str(bundle_root())


def resource_path(*parts: str) -> str:
    """Resolve a resource path from the bundle/source root."""
    return str(bundle_root().joinpath(*parts))


def user_data_path(filename: str = "user_defined_data.json") -> str:
    """Return a writable user data file path, seeded from packaged defaults."""
    base_dir = Path(os.getenv("APPDATA") or app_runtime_dir())
    data_dir = base_dir / APP_DIR_NAME
    data_dir.mkdir(parents=True, exist_ok=True)

    data_file = data_dir / filename
    if not data_file.exists():
        seed = Path(resource_path("script", "modules", "user_defined_data.json"))
        if seed.exists():
            shutil.copy2(seed, data_file)
        else:
            data_file.write_text('{"userDefinedControls": {}}', encoding="utf-8")

    return str(data_file)
