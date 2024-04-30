import sys
from cx_Freeze import setup, Executable

# Specify the main script and other options
console_script = 'Group_2_OS.py'

base = None  # Use None for console-based application

options = {
    'build_exe': {
        'includes': ['tkinter', 'datetime'],  # Add any necessary modules
        'include_files': [],  # Add any additional files or data needed
        'packages': ['os', 'shutil'],  # Add required packages
    }
}

executables = [
    Executable(script=console_script, base=base)
]

setup(
    name='Group_2_OS',
    version='1.0',
    description='Group 2 Operating System Command Line Interface',
    options=options,
    executables=executables
)
