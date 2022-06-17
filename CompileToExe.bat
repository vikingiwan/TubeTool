@echo off
cls
color 0a
title TubeTool Compiler
echo Compiling...
pyinstaller -i TubeTool.ico --onefile TubeTool.py
echo Finished
pause