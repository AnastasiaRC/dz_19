from flask_restx import Resource, Namespace
from flask import request
from dz_19.dao.model.director import DirectorSchema
from dz_19.implemented import director_service
from dz_19.utils import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        data = request.json
        director_service.create(data)
        return "", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    def put(self, did):
        data = request.json
        if 'id' not in data:
            data['id'] = did
        director_service.update(data)
        return "", 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)
        return "", 204
