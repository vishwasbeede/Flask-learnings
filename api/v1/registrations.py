from flask import request
from ..models import db, Registration
from ..decorators import json, collection, etag
from . import api
import logging

@api.route('/registrations/', methods=['POST'])
@json
def new_registration():
    # reg = Registration().import_data(request.get_json(force=True))
    # db.session.add(reg)
    # db.session.commit()
    # return {}, 201, {'Location': reg.get_url()}
    # return {"Hello":200}
    # x= logging.HTTPHandler("kjaksfh")
    logger.error('An exception occurred at %s', 'hello_world')
    return 'sdf'
    