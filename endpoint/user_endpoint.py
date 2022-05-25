from flask import request, jsonify


class UserEndpoint:

    def create_endpoints(app, services):
        user_service = services.user_service

        @app.errorhandler(400)
        def bad_request(error):
            response = jsonify({'message': error.description})
            response.status_code = 400
            return response

        @app.errorhandler(404)
        def page_not_found(error):
            return "INVALID_URL", 404

        @app.route("/user/sign-up", methods=['POST'])
        def sign_up():
            print("sign up start")
            new_user = request.json
            print("new user =",end=""), print(new_user)
            new_user = user_service.create_user(new_user)

            return jsonify({'message': 'SUCCESS'}, 200)
