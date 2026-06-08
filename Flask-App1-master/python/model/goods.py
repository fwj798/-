from python.extensions import db

class Goods(db.Model):
    __tablename__ = 'goods'
    a = db.Column(db.Integer, primary_key=True)
    b = db.Column(db.Integer)
    c = db.Column(db.Integer)
