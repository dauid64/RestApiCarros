from sql_alchemy import banco

class PersonModel(banco.Model):
    __tablename__ = 'persons'

    person_id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String(45))
    sale_opportunity = banco.Column(banco.Boolean, default=True)
    car = banco.relationship('CarModel', back_populates='owner')

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'person_id': self.person_id,
            'name': self.name,
            'sale_opportunity': self.sale_opportunity,
            'car': [car.json() for car in self.car]
        }

    def save_person(self):
        banco.session.add(self)
        banco.session.commit()
    
    @classmethod
    def find_by_id(cls, person_id):
        person = cls.query.filter_by(person_id=person_id).first()
        if person:
            return person
        return None