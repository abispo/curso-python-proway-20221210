from datetime import date

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Date, ForeignKey, Text, Table, Column


from config import Base

# Aqui criamos a tabela associativa entre posts e tags. Quando a tabela associativa não possui colunas além das necessárias para fazer os relacionamentos, podemos utilizar o formato abaixo
posts_tags = Table(
    "posts_tags",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)

# Toda classe que deve ser mapeada para uma tabela, obrigatoriamente deve herdar da classe Base
class User(Base):

    # O atributo __tablename__ serve para indicar o nome que a tabela mapeada terá no banco de dados. Se não indicarmos o valor, o nome da tabela será o nome da classe
    __tablename__ = "users"

    # Abaixo definimos os atributos da classe, que serão mapeados para colunas na tabela. A principal diferença nesse caso da versão 1.* para 2.* do SQLAlchemy, é que na versão 2.* podemos utilizar o type hint de maneira mais eficiente.
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    # Abaixo criamos um atributo do tipo relationship. Esse atributo será preenchido com o objeto Profile que está relacionado ao objeto User. Sempre que a chamada 'user.profile' for executado, ele irá carregar esse objeto relacionado
    profile: Mapped["Profile"] = relationship(back_populates="user")

    # Alteramos o retorno do método __repr__, que é chamado quando o objeto é exibido pelo código
    def __repr__(self):
        return f"<User {self.email}>"


class Profile(Base):

    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    birth_date: Mapped[date] = mapped_column(Date, nullable=True)

    user: Mapped["User"] = relationship(back_populates="profile")

    def __repr__(self):
        return f"<Profile '{self.first_name} {self.last_name}'>"


class Post(Base):

    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)


class Tag(Base):

    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
