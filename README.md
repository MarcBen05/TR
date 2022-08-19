<p align="center">
  <img src="Imatges/logo.png" alt="drawing" width="75"/>
  <h1 align="center">Alou</h1>
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

> Interfície gràfica d'**Alou**.

## Instal·lació i execució
Primerament, s'ha de clonar el repistori en una carpeta. Això es fa descarregant el repositori manualment o mitjançant el comandament següent a la terminal:
```
git clone https://www.github.com/MarcBen05/TR
```
> En cas d'emprar el comandament anterior, es requereix l'eina *Git*.

Per als usuaris de Windows, una vegada descarregat el repositori no cal instal·lar cap eina externa. Només que s'obri la carpeta anomenada *Executable* i s'executi el programa *Alou.exe* aquest funcionarà. En el cas dels usuaris de Linux, aquests hauran de descarregar-se Python (3.9) i les llibreries llistades a baix.

### Llibreries necessàries
 - PyQt5 https://pypi.org/project/PyQt5/
 - PySide2 https://pypi.org/project/PySide2/
 - NumPy https://pypi.org/project/numpy
 - Pandas https://https://pypi.org/project/pandas/
 - Pillow https://pypi.org/project/pillow/
 - sys *(Ja està instal·lat als dispotitius)*
 
 Una vegada que **Alou** i les llibreries estiguin instal·lats, només cal obrir la terminal i executar el següent comandament:
 ```
 python3 main.py
 ```
 > Comandament al sistema operatiu *Linux*.
