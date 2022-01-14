from sqlalchemy.orm.session import Session

from repositories.userRepository import UserRepository


class UserService:
    def __init__(self):
        self.UserRep = UserRepository()
        super(UserRepository).__init__()

    def find_one(self, user_id: int, db: Session):
        return self.UserRep.findAll(user_id, db)
