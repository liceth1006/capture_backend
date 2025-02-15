import io
from zipfile import ZipFile
from fastapi.responses import StreamingResponse

def create_zip_in_memory(files):
    """Crea un archivo ZIP en memoria con los archivos dados."""
    zip_buffer = io.BytesIO()
    with ZipFile(zip_buffer, "w") as zip_file:
        for filename, file_data in files:
            zip_file.writestr(filename, file_data)

    zip_buffer.seek(0)
    return StreamingResponse(zip_buffer, media_type="application/zip", headers={"Content-Disposition": "attachment; filename=screenshots.zip"})
