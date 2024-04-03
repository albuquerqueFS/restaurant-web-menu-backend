from sqlalchemy.orm import Session

from models.user import User

def get_users(session: Session):
    try:
        users = session.query(User).all()
    except:
        return []
    return users

def get_user_by_id(id:int, session: Session):
    try:
        user = session.query(User).filter(User.id == id).first()
    except:
        return None
    return user

def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    return user