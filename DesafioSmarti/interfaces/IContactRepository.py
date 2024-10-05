from abc import ABC, abstractmethod
from schemas import ContactCreate, ContactUpdate
from domains.models import Contact


class IContactRepository(ABC):

    @abstractmethod
    def get_contacts(self, skip: int = 0, limit: int = 100):
        pass

    @abstractmethod
    def get_contact_by_id(self, id: int) -> Contact:
        pass

    @abstractmethod
    def get_contact_by_name(self, name: str) -> Contact:
        pass

    @abstractmethod
    def create_contact(self, contact: ContactCreate) -> Contact:
        pass

    @abstractmethod
    def delete_contact(self, id: int) -> None:
        pass

    @abstractmethod
    def update_contact(self, id: int, contact: ContactUpdate) -> Contact:
        pass