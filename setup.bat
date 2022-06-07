@echo off
color 0C
pip install requests
pip install pystyle
echo Done!
ping localhost -n 2 >nul
echo python "Bloody Joiner.py" >> start.bat
start start.bat
del setup.bat