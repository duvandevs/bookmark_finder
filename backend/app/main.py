from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import create_tables


# Crear la app FastAPI
app = FastAPI(
    title="Bookmark Finder API",
    description="App para buscar y gestionar bookmarks",
    version="1.0.0"
)

# Crear las tablas al iniciar la aplicación
@app.on_event("startup")
def startup_event():
    create_tables()

# Configurar CORS para permitir requests desde el frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios exactos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de prueba -  primer endpoint
@app.get("/")
def read_root():
    return {"message": "¡Bookmark Finder API está funcionando!", "version": "1.0.0"}

# Endpoint de salud del sistema
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "bookmark-finder"}

# Cuando ejecuta la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)