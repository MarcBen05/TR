@ECHO off
set /p ui=Enter UI file:
set /p py=Enter desired Python Script name:
call pyuic5 %ui%.ui -o %py%.py
::call pyside2-uic %ui%.ui -o %py%.py
PAUSE