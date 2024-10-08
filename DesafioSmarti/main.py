from fastapi import Depends, FastAPI, HTTPException
from httpx import delete
from sqlalchemy.orm import Session
from schemas import Contact, ContactCreate, ContactUpdate
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
    try:
        db_contact = contact_repo.get_contact_by_name(name=contact.contactName)
        if db_contact:
            raise HTTPException(status_code=400, detail="Name already registered")
        return contact_repo.create_contact(contact=contact)
    except Exception as e:
        return e

@app.get("/Contacts/", response_model=list[Contact])
def get_contacts(contact_repo: IContactRepository = Depends(get_contact_repository)):
    try:
        contacts = contact_repo.get_contacts()
        return contacts
    except Exception as e:
        return e

@app.get("/Contacts/{name}", response_model=Contact)
def get_contact_by_name(name: str, contact_repo: IContactRepository = Depends(get_contact_repository)):
    try:
        contact = contact_repo.get_contact_by_name(name)
        return contact
    except Exception as e:
        return e

@app.put("/Contacts/{id}", response_model=ContactUpdate)
def update_contact(id: int, contact: ContactUpdate, contact_repo: IContactRepository = Depends(get_contact_repository)):
    print(contact)
    try:
        contact = contact_repo.update_contact(id, contact)
        return contact
    except Exception as e:
        return e

@app.delete("/Contacts/{id}", response_model={})
def delete_contact(id: int, contact_repo: IContactRepository = Depends(get_contact_repository)):
    try:
        contact_repo.delete_contact(id)
        return {"message":"User deleted"}
    except Exception as e:
        return e


