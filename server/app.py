from flask import Flask, request, session
from flask_restful import Resource, Api
from models import db, User, Article  # make sure your models are correct
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'mysecret')
api = Api(app)

db.init_app(app)

# ------------------------
# Login Resource
# ------------------------
class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')

        if not username:
            return {'error': 'Username required'}, 400

        user = User.query.filter_by(username=username).first()
        if not user:
            return {'error': 'User not found'}, 404

        session['user_id'] = user.id
        return user.to_dict(), 200

# ------------------------
# Logout Resource
# ------------------------
class Logout(Resource):
    def delete(self):
        session.pop('user_id', None)
        return '', 204

# ------------------------
# Check Session Resource
# ------------------------
class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = db.session.get(User, user_id)  # modern SQLAlchemy
            return user.to_dict(), 200
        return {}, 401

# ------------------------
# Routes
# ------------------------
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CheckSession, '/check_session')

# ------------------------
# Optional: clear session (for testing)
# ------------------------
@app.route('/clear')
def clear_session():
    session.clear()
    return 'Session cleared', 200

# ------------------------
# Run the app
# ------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5555)
