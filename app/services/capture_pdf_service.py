from PIL import Image as PILImage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Image, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from fastapi.responses import StreamingResponse
from urllib.parse import urlparse
import json
import os
import time
from io import BytesIO
import zipfile

async def capture_screenshots(data: list) -> StreamingResponse:
    """Captura pantallas y genera PDFs con imágenes ajustadas a la página."""
    try:
        # Configurar navegador

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--remote-debugging-port=9222")
        options.binary_location = os.environ.get("CHROME_BIN", "/usr/bin/chromium")
        driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
        )
        pdf_files = []
        max_width, max_height = 500, 700  

        
        output_dir = "/tmp/screenshots"
        os.makedirs(output_dir, exist_ok=True)

        for item in data:
            url = item.get("url")
            if not url:
                continue

            domain = urlparse(url).netloc.replace("www.", "")

            try:
                # Capturar pantalla
                driver.get(url)
                time.sleep(3)  # Esperar a que cargue la página

                # Definir las rutas para la imagen y el PDF
                img_path = os.path.join(output_dir, f"{domain}_screenshot.png")
                pdf_path = os.path.join(output_dir, f"{domain}_screenshot.pdf")

                # Guardar captura de pantalla
                if driver.save_screenshot(img_path):
                    print(f"✅ Captura guardada: {img_path}")

                    # Redimensionar imagen si es necesario
                    with PILImage.open(img_path) as img:
                        img_ratio = img.width / img.height
                        if img.width > max_width or img.height > max_height:
                            if img.width > img.height:
                                new_width = max_width
                                new_height = int(max_width / img_ratio)
                            else:
                                new_height = max_height
                                new_width = int(max_height * img_ratio)
                            img = img.resize((new_width, new_height))
                            img.save(img_path)

                    # Crear PDF con imagen ajustada
                    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
                    story = []
                    style = getSampleStyleSheet()["Title"]
                    story.append(Paragraph(f"Captura de {domain}", style))
                    story.append(Image(img_path, width=new_width, height=new_height))
                    doc.build(story)

                    pdf_files.append(pdf_path)
                else:
                    print(f"⚠️ No se pudo guardar la captura para: {url}")

            except Exception as e:
                print(f"❌ Error al capturar {url}: {e}")

        driver.quit()

        # Crear un archivo ZIP con los PDFs generados
        if not pdf_files:
            raise FileNotFoundError("No se generaron capturas.")

        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            for pdf_file in pdf_files:
                zip_file.write(pdf_file, os.path.basename(pdf_file))

        zip_buffer.seek(0)
        return StreamingResponse(zip_buffer, media_type="application/zip",
                                  headers={"Content-Disposition": "attachment; filename=capturas.zip"})

    except Exception as e:
        print(f"🚨 Error general: {e}")
        return {"error": str(e)}
