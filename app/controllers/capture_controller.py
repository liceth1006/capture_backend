from fastapi import HTTPException
from app.services import capture_png_service
from app.services import capture_pdf_service
from fastapi.responses import StreamingResponse

async def handle_capture_png(request: list) -> StreamingResponse:
    """Recibe el JSON con las URLs y delega la captura al servicio."""
    if not isinstance(request, list):
        raise HTTPException(status_code=400, detail="El cuerpo debe ser una lista de objetos con URL.")
    
    for item in request:
        if not isinstance(item, dict) or 'url' not in item:
            raise HTTPException(status_code=400, detail="Cada objeto debe ser un diccionario con la clave 'url'.")
    
    return await capture_png_service.capture_screenshots(request)

async def handle_capture_pdf(request: list) -> StreamingResponse:
    """Recibe el JSON con las URLs y delega la captura al servicio."""
    if not isinstance(request, list):
        raise HTTPException(status_code=400, detail="El cuerpo debe ser una lista de objetos con URL.")
    
    for item in request:
        if not isinstance(item, dict) or 'url' not in item:
            raise HTTPException(status_code=400, detail="Cada objeto debe ser un diccionario con la clave 'url'.")
    
    return await capture_pdf_service.capture_screenshots(request)



