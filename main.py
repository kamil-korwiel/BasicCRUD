from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from model import Base, Product
from utilitis import create, read, update ,delete


def main():
    
    engine = create_engine("sqlite+pysqlite:///example.db", echo=True)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        new_product = Product(name="Nine", 
                              fullname="Dobre Nine", 
                              manufacturer="Nine Nine", 
                              price=9, 
                              width=9,
                              height=9,
                              length=9,
                              weight=9)
        
        ##### CRUD #####
        # # CREATE
        # create(new_product,session)
        
        # # READ
        # list_of_products = read(session)
        # print("------------------------------")
        # [print(item) for item in list_of_products]
        # print("------------------------------")
        
        # # UPDATE
        # first_product = list_of_products[0]
        # first_product.length = 100
        # first_product.weight = 100
        # first_product.price = 100
        # update(first_product,session)
        
        # # DELETE
        # list_of_products = read(session)
        # delete(list_of_products[4],session)
        
        
        
        


if __name__ == "__main__":
    main()
