from flask import request, session, jsonify, make_response, render_template
from flask_restful import Resource, Api
from config import app, db, api
from models import User, Monster, Buy, Media, Story

class LogOUT(Resource):
    def delete(self):
        session['user_id'] = None
        return {}

api.add_resource(LogOUT,'/logout')

class SaveSe(Resource):

    def get(self):
        print(session)
        return {}

    def post(self):
        print(session)
        data = request.get_json()
        session['data'] = data['data']
        print(data)
        return {}

api.add_resource(SaveSe,'/session')


class CSession(Resource):
    def get(self):
        if session.get('user_id'):
            user = User.query.filter(User.id == session.get('user_id')).first()
            return user.to_dict()
        else:
            return {}, 404
api.add_resource(CSession,'/checksessions')

class LoginIN(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter(User.username == data['username']).first()
        if (user and user.authenticate(data['password'])):
            session['stay_logged_in'] = data.get('stayLoggIn', False)
            session['user_id'] = user.id
            print(session)
            return jsonify(user.to_dict())
        return make_response({'error':'Invalid username or password'}, 401)

api.add_resource(LoginIN, '/login')

class All_User(Resource):

    def get(self):
        au = User.query.all()
        return [us.to_dict(rules=('-sbus', '-smeds','-smons')) for us in au],200

    def post(self):
        try:
            data = request.get_json()
            new_user = User(
                username = data['username'],
                password_hash = data['password'],
                fav_mon = data['fav_mon'], 
                fav_mov = data['fav_mov']
            )
            db.session.add(new_user)
            db.session.commit()
            return new_user.to_dict(),201
        except Exception as e:
            return make_response({'errors': str(e)},404)
api.add_resource(All_User,'/user')

class One_User(Resource):
    def get(self, id):
        act = User.query.filter(User.id == id).first()
        if (act):
            return act.to_dict(rules=('-sbus', '-smeds','-smons')),200
        else:
            return make_response({'error':'This user does not exist'},400)
    def patch(self, id):
        one = User.query.filter(User.id == id).first()
        if (one):
            try:
                data = request.get_json()
                for key in data:
                    setattr(one,key,data[key])
                db.session.add(one)
                db.session.commit()
                return one.to_dict(rules=('-sbus', '-smeds','-smons')),202
            except Exception as e:
                return make_response({"error": str(e)},404) 
        else:
            return make_response('This user does not exist',404)
    def delete(self, id):
        one = User.query.filter(User.id == id).first()
        if (one):
            db.session.delete(one)
            db.session.commit()
            return {}, 204
        else:
            return make_response({
                'error': 'Could not find user'
            },404)

api.add_resource(One_User,'/user/<int:id>')
