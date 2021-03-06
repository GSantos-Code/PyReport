from cx_Freeze import setup, Executable
import sys

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
               r'C:\Users\gabriel.azevedo\Desktop\PyReport-win11\Capture.py',
               r'C:\Users\gabriel.azevedo\Desktop\PyReport-win11\functions.py',
               r'C:\Users\gabriel.azevedo\Desktop\PyReport-win11\main.py',
               r'C:\Users\gabriel.azevedo\Desktop\PyReport-win11\utils.py'
               ],
      options = {'build_exe': {'include_files': [("imgs","imgs"),("fonts","fonts")]}}
      ) 
