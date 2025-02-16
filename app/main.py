from fastapi import FastAPI
from app.routers import capture_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Web Screenshot API")

# Configuración de CORS
origins = [
    "http://localhost:5173", 
    "http://127.0.0.1:5173",
    "https://screenzip.vercel.app",
    "https://screenzip-git-main-liceth-olmos-projects.vercel.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Incluir el router de capturas
app.include_router(capture_router.router)

@app.get("/")
def read_root():
    return {"message": "API para capturar pantallas y devolver en un ZIP"}
