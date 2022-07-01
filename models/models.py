from sqlalchemy import Column, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import String, Integer

Base = declarative_base()

class Patent(Base):

    __tablename__ = "patent"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    number = Column(String(7))

    def __str__(self):
        return self.number


if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://kiberium:root1234@localhost/kiberium_db", echo=True)
    Base.metadata.create_all(engine)
    print("Database Created")
