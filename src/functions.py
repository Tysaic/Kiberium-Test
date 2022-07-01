from sqlalchemy.orm import Session

from models import Patent

def patent_by_id(db: Session, patent_id: int):
    return db.query(Patent).filter(Patent.id == patent_id).first().number

def patent_by_number(db: Session, patent_number: str):
    return db.query(Patent).filter(Patent.number == patent_number).first().id
