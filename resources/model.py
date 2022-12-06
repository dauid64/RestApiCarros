from flask_restful import Resource, reqparse
from models.model import CarModelModel

class Models(Resource):
    def get(self):
        return {'Models': [model.json() for model in CarModelModel.query.all()]}, 200

class Model(Resource):

    args = reqparse.RequestParser()

    args.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank")

    def post(self):

        data = Model.args.parse_args()

        model_exist = CarModelModel.find_by_name(data['name'])

        if model_exist:
            return {'message': f'Model {data["name"]} already exist'}, 400
        
        model = CarModelModel(**data)

        try:
            model.save_model()
        except:
            return {'message': 'An internal error ocurred trying to create a new model.'}, 500
        
        return {'color': model.json()}, 200
