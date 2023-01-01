from sqlalchemy.orm import Session

from . import models

def get_account(db: Session, account_id: int):
    return db.query(models.Account).filter(models.Account.id == account_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.Account).filter(models.Account.email == email).first()
