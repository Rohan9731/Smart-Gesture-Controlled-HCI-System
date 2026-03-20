# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

project_dir = Path(SPECPATH)

# Bundle project assets required at runtime.
datas = [
    (str(project_dir / "resources"), "resources"),
    (str(project_dir / "animations"), "animations"),
    (str(project_dir / "script" / "modules" / "user_defined_data.json"), "script/modules"),
    (str(project_dir / ".env.example"), "."),
]

binaries = []
hiddenimports = [
    "mediapipe.python.solutions.hands",
    "mediapipe.python.solutions.drawing_utils",
    "mediapipe.python.solutions.drawing_styles",
]

# Include MediaPipe model data and native libs needed at runtime.
datas += collect_data_files("mediapipe")
binaries += collect_dynamic_libs("mediapipe")


a = Analysis(
    ["main.py"],
    pathex=[str(project_dir)],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="SmartGestureHCI",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=str(project_dir / "resources" / "dark.ico"),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="SmartGestureHCI",
)
