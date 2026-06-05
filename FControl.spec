# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/fcontrol/main.py'],
    pathex=['src'],
    binaries=[],
    datas=[
        ('.venv/lib/python3.13/site-packages/currency_converter/eurofxref-hist.zip', 'currency_converter'),
    ],
    hiddenimports=[],
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
    name='FControl',
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
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='FControl',
)
app = BUNDLE(
    coll,
    name='FControl.app',
    icon=None,
    bundle_identifier=None,
)
