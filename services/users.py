from sqlalchemy.orm import Session

from models.user import User

def get_user_by_id(session: Session, id:int):
    try:
        user = session.query(User).filter(User.id == id).one()
    except:
        return None
    return user

def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    return user