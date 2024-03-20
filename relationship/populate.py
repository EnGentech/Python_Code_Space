from sqlalchemy.orm import sessionmaker
from main import User, Post, engine

session = sessionmaker()(bind=engine)

# #lets create a user
# new_user = User(name="Gentle", nickname="EnGentech")
#
# session.add(new_user)
# session.commit()

multiple_post = [
    {
        "title": "Learning in progress",
        "content": "learning programing has been a huge success"
    },
{
        "title": "Today is sunday",
        "content": "Behold its fathers day in the country"
    },
{
        "title": "KingMaker",
        "content": "Making kings is my job"
    },
{
        "title": "Money",
        "content": "What money cannot buy more money can buy"
    },
{
        "title": "Friendenemy",
        "content": "One enemy, many, 100 friends too small"
    },
]

# Query a user
posts = session.query(Post).filter(Post.id == 1).first()
#lets add the post unto the data base

print(posts.title)