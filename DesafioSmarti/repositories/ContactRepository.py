from sqlalchemy.orm import Session
from typing import List
from email_validator import validate_email, EmailNotValidError
from domains.models import Contact
from schemas import ContactCreate, ContactUpdate
from interfaces.IContactRepository import IContactRepository

class ContactRepository(IContactRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_contact_by_id(self, id: int):
        return self.db.query(Contact).filter(Contact.id == id).first()

    def get_contact_by_name(self, name: str):
        return self.db.query(Contact).filter(Contact.contactName == name).first()

    def create_contact(self, contact: ContactCreate):
        try:
            valid =  validate_email(contact.email)
            contact.email = valid.normalized
        except EmailNotValidError as e:
            return e
        db_contact = Contact(contactName=contact.contactName, phoneNumber=contact.phoneNumber, email=contact.email)
        self.db.add(db_contact)
        self.db.commit()
        self.db.refresh(db_contact)
        return db_contact

    def delete_contact(self, id: int):
        contact = self.db.query(Contact).filter(Contact.id == id).first()
        if contact:
            self.db.delete(contact)
            self.db.commit()

    def get_contacts(self, skip: int = 0, limit: int = 100):
        return self.db.query(Contact).offset(skip).limit(limit).all()

    def update_contact(self, id: int, contact: ContactUpdate):
        db_contact = self.get_contact_by_id(id)
        if db_contact:
            db_contact.contactName = contact.contactName or db_contact.contactName
            db_contact.phoneNumber = contact.phoneNumber or db_contact.phoneNumber
            db_contact.email = contact.email or db_contact.email
            self.db.commit()
            self.db.refresh(db_contact)
        return db_contact