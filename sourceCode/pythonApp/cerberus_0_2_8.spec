# -*- mode: python -*-

block_cipher = None


a = Analysis(['/Users/z036415/personalGitHub/document-search/sourceCode/cerberus_0_2_8.py'],
             pathex=['/Users/z036415/personalGitHub/document-search/sourceCode/pythonApp'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='cerberus_0_2_8',
          debug=False,
          strip=False,
          upx=True,
          console=True )
