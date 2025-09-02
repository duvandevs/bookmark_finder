from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuración de la base de datos SQLite
DATABASE_URL = "sqlite:///./bookmarks.db"

# Crear el engine (motor) de la base de datos
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}  # Necesario para SQLite
)

# Crear una clase para las sesiones de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para nuestros modelos
Base = declarative_base()

# Función para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para crear todas las tablas
def create_tables():
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas de base de datos creadas exitosamente")