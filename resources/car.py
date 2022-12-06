from flask_restful import Resource, reqparse
from models.car import CarModel
from models.person import PersonModel
from models.color import ColorModel
from models.model import CarModelModel

class Cars(Resource):
    def get(self):
        return {'car': [car.json() for car in CarModel.query.all()]}

class Car(Resource):

    args = reqparse.RequestParser()

    args.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank")
    args.add_argument('brand', type=str, required=True, help="The field 'brand' cannot be left blank")
    args.add_argument('color_id', type=int, required=True, help="The field 'color_id' cannot be left blank")
    args.add_argument('model_id', type=int, required=True, help="The field 'model_id' cannot be left blank")
    args.add_argument('owner_id', type=int, required=True, help="The field 'owner_id' cannot be left blank")

    def post(self):
        data = Car.args.parse_args()
        
        car = CarModel(**data)
        
        #VERIFICAÇÃO SE EXISTEM OS IDS CORRESPONDENTES
        if not PersonModel.find_by_id(data['owner_id']):
            return {'message': 'owner_id not already exist'}
        if not CarModelModel.find_by_id(data['model_id']):
            return {'message': 'model_id it is not valid'}
        if not ColorModel.find_by_id(data['color_id']):
            return {'message': 'color_id it is not valid'}

        #ENCONTRANDO QUANTOS CARROS TEM NO ID DO DONO CORRESPONDENTE
        carros_in_owner = CarModel.query.filter(CarModel.owner_id==data['owner_id']).count()
        
        #APLICANDO REGRA DE NEGOCIO
        if carros_in_owner > 2:
            return {'message': 'Voce nao pode adicionar mais de 3 carro no mesmo proprietario'}, 404
        if carros_in_owner == 0:
            person = PersonModel.query.filter(PersonModel.person_id==data['owner_id']).first()
            person.sale_opportunity = False
        try:
            car.save_car()
        except:
            return {'message': 'An internal error ocurred trying to create a new car.'}, 500
        
        return {'car': car.json()}, 200

