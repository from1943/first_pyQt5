# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

SETUP_DIR = 'C:\\Users\\xuhan\\PycharmProjects\\exportGui\\'
a = Analysis(['main.py', 'export.py', 'create.py'],
             pathex=['C:\\Users\\xuhan\\PycharmProjects\\exportGui'],
             binaries=[],
             datas=[('static','static')],
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
          [("config.ini","C:/Users/xuhan/PycharmProjects/exportGui/static/config.ini","static"),
	   ("xls.png","C:/Users/xuhan/PycharmProjects/exportGui/static/xls.png","static"),
	   ("xlsx.png","C:/Users/xuhan/PycharmProjects/exportGui/static/xlsx.png","static")],
          name='export',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='C:\\Users\\xuhan\\PycharmProjects\\exportGui\\Excel.ico')
