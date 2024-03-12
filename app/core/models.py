from sqlalchemy import ARRAY, Column, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class UserFilmRoleAssociation(Base):
    __tablename__ = 'user_film_association'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    film_id = Column(Integer, ForeignKey('films.id'))
    role = Column(String(length=10))


class UserCompanyRoleAssociation(Base):
    __tablename__ = 'user_company_association'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))
    role = Column(String(length=10), nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(length=50))
    last_name = Column(String(length=50))
    email = Column(String(length=50))
    minimum_fee = Column(Integer)
    films = relationship("Film", secondary='user_film_association', back_populates="users")
    companies = relationship("Company", secondary="user_company_association",
                             back_populates="users")


class Film(Base):
    __tablename__ = 'films'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=100))
    description = Column(Text)
    budget = Column(Integer)
    release_year = Column(Integer)
    genres = Column(ARRAY(String))
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Company", back_populates="films")


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=100))
    contact_email_address = Column(String(length=50))
    phone_number = Column(String(length=15))
    films = relationship("Film", back_populates="company")

    users = relationship(
        "User", secondary="user_company_association",
        back_populates="companies"
    )
