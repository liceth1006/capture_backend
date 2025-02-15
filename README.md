# 📸 Backend de Captura de Pantallas (PNG y PDF) con FastAPI

Este proyecto es un servicio backend desarrollado con **FastAPI** que permite capturar pantallas de sitios web en formato **PNG** o **PDF**, devolviendo las capturas comprimidas en un archivo **ZIP**.

## 🚀 Características
- 📂 Endpoints para capturas en **PNG** y **PDF**  
- ⚙️ Uso de **Selenium** para automatización  
- 🧩 Retorno de capturas en **ZIP**  
- 🛡️ Validaciones con **FastAPI**  

---

## 📋 Requisitos
- **Python 3.10 o superior**  
- **Google Chrome** instalado  
- **Chromedriver** (automático con `webdriver-manager`)  

---

## 🛠️ Instalación
```bash
# Clona el repositorio
git https://github.com/liceth1006/capture_backend.git 
cd captura-backend

# Crea un entorno virtual e instala dependencias
python -m venv venv
source venv/bin/activate  
pip install -r requirements.txt
```

---

## 🧩 Archivos principales
```
📂 app/
 ┣ 📂 controllers/
 ┃ ┗ capture_controller.py      # Controladores
 ┣ 📂 services/
 ┃ ┣ capture_png_service.py     # Servicio PNG
 ┃ ┗ capture_pdf_service.py     # Servicio PDF
 ┣ 📂 utils/
 ┃ ┗ zip_utils.py              # Generación de ZIP
 ┗ main.py                     # Punto de entrada
```

---

## 🚀 Ejecución
```bash
uvicorn app.main:app --reload
```
- 📘 **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- 📗 **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

---

## 🔑 Uso de los Endpoints
### 📸 Captura en PNG
- **URL:** `/api/capture/png`  
- **Método:** `POST`  
- **Cuerpo:** JSON: `[{"url": "<URL>"}]`  

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/capture/png' \
  -H 'Content-Type: application/json' \
  -d '[{"url": "https://example.com"}]'
```

### 📄 Captura en PDF
- **URL:** `/api/capture/pdf`  
- **Método:** `POST`  
- **Cuerpo:** JSON: `[{"url": "<URL>"}]`  

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/capture/pdf' \
  -H 'Content-Type: application/json' \
  -d '[{"url": "https://example.com"}]'
```

---

## ⚙️ Configuración (`requirements.txt`):
```txt
fastapi
uvicorn
selenium
webdriver_manager
python-multipart
```

---

## 🐞 Manejo de Errores
- **400 Bad Request:** Solicitud inválida  
- **500 Internal Server Error:** Error en la captura  



## 🛡️ Licencia
Proyecto bajo la licencia **MIT**  

---

## 📞 Contacto
- Desarrollado por: **Liceth Olmos**  
- 📧 Contacto: [https://www.licetholmos.com/]  

