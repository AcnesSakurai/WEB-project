import sqlalchemy
from .db_session import SqlAlchemyBase


class Pentacles(SqlAlchemyBase):
    __tablename__ = 'Pentacles'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    linear = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    overturn = sqlalchemy.Column(sqlalchemy.String, nullable=True)