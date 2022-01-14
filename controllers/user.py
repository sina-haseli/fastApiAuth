from fastapi.params import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm.session import Session

from models.database import get_db
from services.userService import UserService

route = APIRouter()


@route.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db), userService: UserService = Depends(UserService)):
    return UserService.find_one(userService, user_id, db)
