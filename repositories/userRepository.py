from sqlalchemy.orm.session import Session

from models import dbmodels


class UserRepository:
    def findAll(self, user_id: int, db: Session):
        return db.query(dbmodels.User).filter(dbmodels.User.id == user_id).first()
