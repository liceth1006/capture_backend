from fastapi import APIRouter, Body
from app.controllers import capture_controller
from fastapi.responses import StreamingResponse

router = APIRouter(prefix="/api/capture", tags=["Capture"])

@router.post("/png")
async def capture(request: list = Body(...)) -> StreamingResponse:
    """Endpoint para capturar pantallas de las páginas enviadas en un archivo JSON."""
    return await capture_controller.handle_capture_png(request)


# @router.post("/pdf")
# async def capture_pdf(file: UploadFile = File(...)) -> StreamingResponse:
#     """Endpoint para capturar pantallas en PDF."""
#     return await capture_controller.handle_capture_pdf(file)