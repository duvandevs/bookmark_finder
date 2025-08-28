# Especificaciones Técnicas - Bookmark Finder

## Casos de Uso Principales

### 1. Cargar Archivos de Bookmarks
- Usuario arrastra múltiples archivos (.html/.json)
- Sistema detecta formato automáticamente
- Procesa y almacena en SQLite local

### 2. Buscar Bookmarks
- Búsqueda por texto libre en título/URL/carpeta
- Filtrado por carpetas específicas
- Resultados paginados y ordenables

### 3. Visualizar Resultados
- Lista con título, URL, carpeta, fecha
- Enlaces funcionales que abren en nueva pestaña
- Estadísticas: total bookmarks, carpetas, archivos procesados

## Estructura de Base de Datos

### Tabla: bookmarks
- id (INTEGER PRIMARY KEY)
- title (TEXT)
- url (TEXT)
- folder (TEXT)
- date_added (TEXT)
- source_file (TEXT)
- created_at (DATETIME)

### Tabla: files
- id (INTEGER PRIMARY KEY)
- filename (TEXT)
- file_type (TEXT)
- processed_at (DATETIME)
- bookmarks_count (INTEGER)

## API Endpoints
- POST /api/upload - Subir archivos
- GET /api/bookmarks - Listar con filtros
- GET /api/search?q=texto - Búsqueda
- GET /api/folders - Listar carpetas
- GET /api/stats - Estadísticas