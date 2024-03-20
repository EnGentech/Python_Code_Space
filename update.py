from main import session, User, engine

up_session = session(bind=engine)

#first query for the name of object you need to update
update_username = up_session.query(User).filter(User.name == "Blessing").first()

update_username.name = "My_future"
#commit the update
up_session.commit()