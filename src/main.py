from sqlalchemy.orm import Session

import crud, models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

db_account = crud.get_account(db=SessionLocal(), account_id=1)
print(db_account)
