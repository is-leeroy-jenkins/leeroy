# -*- mode: python ; coding: utf-8 -*-
"""Package Leeroy and its dynamically loaded application dependencies."""
from pathlib import Path
from PyInstaller.utils.hooks import collect_all, collect_submodules, copy_metadata

root = Path( SPECPATH )
datas = [(str( root / 'app.py' ), '.'),
         (str( root / 'resources' ), 'resources'),
         (str( root / '.streamlit' / 'config.toml' ), '.streamlit')]
# Runtime databases are created in user storage; development data and secrets are excluded.
hiddenimports = ['config', 'boogr']
binaries = []
for package in ('streamlit', 'webview',
                'plotly', 'sqlite_vec', 'sentence_transformers', 'transformers',
                'torch', 'torchvision', 'llama_cpp'):
    package_datas, package_bins, package_hidden = collect_all( package )
    datas += package_datas
    binaries += package_bins
    hiddenimports += package_hidden
for distribution in ('streamlit', 'sentence-transformers', 'transformers'):
    datas += copy_metadata( distribution, recursive=True )

a = Analysis( [str( root / 'desktop.py' )], pathex=[str( root )],
    binaries=binaries, datas=datas, hiddenimports=hiddenimports,
    hookspath=[], runtime_hooks=[], excludes=[], noarchive=False )
pyz = PYZ( a.pure )
exe = EXE( pyz, a.scripts, [], exclude_binaries=True, name='Leeroy',
    console=False, disable_windowed_traceback=False )
coll = COLLECT( exe, a.binaries, a.datas, strip=False, upx=False, name='Leeroy' )
