from flask_restx import Resource, Namespace
from flask import request
from dz_19.dao.model.genre import GenreSchema
from dz_19.implemented import genre_service
from dz_19.utils import auth_required


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        data = request.json
        genre_service.create(data)
        return "", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        r = genre_service.get_one(gid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    def put(self, gid):
        data = request.json
        if 'id' not in data:
            data['id'] = gid
        genre_service.update(data)
        return "", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204

