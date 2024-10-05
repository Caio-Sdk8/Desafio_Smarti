from sqlalchemy import Column, Integer, String
from database.database import  Base

class Contact(Base):
    __tablename__ = "Contacts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    contactName = Column(String, nullable=False)
    phoneNumber = Column(String)
    email = Column(String)