from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from sqlalchemy import ForeignKey, Text, String


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True) #the mapped_column is used to add extra attributes
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    email_address = mapped_column(String(255), nullable=False)
    comments: Mapped[list["Comment"]] = relationship(back_populates="user")

    """
    Lets define a string representation for our user and comment 
    """
    def __repr__(self):
        return "<User is {}".format(self.username)

class Comment(Base):
    __tablename__ = 'comments'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    user: Mapped["User"] = relationship(back_populates="comments")

    def __repr__(self):
        return "<Comment: {} was made by {}".format(self.text, self.user.username)
