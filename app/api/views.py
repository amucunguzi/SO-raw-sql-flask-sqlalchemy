from flask import jsonify
from ..db import db
from . import api

from .some_service import SomeService

service = SomeService(db)


@api.route('/test', methods=('GET', ))
def entry():
    results = service.get_some_db_data()
    return jsonify({'key': 'some value', 'results': results}), 200
