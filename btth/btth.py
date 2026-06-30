from fastapi import FastAPI
from pydantic import BaseModel,Field
app = FastAPI()
products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000},
    {"id": 3, "name": "Screen", "price": 3633636}
]
class CreateProduct(BaseModel):
    id:int
    name:str =Field(min_length=2)
    price:float =Field(gt=0)
class UpdateProduct(BaseModel):
    name:str
    price:float
@app.get("/")
def get_root():
    return{
        "message":"Hú le"
    }   
# API lay toan bo san pham
@app.get('/products')
def get_products():
    return {
        "data":products
    }
# lay san pham theo id
@app.get("/product/{product_id}")
def get_product_by_id(product_id=int):
    for product in products:
        if product["id"]==product_id:
            return{
                "data":product
            }
    return{
        "message":"Khong tim thay san pham",
        "data":None
    }
#lay danh sach san pham theo khoang gia
@app.get("/product")
def get_product_by_price(start_price:float,end_price:float):
    find_product=[]
    for product in products:
        if start_price<=product["price"]<=  end_price:
            find_product.append(product)
    if find_product:
        return{
            "data":find_product
        }
    else:
        return{
            "message":"Khong tim thay",
            "data":None
        }
@app.post('/product')
def create_product(new_product:CreateProduct):
    products.append({
        "id":new_product.id,
        "name":new_product.name,
        "price":new_product.price
    })
    return{
        "message":"Them thanh cong",
        "data":new_product
    }
@app.put("/product")
def update_product(product_id:int,update_product=UpdateProduct):
    for product in products:
        if product["id"]==product_id:
            product["name"]==update_product.name
            product["price"]==update_product.price
            return{
                "message":"Cap nhat san pham thanh cong",
                "data":{
                    "id":product_id,
                    "name":update_product.name,
                    "price":update_product.price
                }
            }
    return{
        "message":"san pham khong ton tai",
        "data":None
    }
@app.delete("/product/{product_id}")
def delete_product(product_id:int):
    for product in products:
        if product["id"]==product_id:
            products.remove(product)
            return{
                "message":"Xoa thanh cong",
                "data":product
            }
    return{
        "message":"Khong ton tai",
        "data":None
    }