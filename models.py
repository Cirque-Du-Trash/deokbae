from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MMR(db.Model):
    __tablename__ = 'mmrs'
    id = db.Column(db.BigInteger, primary_key=True)
    mmr = db.Column(db.Integer, default=0)
    
    def to_dict(self):
        return {
            'id': self.id,
            'mmr': self.mmr,
            'rank': MMR.query.filter(MMR.mmr > self.mmr).count() + 1
        }