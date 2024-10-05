from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from schemas import Contact, ContactCreate
from domains import models
from interfaces.IContactRepository import IContactRepository
from repositories.ContactRepository import ContactRepository
from database.database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

# Função para injeção de dependência do repositório
def get_contact_repository(db: Session = Depends(get_db)) -> IContactRepository:
    return ContactRepository(db)  # Deve instanciar corretamente

@app.post("/Contacts/", response_model=Contact)
def create_contact(contact: ContactCreate, contact_repo: IContactRepository = Depends(get_contact_repository)):
    db_contact = contact_repo.get_contact_by_name(name=contact.contactName)
    if db_contact:
        raise HTTPException(status_code=400, detail="Email already registered")
    return contact_repo.create_contact(contact=contact)

@app.get("/Contacts/", response_model=list[Contact])
def get_contacts(contact_repo: IContactRepository = Depends(get_contact_repository)):
    contacts = contact_repo.get_contacts()
    return contacts
