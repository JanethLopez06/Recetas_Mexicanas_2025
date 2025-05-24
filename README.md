#  Sazón Mexicano

¡Bienvenida/o a **Sazón Mexicano**!  
Una aplicación web interactiva desarrollada con [Reflex (Pynecone)](https://reflex.dev/) y Python.  
Disfruta de una colección de recetas tradicionales con estilo retro, explicadas paso a paso, incluyendo ingredientes, instrucciones detalladas y tablas nutricionales.

---

## 🌐 Demo en línea

👉 [Haz clic aquí para ver la app en Vercel](https://sazonmexicano.vercel.app/)  

---

## 🧪 Tecnologías utilizadas

- 🐍 Python
- ⚛️ Reflex (antes Pynecone)
- 🎮 NES.css (para estilo retro tipo 8-bits)
- ☁️ Despliegue con [Vercel](https://vercel.com)

---

## 📖 ¿Cómo usar la página?

- Navega entre las recetas usando los botones **"Menú Principal"** y **"Siguiente Receta"**.
- Cada receta muestra sus **ingredientes, instrucciones paso a paso y tabla nutricional**.
- Descubre más recetas con solo dar clic en **"Siguiente Receta"**.
- ¡Sigue las instrucciones y disfruta cocinando platillos mexicanos tradicionales!

---

## 🚀 Cómo ejecutar el proyecto localmente

```bash
# Clona el repositorio
git clone https://github.com/JanethLopez06
/Sazon_Mexicano.git
cd tu-repo

# Crea y activa el entorno virtual
python -m venv .venv
source .venv/bin/activate         # Linux/macOS
# o
source .venv/Scripts/activate     # Windows (Git Bash)

# Instala Reflex y dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Ejecuta la app en modo desarrollo
reflex run
# La app se abrirá automáticamente en tu navegador en:
👉 http://localhost:3000
