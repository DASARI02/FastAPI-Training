from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from typing import List


DATABASE_URL = "sqlite:///./test.db"

Base = declarative_base()
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class ProductInDB(Base):
    __tablename__ = "products"

    productid = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

Base.metadata.create_all(bind=engine)


app = FastAPI()


class Product(BaseModel):
    productid: int
    name: str
    price: float

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def add_product(db: Session, product: Product):
    db_product = ProductInDB(productid=product.productid, name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def get_all_products(db: Session):
    return db.query(ProductInDB).all()

def update_product(db: Session, product: Product):
    db_product = db.query(ProductInDB).filter(ProductInDB.productid == product.productid).first()
    if db_product:
        db_product.name = product.name
        db_product.price = product.price
        db.commit()
        db.refresh(db_product)
        return db_product
    return None

def apply_discount(db: Session, discount_percentage: float):
    products = db.query(ProductInDB).all()
    for product in products:
        product.price -= product.price * (discount_percentage / 100)
    db.commit()
    return products


@app.post("/addProduct", status_code=status.HTTP_201_CREATED)
async def add_product_endpoint(product: Product, db: Session = Depends(get_db)):
    db_product = add_product(db, product)
    return db_product

@app.put("/updateProduct")
async def update_product_endpoint(product: Product, db: Session = Depends(get_db)):
    db_product = update_product(db, product)
    if db_product:
        return db_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.get("/viewall", response_model=List[Product])
async def view_all(db: Session = Depends(get_db)):
    return get_all_products(db)

@app.put("/applyDiscount")
async def apply_discount_endpoint(discount_percentage: float, db: Session = Depends(get_db)):
    updated_products = apply_discount(db, discount_percentage)
    return updated_products
