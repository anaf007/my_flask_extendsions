from my_flask_extendsions.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Article(SurrogatePK, Model):
    __tablename__ = 'articles'

    title = Column(db.String(80), unique=True, nullable=False)
    rendered_text = Column(db.String(80))
    author_name = Column(db.String(80))
    url = Column(db.String(80))
    last_update = Column(db.String(80))
    published = Column(db.String(80))

    pub_date = Column(db.DateTime, nullable=False, default=dt.datetime.now)