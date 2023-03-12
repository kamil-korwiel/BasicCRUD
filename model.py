from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String

from typing import Optional
    
    
class Base(DeclarativeBase):
    pass 
    
class Product(Base):
    __tablename__ = "product_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    manufacturer: Mapped[str] = mapped_column(String(255))
    price: Mapped[int]
    weight: Mapped[float]
    width: Mapped[int]
    height: Mapped[int]
    length: Mapped[int]
    
    def __repr__(self) -> str:
         return "<Product(id='%d',name='%s', fullname='%s', price='%d', weight='%.2f',size= '%dx%dx%d')>" % (
            self.id,
            self.name,
            self.fullname,
            self.price,
            self.weight,
            self.length,
            self.width,
            self.height,
        )
