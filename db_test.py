from sqlalchemy import Column, Integer, String, Numeric, Text, DateTime, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define the base class for the models
Base = declarative_base()


# Define the ProductPrice model
class ProductPrice(Base):
    __tablename__ = "amazon_product_prices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(255), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    url = Column(Text, nullable=False)
    last_checked = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ProductPrice(product_name='{self.product_name}', price={self.price}, url='{self.url}')>"


# Define the SQLAlchemy engine
DATABASE_URL = "postgresql://postgres:foobarbaz@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Query all product prices
product_prices = session.query(ProductPrice).all()
for product in product_prices:
    print(product)
