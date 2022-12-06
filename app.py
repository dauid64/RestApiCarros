from flask import Flask
from flask_restful import Api
from resources.color import Colors, Color, ColorModel
from resources.model import Models, Model, CarModelModel
from resources.person import Persons, Person
from resources.car import Cars, Car

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()
    #Resolução para criar as cores e modelos padrões
    if not ColorModel.query.all():
        banco.session.add(ColorModel("Yellow"))
        banco.session.add(ColorModel("Blue"))
        banco.session.add(ColorModel("Gray"))
        banco.session.commit()
    if not CarModelModel.query.all():
        banco.session.add(CarModelModel("hatch"))
        banco.session.add(CarModelModel("sedan"))
        banco.session.add(CarModelModel("convertible"))
        banco.session.commit()
    
api.add_resource(Colors, '/colors')
api.add_resource(Color, '/color')
api.add_resource(Models, '/models')
api.add_resource(Model, '/model')
api.add_resource(Persons, '/persons')
api.add_resource(Person, '/person')
api.add_resource(Cars, '/cars')
api.add_resource(Car, '/car')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=5000)