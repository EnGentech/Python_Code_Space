from main import User, Post
from populate import session

user_to_delete = session.query(User).filter(user.id == 1).first()

posts=session.query(Post).all()

session.delete(user_to_delete)
session.commit()
#doing the above will delete post made from the user defined