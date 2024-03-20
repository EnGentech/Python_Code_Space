from main import User, engine, session

re_session = session(bind=engine)

# all_users = re_session.query(User).all()
#
# for user in all_users:
#     print(user.nickname)

gentle = re_session.query(User).filter(User.name == 'Gentle').all()
print(gentle)