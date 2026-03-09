from fastapi import FastAPI

from models.models import Product
from database import database_models
from database.db import session, engine

app = FastAPI()   # this is fastapi object after import

database_models.Base.metadata.create_all(engine)

def init_db():
    db = session()


init_db()

@app.get("/")
def greet():
    return "welcome to my app"


products = [

    #Product(1, "HP", "Budget Laptop", 40000, 1),   # object of Product entity
    #Product(2, "ACER", "Budget Laptop", 25000, 3)   # each object will refer to one product entity in your DB


    Product(id = 1, name = "Dell", description = "Dell Laptop", price = 50000, quantity = 50000),
    Product(id = 2, name = "acer", description= "acer laptop", price = 40000, quantity = 2),

]


@app.get("/products")    # this is for getting all the data
def get_all_products():
    return products

@app.get("/products/{id}")
def get_product_by_id(id:int):
    for p in products:
        if p.id == id:
            return p
    return "product not found"


@app.post("/products")
def add_product(product:Product):
    products.append(product)
    return product

@app.put("/products/{id}")
def update_product(id:int, product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated successfully"

    return "product not found"

@app.delete("/products/{id}")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted successfully"

    return "product not found"

