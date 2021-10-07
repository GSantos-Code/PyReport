from cx_Freeze import setup, Executable
import sys
import os

exe = Executable(
      script="utils2.py",
      base="Win32GUI",
      targetName="PyReport.exe",
      icon= "icone.ico"
     )
setup(
      name="PyReport.exe",
      version="1.0",
      author="Gabriel Santos",
      description="Copyright 2021",
      executables=[exe],
      scripts=[
               os. getcwd()+ '\\Capture.py',
               os. getcwd()+ '\\functions.py',
               os. getcwd()+ '\\main.py',
               os. getcwd()+ '\\utils.py',
               os. getcwd()+ '\\ConvGIF.py'
               
               ],
      options = {'build_exe': {'include_files': [("imgs","imgs"),("fonts","fonts"),("tools","tools")]}}
      ) 
