from flask_restful import Resource, reqparse
from models.color import ColorModel

class Colors(Resource):
    def get(self):
        return {'colors': [color.json() for color in ColorModel.query.all()]}, 200
    
class Color(Resource):

    args = reqparse.RequestParser()

    args.add_argument('name', type=str, required=True, help="The field 'name' cannot be left blank")

    def post(self):
        data = Color.args.parse_args()

        color_exist = ColorModel.find_by_name(data['name'])

        if color_exist:
            return {'message': f'Color {data["name"]} already exist'}, 400
        
        color = ColorModel(**data)

        try:
            color.save_color()
        except:
            return {'message': 'An internal error ocurred trying to create a new color.'}, 500
        
        return {'color': color.json()}, 200



