from random import randint, choice 
from config import app, db
from models import User, Dream, Birthday_thing, Wishlist, Color, Holiday_list, Birthday_list
import itertools
from flask import Flask, render_template, request, jsonify
import requests 
# from bs4 import BeautifulSoup 
import json


main = User(username="gray_ghost", email="gray_ghost@example.com",password_hash= "kittenlove")
c = Color(
    blanket = c1,
    food = c2,
    clothes = c3,
    towels = c4,
    glass_things = c5,
    cutlery = c6,
    drinks = c7,
    phone_accessories = c8,
    accessories = c9,
    candles = c10,
    stationary = c11,
    cosmetics_fragrances = c12,
    toiletries = c13,
    blind_bags = c14,
    bags_backpacks = c15,
    jewelry = c16,
)
c1 = json.dumps([])
c2 = json.dumps([])
c3 = json.dumps([])
c4 = json.dumps([])
c5 = json.dumps([])
c6 = json.dumps([])
c7 = json.dumps([])
c8 = json.dumps([])
c9 = json.dumps([])
c10 = json.dumps([])
c11 = json.dumps([])
c12 = json.dumps([])
c13 = json.dumps([])
c14 = json.dumps([])
c15 = json.dumps([])
c16 = json.dumps([])

d = Dream(
    things = d1, 
    places = d2,
    states_coutries = d3
)
d1 = json.dumps([])
d2 = json.dumps([])
d3 = json.dumps([])

bt = Birthday_thing(
    food = b1, 
    drinks = b2,
    beauty = b3,
    clothing_stores = b4,
    miscellaneous = b5,
)
b1 = json.dumps([])
b2 = json.dumps([])
b3 = json.dumps([])
b4 = json.dumps([])
b5 = json.dumps([])

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        db.session.query(User).delete()
        db.session.add_all([main])
        db.session.commit()
        print("Deleting Customers")