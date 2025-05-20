#!/bin/bash

# Activar entorno virtual
source .venv/Scripts/activate   # Linux/macOS
# o en Git Bash Windows:
# source .venv/Scripts/activate

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt

# Borrar carpeta public si existe
rm -rf public

# Inicializar Reflex (según tu proyecto)
reflex init

# Exportar solo frontend
reflex export --frontend-only

# Borrar carpeta public (otra vez, si es necesario)
rm -rf public

# Descomprimir frontend.zip en public
unzip frontend.zip -d public

# Borrar frontend.zip
rm -f frontend.zip

# Desactivar entorno virtual
deactivate
