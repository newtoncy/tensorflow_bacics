import sqlalchemy as sa
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine('mysql+pymysql://newtoncy:A123456a@localhost:3306/learn_sqlalchemy')

Base = declarative_base()


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20), unique=True)
    articles = relationship('Article', secondary='article_tag')


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    url = Column(String(255))
    author_id = Column(Integer, ForeignKey('author.id', ondelete='set null'))
    author = relationship('Author', backref=backref('articles'))
    tags = relationship('Tag', secondary='article_tag')


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=25))
    comment = Column(String(length=50))


class ArticleTag(Base):
    __tablename__ = 'article_tag'
    article_id = Column(Integer, ForeignKey('article.id', ondelete='cascade'), primary_key=True)
    tag_id = Column(Integer, ForeignKey('tag.id', ondelete='cascade'), primary_key=True)


session = sessionmaker(conn)
sess = session()

Base.metadata.create_all(conn)

gx = Tag(name='搞笑')
jy = Tag(name='教育')
ys = Tag(name='严肃')
article1 = Article(title='论教育的搞笑性')
article2 = Article(title='论教育的严肃性')
article1.tags.append(gx)
article1.tags.append(jy)
article2.tags.append(jy)
article2.tags.append(ys)
newtoncy = Author(name='newtoncy')
article1.author = newtoncy
article2.author = newtoncy

sess.add_all([gx, jy, ys, article1, article2])
sess.commit()
pass
