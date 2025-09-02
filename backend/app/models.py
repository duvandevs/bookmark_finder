from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from .database import Base

# Modelo para los bookmarks
class Bookmark(Base):
    __tablename__ = "bookmarks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)  # Título del bookmark
    url = Column(Text, nullable=False)           # URL del bookmark
    folder = Column(String(200), nullable=True)  # Carpeta/categoría
    date_added = Column(String(50), nullable=True)  # Fecha del bookmark original
    source_file = Column(String(200), nullable=True)  # De qué archivo vino
    created_at = Column(DateTime, default=func.now())  # Cuándo se agregó a nuestra DB
    
    def __repr__(self):
        return f"<Bookmark(title='{self.title}', url='{self.url}')>"

# Modelo para los archivos procesados
class ProcessedFile(Base):
    __tablename__ = "processed_files"
    
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String(200), nullable=False)
    file_type = Column(String(10), nullable=False)  # 'html' o 'json'
    bookmarks_count = Column(Integer, default=0)
    processed_at = Column(DateTime, default=func.now())
    
    def __repr__(self):
        return f"<ProcessedFile(filename='{self.filename}', count={self.bookmarks_count})>"