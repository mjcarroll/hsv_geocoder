from project import db

class Location(db.Model):
    __tablename__ = "location"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    search_street = db.Column(db.String, unique=True, nullable=False)

    valid_address = db.Column(db.Boolean)
    full_address = db.Column(db.String)
    country = db.Column(db.String)
    postal_code = db.Column(db.Integer)
    locality = db.Column(db.String)
    street = db.Column(db.String)
    number = db.Column(db.Integer)

    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    raw = db.Column(db.String)

    def __init__(self, search_street):
        self.search_street = search_street

    def __repr__(self):
        return '<Location {0}>'.format(self.search_street)