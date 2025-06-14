import fastapi
from routers import products, users, basic_auth_users, jwt_auth_user
from fastapi.staticfiles import StaticFiles #* -> Para importar objetos estaticos


app = fastapi.FastAPI(prefix="/root")  # * -> crea el objeto FastAPI

# * Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_user.router)

app.mount("/static", StaticFiles(directory="static"), name="static")#* Primero el path, luego el nombre del directorio y el nombre


@app.get("/")  # * -> Define la ruta raiz de la API
async def root():
    # --------> Es la funcion que se ejecuta al acceder a la raiz
    return fastapi.Response(status_code=200, content='Hola FastAPI')

# ? URL Local: http://127.0.0.1:8000/

# * async sirve para definir que el servidor no va a frenar por esperar la respuesta
# * de la funcion.


@app.get("/url")  # * --------> Define una ruta con un parametro
async def read_item():
    # * ----> Devuelve un diccionario al acceder a la ruta /url
    return {"url": "https://www.youtube.com"}

# ? URL Local: http://127.0.0.1:8000/url

#! Inicia Servidor: uvicorn main:app --reload

# ** Funciones Principales:
# * POST: Para crear datos
# * GET: Para leer datos
# * PUT: Para actualizar datos
# * DELETE: Para eliminar datos

# ** Funciones Exoticas:
# * OPTIONS: Para obtener los metodos que soporta la API
# * HEAD: Para obtener los headers de la respuesta
# * PATCH: Para actualizar parcialmente los datos
# * TRACE: Para obtener el camino que sigue la solicitud
