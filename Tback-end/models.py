from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, metadata, bcrypt
from sqlalchemy.orm import relationship,validates 

#sign in with email, and then send an email to said email 
#one-many 
#many gets the id and relationship 
#one gets the relationship only 
class Color(db.Model, SerializerMixin): 
    __tablename__ = 'colors' 
    id = db.Column (db.Integer, primary_key=True) 
    blanket = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="colors")

class Dream(db.Model, SerializerMixin): 
    __tablename__ = 'dreams' 
    id = db.Column (db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="dreams")

class Birthday_thing(db.Model, SerializerMixin): 
    __tablename__ = 'birthday_things' 
    id = db.Column (db.Integer, primary_key=True) 
    user = db.relationship("User", back_populates="birthday_things")
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class Wishlist(db.Model, SerializerMixin): 
    __tablename__ = 'wishlists' 
    id = db.Column (db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    birthday_list_id = db.Column(db.Integer, db.ForeignKey('birthday_lists.id'))
    holiday_list_id = db.Column(db.Integer, db.ForeignKey('holiday_lists.id'))
    users = db.relationship("User", back_populates="wishlists",  cascade ="all")
    birthday_lists = db.relationship('Birthday_list', back_populates = 'wishlists', cascade ="all")
    holiday_lists = db.relationship('Holiday_list', back_populates= 'wishlistts', cascade ="all")

class Birthday_list(db.Model, SerializerMixin): 
    __tablename__ = 'birthday_lists' 
    id = db.Column (db.Integer, primary_key=True) 
    wishlists = db.relationship("Wishlist", back_populates="birthday_lists", cascade ="all, delete-orphan")


class Holiday_list(db.Model, SerializerMixin): 
    __tablename__ = 'holiday_lists' 
    id = db.Column (db.Integer, primary_key=True) 
    wishlists = db.relationship("wishlist", back_populates="holiday_lists", cascade ="all, delete-orphan")

class User(db.Model, SerializerMixin):
    __tablename__= 'users' 
    id=db.Column (db.Integer, primary_key=True)
    username= db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)
    colors = db.relationship("Color", back_populates="user")
    birthday = db.relationship("Birthday", back_populates="user")
    dreams = db.relationship("Dream", back_populates="user")
    wishlists = db.relationship("wishlist", back_populates="users", cascade ="all, delete-orphan")

    @hybrid_property
    def password_hash(self):
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash,password.encode('utf-8'))

    # @validates('password')
    # def check_pass(self,key,value):
    #     if 0>=value>=8:
    #         return value
    #     else:
    #         raise ValueError("Make your password longer")




    