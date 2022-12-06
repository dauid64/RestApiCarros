from sql_alchemy import banco

class CarModelModel(banco.Model):
    __tablename__ = 'models'

    model_id = banco.Column(banco.Integer, primary_key=True)
    name = banco.Column(banco.String)
    cars = banco.relationship('CarModel', back_populates="model")

    def __init__(self, name):
        self.name = name

    @classmethod
    def find_by_name(cls, name):
        model = cls.query.filter_by(name=name).first()
        if model:
            return model
        else:
            return None

    @classmethod
    def find_by_id(cls, model_id):
        model = cls.query.filter_by(model_id=model_id).first()
        if model:
            return model
        return None

    def json(self):
        return {
            'model_id': self.model_id,
            'name': self.name
        }

    def save_model(self):
        banco.session.add(self)
        banco.session.commit()
