# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['SUPER-TWISTER.py'],
             pathex=[],
             binaries=[],
             datas=[('wavs/mano destra.wav', 'wavs'), ('wavs/mano sinistra.wav', 'wavs'), ('wavs/piede destro.wav', 'wavs'), ('wavs/piede sinistro.wav', 'wavs'), ('wavs/1.wav', 'wavs'), ('wavs/2.wav', 'wavs'), ('wavs/3.wav', 'wavs'), ('wavs/4.wav', 'wavs'), ('wavs/5.wav', 'wavs'), ('wavs/6.wav', 'wavs'), ('wavs/rosso.wav', 'wavs'), ('wavs/verde.wav', 'wavs'), ('wavs/blu.wav', 'wavs'), ('wavs/giallo.wav', 'wavs')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='SUPER-TWISTER',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
