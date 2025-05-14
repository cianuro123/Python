from fastapi import APIRouter

router = APIRouter(prefix="/product", 
                   tags=["Products"],
                   responses={404:{"message":"No encontrado"}})

list_products = ["Producto 0","Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]
@router.get("/all")
def products():
    return list_products

@router.get("/{id}")
def products(id:int):
    return list_products[id]

@router.get("/")
def products(id:int):
    return list_products[id]
    