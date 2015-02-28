#! usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from cx_Freeze import setup, Executable

build_exe_options = {"icon": "net.ico", "include_files": ["net.ico"], "constants": []}
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "basher",
      version = "1.0.27",
      author = "Safoyeth",
      description = u"Простой парсер сайта bash.im",
      options = {"build_exe": build_exe_options},
      executables = [Executable("basher.py", base = base, targetName = "basher.exe",
                                shortcutName = "Basher", shortcutDir = "DesktopFolder",
                                compress = True)])
