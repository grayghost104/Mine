from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy
from config import db, metadata, bcrypt
from sqlalchemy.orm import relationship,validates 

#sign in with email, and then send an email to said email 
#one-many 
#many gets the id and relationship 
#one gets the relationship only 

# blanket food  clothes  towels  glass_things  cutlery  drinks  phone_accessories  accessories  candles  stationary  cosmetics_fragrances  toiletries  blind_bags  bags_backpacks   jewelry 


class Color(db.Model, SerializerMixin): 
    __tablename__ = 'colors' 
    id = db.Column (db.Integer, primary_key=True) 
    pic = db.Column(db.String)
    des = db.Column(db.String)
    price = db.Column(db.String)
    link = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="colors")      

# things  places  states_coutries 

class Dream(db.Model, SerializerMixin): 
    __tablename__ = 'dreams' 
    id = db.Column (db.Integer, primary_key=True) 
    pic = db.Column(db.String)
    des = db.Column(db.String)
    price = db.Column(db.String)
    link = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="dreams")


#  foods  drinks  beauty  clothing_stores  miscellaneous 
class Birthday_thing(db.Model, SerializerMixin): 
    __tablename__ = 'birthday_things' 
    id = db.Column (db.Integer, primary_key=True) 
    pic = db.Column(db.String)
    des = db.Column(db.String)
    price = db.Column(db.String)
    link = db.Column(db.String)
    user = db.relationship("User", back_populates="birthday_things")
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class Photo(db.Model, SerializerMixin): 
    __tablename__ = 'photos' 
    id = db.Column (db.Integer, primary_key=True)
    pic = db.Column(db.String)
    people = db.Column(db.String)
    place = db.Column(db.String)
    date = db.Column(db.String)
    story = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="photos") 


class Tv_showF(db.Model, SerializerMixin): 
    __tablename__ = 'tv_showFs' 
    id = db.Column (db.Integer, primary_key=True)
    watched = db.Column(db.String)
    rating = db.Column(db.String)
    feeling = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="tv_showFs")

class Tv_showFav(db.Model, SerializerMixin): 
    __tablename__ = 'tv_showFavs' 
    id = db.Column (db.Integer, primary_key=True)
    rating = db.Column(db.String)
    feeling = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="tv_showFavs")


class Tv_showC(db.Model, SerializerMixin): 
    __tablename__ = 'tv_showCs' 
    id = db.Column (db.Integer, primary_key=True)
    watching = db.Column(db.String)
    rating = db.Column(db.String)
    feeling = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="tv_showCs")


class Movie(db.Model, SerializerMixin): 
    __tablename__ = 'movies' 
    id = db.Column (db.Integer, primary_key=True)
    watched = db.Column(db.String)
    rating = db.Column(db.String)
    feeling = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    user = db.relationship("User", back_populates="movies")

class User(db.Model, SerializerMixin):
    __tablename__= 'users' 
    id=db.Column (db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    username= db.Column(db.String, nullable=False, unique=True)
    _password_hash = db.Column(db.String)

    colors = db.relationship("Color", back_populates="user")
    birthday_things = db.relationship("Birthday_thing", back_populates="user")
    dreams = db.relationship("Dream", back_populates="user")
    photos = db.relationship("Photo", back_populates="user")
    tv_showFs = db.relationship("Tv_showF", back_populates="user")
    tv_showCs = db.relationship("Tv_showC", back_populates="user")
    tv_showFavs = db.relationship("Tv_showFav", back_populates="user")
    movies = db.relationship("Movie", back_populates="user")
    
    # wishlists = db.relationship("wishlist", back_populates="users", cascade ="all, delete-orphan")
    
    
    @validates('email')
    def validate_image(self, key, email):
        if "@" in email:
            return email
        else:
            raise ValueError('invalid email')

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


# class Wishlist(db.Model, SerializerMixin): 
#     __tablename__ = 'wishlists' 
#     id = db.Column (db.Integer, primary_key=True) 

#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
#     users = db.relationship("User", back_populates="wishlists",  cascade ="all")

#     birthday_list_id = db.Column(db.Integer, db.ForeignKey('birthday_lists.id'))
#     birthday_lists = db.relationship('Birthday_list', back_populates = 'wishlists', cascade ="all")

#     holiday_list_id = db.Column(db.Integer, db.ForeignKey('holiday_lists.id'))
#     holiday_lists = db.relationship('Holiday_list', back_populates= 'wishlistts', cascade ="all")

# class Birthday_list(db.Model, SerializerMixin): 
#     __tablename__ = 'birthday_lists' 
#     id = db.Column (db.Integer, primary_key=True)
#     wishlists = db.relationship("Wishlist", back_populates="birthday_lists", cascade ="all, delete-orphan")


# class Holiday_list(db.Model, SerializerMixin): 
#     __tablename__ = 'holiday_lists' 
#     id = db.Column (db.Integer, primary_key=True) 
#     wishlists = db.relationship("wishlist", back_populates="holiday_lists", cascade ="all, delete-orphan")


    