"""
all together iso_app
plus rest api
app translate in this version
"""

from flask import Flask
from flask_restful import Api, abort, Resource, reqparse
import json
from deep_translator import GoogleTranslator
import pycountry
import re


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument("iso", type=str, help= "Add iso value.", required=True)
parser.add_argument("countries", type=str, action='append', help="Without countries list there can't be any match.", required=True)


def dict_output(iso, match_count, matches):
    out = {}
    out['iso'] = iso
    out['match_count'] = match_count
    out['matches'] = matches
    return out


def iso_func(iso, countr):
    match_count = 0
    matches = []
    pattern = "[a-zA-Z]{3}"

    if not re.match(pattern, iso):
        print('Incorect iso there will be 0 matches')
        abort(400, message='ISO code in wrong format.')

    iso_country = pycountry.countries.get(alpha_3 = iso.upper())
    # print(type(iso_country))

    if iso_country == None:
        print('Non existing ISO code.')
        abort(400, message='Non existing ISO code')

    for c in countr:
        try:
            #print("Nazov {0} prelozeny nazov do en {1}".format(c, GoogleTranslator(source='auto', target='en').translate(c)))
            if GoogleTranslator(source='auto', target='en').translate(c).upper() == iso_country.name.upper():
                match_count += 1
                matches.append(c)
        except:
            continue

    return json.dumps(dict_output(iso, match_count, matches), indent=4, ensure_ascii=False)


class Iso_app(Resource):
    def post(self):
        args = parser.parse_args()
        output = iso_func(args['iso'], args['countries'])
        return output, 200


api.add_resource(Iso_app, "/iso")


if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
