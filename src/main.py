from sqlalchemy.orm import Session

import crud, models
import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_account = crud.get_account(get_db(), account_id=1)
print(db_account)
