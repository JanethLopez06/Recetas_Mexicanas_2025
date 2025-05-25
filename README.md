# 🌮 Sazón Mexicano
¡Bienvenida/o a Sazón Mexicano!
Una aplicación web interactiva desarrollada con Reflex (antes Pynecone) y Python.
Disfruta de una colección de recetas tradicionales con estilo retro, explicadas paso a paso, incluyendo ingredientes, instrucciones detalladas y tablas nutricionales.

---

## 🌐 Demo en línea
👉 Haz clic aquí para ver la app en Vercel

---

## 🧪 Tecnologías utilizadas
🐍 Python

⚛️ Reflex (antes Pynecone)

🎮 NES.css (para estilo retro tipo 8-bits)

☁️ Despliegue con Vercel

---

## 📖 ¿Cómo usar la página?
Navega entre las recetas usando los botones "Menú Principal" y "Siguiente Receta".

Cada receta muestra sus ingredientes, instrucciones paso a paso y tabla nutricional.

Descubre más recetas con solo dar clic en "Siguiente Receta".

¡Sigue las instrucciones y disfruta cocinando platillos mexicanos tradicionales!

---

## 🚀 Cómo ejecutar el proyecto localmente
### Clona el repositorio
git clone https://github.com/JanethLopez06/Sazon_Mexicano.git
cd Sazon_Mexicano

### Crea y activa el entorno virtual
python -m venv .venv
source .venv/bin/activate         # Linux/macOS
### o
source .venv/Scripts/activate     # Windows (Git Bash)

### Instala Reflex y dependencias
pip install --upgrade pip
pip install -r requirements.txt

### Ejecuta la app en modo desarrollo
reflex run

### La app se abrirá automáticamente en tu navegador:
### 👉 http://localhost:3000

---

## 🛠️ Construcción y despliegue para Vercel
Para preparar la versión lista para producción y subirla a Vercel, utiliza el script build.sh incluido en el proyecto.

### ¿Qué hace el script build.sh?
- Activa el entorno virtual .venv.

- Actualiza pip e instala todas las dependencias.

- Elimina la carpeta public si existe (para limpiar versiones anteriores).

- Inicializa Reflex (si es necesario).

- Exporta solo el frontend, creando un archivo comprimido frontend.zip.

- Limpia nuevamente la carpeta public.

- Descomprime el contenido de frontend.zip dentro de la carpeta public.

- Elimina el archivo frontend.zip.

- Desactiva el entorno virtual.

## 📁 Importante: la carpeta public y Vercel
La carpeta public es la que Vercel utiliza para desplegar tu sitio estático.

En la configuración de tu proyecto en Vercel, asegúrate de que la carpeta de salida (Output Directory) esté configurada como public.

Cada vez que hagas cambios en el proyecto y quieras actualizar el despliegue, ejecuta el script para regenerar la carpeta public con los últimos archivos.



