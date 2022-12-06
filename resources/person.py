from flask_restful import Resource, reqparse
from models.person import PersonModel

class Persons(Resource):
    def get(self):
        return {'person': [person.json() for person in PersonModel.query.all()]}, 200

class Person(Resource):

    args = reqparse.RequestParser()

    args.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank")

    def post(self):

        data = Person.args.parse_args()

        person = PersonModel(**data)

        try:
            person.save_person()
        except:
            return {'message': 'An internal error ocurred trying to create a new person.'}, 500
        
        return {'color': person.json()}, 200