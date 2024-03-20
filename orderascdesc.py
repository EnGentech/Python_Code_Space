from main import User, engine, session
from sqlalchemy import desc

order_session = session(bind=engine)

query_desc_order = order_session.query(User).order_by(desc(User.name)).all()

for order in query_desc_order:
    print(order.name, order.nickname)