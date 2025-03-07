# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['HaloClock.py'],
    pathex=[],
    binaries=[],
    datas=[('Halo.ttf', '.'), ('Halo4OST.mp3', '.'), ('halo-icon-36667.ico', '.')],
    hiddenimports=['PyQt5.sip'],
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
    a.binaries,
    a.datas,
    [],
    name='HaloClock',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['halo-icon-36667.ico'],
)
