# Map My World API

Map My World es una aplicación backend diseñada para explorar y revisar diferentes ubicaciones y categorías del mundo,
como restaurantes, parques y museos. Esta API REST permite a los usuarios agregar nuevas ubicaciones y categorías, y
ofrece recomendaciones de combinaciones de ubicación y categoría que no han sido revisadas recientemente.

## Tecnologías Utilizadas

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn
- flake8

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/fhersho/map_my_world.git
cd map_my_world
```

2. Crea un entorno virtual y actívalo:

```bash
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Instala `flake8` para evaluar el código:

```bash
pip install flake8
```

## Ejecución

1. Inicia el servidor:

```bash
uvicorn app.main:app --reload
```

2. Accede a la documentación interactiva de la API en `http://localhost:8000/docs`.

## Evaluación del Código

Para evaluar el código con `flake8`, ejecuta el siguiente comando en el directorio raíz del proyecto:

```bash
flake8 .
```

## Endpoints

### Ubicaciones

- **Crear una nueva ubicación**

  `POST /locations/`

  **Cuerpo de la solicitud:**
  ```json
  {
    "latitude": 40.7128,
    "longitude": -74.0060
  }
  ```

- **Obtener una ubicación por ID**

  `GET /locations/{location_id}`

- **Listar todas las ubicaciones**

  `GET /locations/`

### Categorías

- **Crear una nueva categoría**

  `POST /categories/`

  **Cuerpo de la solicitud:**
  ```json
  {
    "name": "Restaurantes"
  }
  ```

- **Obtener una categoría por ID**

  `GET /categories/{category_id}`

- **Listar todas las categorías**

  `GET /categories/`

### Recomendaciones

- **Obtener recomendaciones de combinaciones de ubicación-categoría no revisadas recientemente**

  `GET /recommendations/`

## Manejo de Errores

- **400 Bad Request:** Solicitudes incorrectas o malformadas.
- **404 Not Found:** Recursos no encontrados.
- **500 Internal Server Error:** Errores inesperados en el servidor.

## Contribuir

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

```

Este `README.md` proporciona una descripción clara del proyecto, instrucciones para la instalación y ejecución, y detalles sobre los endpoints y el manejo de errores. Además, incluye instrucciones para instalar y utilizar `flake8` para evaluar el código.