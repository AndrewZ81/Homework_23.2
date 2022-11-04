from flask import jsonify
from flask import request
from flask_restx import Resource, Namespace

queries_ns = Namespace("perform_query")


@queries_ns.route("/")
class QueriesView(Resource):
    def post(self):
        post_data = request.json
        response = jsonify(post_data)
        response.status_code = 201
        return response
