<p align="center">
  <img src="/Programa/assets/logo.png" alt="drawing" width="75"/>
  <h1 align="center">Alou (Nom subjecte a canvis)</h1>
</p>

[![Python 3.9](https://img.shields.io/badge/python-3.9-yellow.svg)](https://www.python.org/)
[![Build](https://img.shields.io/badge/Supported_OS-Windows-orange.svg)]()
[![Build](https://img.shields.io/badge/Supported_OS-Linux-orange.svg)]()

Aquest repositori conté tot el codi del programa **Alou**, el prototip de GPS que he dissenyat per al meu treball de recerca.

## Què és exactament Alou?
Alou és un prototip de GPS per al meu treball de recerca que intenta apel·lar més als joves i soluciona un dèficit que els GPS convencionals tenen. Aquest dèficit en concret és la falta de funcionalitat per a fer rutes. Els GPS convencionals troben el camí més curt entre una localització i el destí, però no poden trobar la ruta òptima entre una localització i tots els llocs propers amb una certa característica, com podria ser que aquests fossin monuments. Altrament, Alou pretén apel·lar als joves prioritzant les localitzacions que ells indiquin en una enquesta. En ser un prototip, aquest només se centrarà en una zona en concret. No obstant, fer que treballi amb geo-localització a temps real és plausible a causa de com s'estructura el programa.

<p align="center">
  <img src="/Imatges/App.PNG"/>
</p>

## Instal·lació i execució
En cas de voler descarregar el programa, els arxius essencials es troben a la carpeta 'Programa'. A més, són necessàries algunes llibreries de Python i, òbviament, és necessari que Python (3.9) estigui instal·lat al dispositiu en què s'executi.

### Llibreries necessàries
 - PyQt5 https://pypi.org/project/PyQt5/
 - PySide2 https://pypi.org/project/PySide2/
 - Pandas https://https://pypi.org/project/pandas/
 - Pillow https://pypi.org/project/pillow/
 - os *(Ja està instal·lat als dispotitius)*
 
 Una vegada que **Alou** i les llibreries estiguin instal·lats, només cal obrir la terminal i executar el següent comandament:
 ```
 py main.py
 ```
