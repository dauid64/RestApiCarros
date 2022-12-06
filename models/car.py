from sql_alchemy import banco

class CarModel(banco.Model):
    __tablename__ = 'cars'

    car_id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String)
    brand = banco.Column(banco.String)
    color_id = banco.Column(banco.Integer, banco.ForeignKey('colors.color_id'))
    model_id = banco.Column(banco.Integer, banco.ForeignKey('models.model_id'))
    owner_id = banco.Column(banco.Integer, banco.ForeignKey('persons.person_id'))
    color = banco.relationship('ColorModel', back_populates='cars')
    model = banco.relationship('CarModelModel', back_populates='cars')
    owner = banco.relationship('PersonModel', back_populates='car')

    def __init__(self, name, brand, color_id, model_id, owner_id):
        self.name = name
        self.brand = brand
        self.color_id = color_id
        self.model_id = model_id
        self.owner_id = owner_id

    def json(self):
        return {
            'car_id': self.car_id,
            'name': self.name,
            'brand': self.brand,
            'color': self.color.name,
            'model': self.model.name,
            'owner': self.owner.name
        }

    def save_car(self):
        banco.session.add(self)
        banco.session.commit()