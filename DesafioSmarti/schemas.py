from pydantic import BaseModel


class ContactBase(BaseModel):
    contactName: str
    phoneNumber: str | None = None
    email: str | None = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    pass

class Contact(ContactBase):
    id: int

    class Config:
        from_attributes = True