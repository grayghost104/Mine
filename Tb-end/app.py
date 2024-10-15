from flask import request, session, jsonify, make_response, render_template
from flask_restful import Resource, Api
from config import app, db, api, mail
from models import User
from flask_mail import Message
from models import User, Dream, Birthday_thing, Wishlist, Color, Holiday_list, Birthday_list

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




# class SendEmail(Resource):
#     def post(self):
#         try:
#             data = request.get_json()
#             recipient_email = data.get('recipient_email')
#             user_email = data.get('user_email')
#             user_name = data.get('user_name')
#             subject = data.get('subject')
#             project_id = data.get('project_id')
#             sender_email = data.get('user_email')
#             company_name = data.get('company_name')
#             redirect_url = 'http://localhost:3000/'

#             html_body = f"""
#             <!DOCTYPE html>
#             <html>
#             <head>
#                 <style>
#                 body {{
#                     font-family: Arial, sans-serif;
#                     background-color: #f4f4f4;
#                     color: #333;
#                     margin: 0;
#                     padding: 0;
#                 }}
#                 .email-container {{
#                     width: 100%;
#                     max-width: 600px;
#                     margin: 0 auto;
#                     background-color: #ffffff;
#                     padding: 20px;
#                     border: 1px solid #ddd;
#                 }}
#                 .header {{
#                     background-color: #4caf50;
#                     color: #ffffff;
#                     padding: 10px;
#                     text-align: center;
#                 }}
#                 .content {{
#                     margin: 20px 0;
#                 }}
#                 .button {{
#                     display: inline-block;
#                     padding: 10px 20px;
#                     background-color: #4caf50;
#                     color: #ffffff;
#                     text-decoration: none;
#                     border-radius: 5px;
#                 }}
#                 .footer {{
#                     text-align: center;
#                     margin-top: 20px;
#                     font-size: 12px;
#                     color: #888;
#                 }}
#                 </style>
#             </head>
#             <body>
#                 <div class="email-container">
#                 <div class="header">
#                     <h1>Welcome to My Landscaper</h1>
#                 </div>
#                 <div class="content">
#                     <p>Hello {company_name},</p>
#                     <p>
#                     I hope this email finds you well. My name is {user_name}, and I would
#                     like to invite you to place a bid on my upcoming landscaping project
#                     through My Landscaper. I have outlined my project details and selected
#                     specific items that I would like to incorporate. You can view the full
#                     description of my project and the items chosen by visiting My
#                     Landscaper.
#                     </p>
#                     <p>To view and bid on my project, please use the following project code: {project_id}.</p>
#                     <p>I look forward to the possibility of working together and discussing my vision further.</p>
#                     <p>Best regards,</p>
#                     <p>{user_name}</p>
#                     <p>Click the button below to log into My Landscaper and view my project.</p>
#                     <a href="{redirect_url}" class="button">My Landscaper</a>
#                 </div>
#                 <div class="footer">
#                     <p>&copy; 2024 My Landscaper. All rights reserved.</p>
#                 </div>
#                 </div>
#             </body>
#             </html>
#             """


#             # Create the email message
#             msg = Message(subject, recipients=[recipient_email], sender=sender_email)
#             msg.html = html_body
#             msg.reply_to = user_email

#             mail.send(msg)
#             return {"message": "Email sent successfully!"}, 200
#         except Exception as e:
#             print(e)
#             return {"error": "Failed to send email."}, 500
        
# api.add_resource(SendEmail, '/send_email')

api.add_resource(One_User,'/user/<int:id>')
if __name__ == '__main__':
    app.run(port=5555, debug=True)