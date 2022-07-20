"""
import cx_Freeze
import os
path = "/Users/yuli/Documents/python_projects/topdown"
included_files = []
print(included_files)
executables = [cx_Freeze.Executable("main.py")]
cx_Freeze.setup(
    name = "Top down survival game",
    options={"build_exe": {"packages":["pygame", "random"]}},
    executables = executables
)
"""


import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["pygame"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="topdown_game",
    version="0.1",
    description="My GUI application!",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)],
)
