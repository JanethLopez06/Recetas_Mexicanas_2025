#!/bin/bash

# Activar entorno virtual (en bash)
source .venv/Scripts/activate

python.exe -m pip install --upgrade pip
pip install -r requirements.txt

reflex init
reflex export --frontend-only

rm -rf public
unzip fronted.zip -d public
rm fronted.zip

# Desactivar entorno virtual
deactivate
