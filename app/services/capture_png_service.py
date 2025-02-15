import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from app.utils import zip_utils
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

async def capture_screenshots(data: list) -> StreamingResponse:
    """Realiza las capturas de pantalla y las devuelve en un ZIP."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    screenshots = []

    for item in data:
        url = item.get("url")
        if not url:
            continue

        domain = urlparse(url).netloc.replace("www.", "")
        try:
            driver.get(url)
            time.sleep(5)
            screenshot = driver.get_screenshot_as_png()
            screenshots.append((f"{domain}.png", screenshot))
            print(f"Captura realizada: {domain}.png")
        except Exception as e:
            print(f"Error al capturar {url}: {e}")

    driver.quit()

    return zip_utils.create_zip_in_memory(screenshots)
