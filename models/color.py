from sql_alchemy import banco

class ColorModel(banco.Model):
    __tablename__ = 'colors'

    color_id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String)
    cars = banco.relationship('CarModel', back_populates="color")
    

    def __init__(self, name):
        self.name = name

    @classmethod
    def find_by_name(cls, name):
        color = cls.query.filter_by(name=name).first()
        if color:
            return color
        else:
            return None

    @classmethod
    def find_by_id(cls, color_id):
        color = cls.query.filter_by(color_id=color_id).first()
        if color:
            return color
        return None
    

    def json(self):
        return {
            'color_id': self.color_id,
            'name': self.name,
        }

    def save_color(self):
        banco.session.add(self)
        banco.session.commit()