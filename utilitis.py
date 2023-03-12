from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from model import Product

# ADD   
def create(product:Product, session:Session):
    session.add(product)
    session.commit()
    
# GET    
def read(session:Session): 
    result = session.query(Product)
    pulled_product = result.all() 
    return pulled_product
    # print(getted_product)
    # or 
    # stmt = select(Product)
    # getted_product = session.scalars(stmt).one()
    # print(getted_product)

# UPDATE   
def update(product:Product, session:Session):
    # product.height = 6
    # product.length = 6
    # product.width = 6
    # product.weight= 6
    session.commit()
    
# DELETE    
def delete(product:Product, session:Session):
    session.delete(product)
    session.commit()

    
    



    
    