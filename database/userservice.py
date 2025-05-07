from database import get_db
from database.models import *

def add_user(username, phone_number):
    # первый способ генерации сессий (устаревший)
    db = next(get_db())
    # второй способ генерации сессий
    with next(get_db()) as db:
        user = db.query(User).filter_by(username=username).first()
        if not user:
            user = db.query(User).filter_by(phone_number=phone_number).first()
            # объединение 9 и 11 строчки через 1 запрос
            # user = db.query(User).filter(User.username == username and User.phone_number == phone_number).first()
            if not user:
                user = User(username=username, phone_number=phone_number)
                db.add(user)
                db.commit()
                db.refresh(user)
        return user.id




