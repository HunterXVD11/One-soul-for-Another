# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['ControlaF.py'],
             pathex=['C:\\Users\\gabri\\OneDrive\\Área de Trabalho\\ASFA\\one-soul-for-another'],
             binaries=[],
             datas=[("Cobra_Animations","Cobra_Animations"),("Cogumelho_Animations","Cogumelho_Animations"),("Disparos_animations","Disparos_animations"),("Esqueleto_animations","Esqueleto_animations"),("Fase2_Tiles","Fase2_Titles"),("Goblin","Goblin"),("Ladino_Animations","Ladino_Animatios"),("Minhoca_Animations","Minhoca_Animations"),("Monstro_OlhoVoador_animations","Monstro_OlhoVoador_animations"),("Morte_animations","Morte_animations"),("PPlay","PPlay"),("Player_animations","Player_animations"),("Slime_Animations","Slime_Animations")],
             hiddenimports=[],
             hookspath=[],
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
          name='ControlaF',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
