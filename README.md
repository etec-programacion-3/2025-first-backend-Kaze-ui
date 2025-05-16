# Sistema de Gestión de Biblioteca

## Descripción
Este proyecto es un sistema backend para la gestión de una biblioteca escolar. Permite realizar operaciones CRUD sobre libros, así como búsqueda, filtrado, ordenamiento y paginación.

## Endpoints

### Libros

#### Obtener todos los libros
- **GET** `/libros`

#### Crear un nuevo libro
- **POST** `/libros`

#### Actualizar un libro
- **PUT** `/libros/<id>`

#### Eliminar un libro
- **DELETE** `/libros/<id>`

#### Buscar libros
- **GET** `/libros/buscar`
  - Parámetros opcionales:
    - `titulo`: Buscar por título.
    - `categoria`: Filtrar por categoría.
    - `orden`: Ordenar por un campo (por defecto, `titulo`).
    - `pagina`: Número de página (por defecto, 1).
    - `tamano`: Tamaño de página (por defecto, 10).

## Requisitos
- Python 3.10+
- Flask
- SQLAlchemy

## Instalación
1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   python run.py
   ```

## Pruebas
Utiliza el archivo `requests.http` para probar los endpoints.
