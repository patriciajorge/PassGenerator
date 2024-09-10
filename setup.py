import sys
import os
from cx_Freeze import setup, Executable

# Lista de arquivos a serem incluídos no build
files = ['pass.ico'] 

# Comando para esconder o console
if sys.platform == 'win32':
    base = 'Win32GUI'

config = Executable(
    script='app.py',
    icon='pass.ico',
    base=base
)

setup(
    name='PassGenerator',
    version='1.0',
    description='The project is a password generator using Tkinter, allowing users to set length and character types. It displays the generated password after clicking "Generate Password.',
    author='Patrícia Jorge',
    options={'build_exe': {'include_files': files, 'include_msvcr': True}},
    executables=[config]
)