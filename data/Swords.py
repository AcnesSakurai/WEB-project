import sqlalchemy
from .db_session import SqlAlchemyBase


class Swords(SqlAlchemyBase):
    __tablename__ = 'Swords'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    linear = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    overturn = sqlalchemy.Column(sqlalchemy.String, nullable=True)