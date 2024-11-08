from random import randint, choice 
from config import app, db
from models import User, Dream, Birthday_thing, Color
import itertools
from flask import Flask, render_template, request, jsonify
import requests 
# from bs4 import BeautifulSoup 
import json
#  export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask db init
# flask db migrate -m 'Create tables'
# flask db upgrade
# python seed.py

main = User(username="gray_ghost", email="gray_ghost@example.com",password_hash= "kittenlove")
    # blanket 
    # food 
    # clothes 
    # towels 
    # glass_things 
    # cutlery 
    # drinks 
    # phone_accessories 
    # accessories 
    # candles ,
    # stationary ,
    # cosmetics_fragrances ,
    # toiletries ,
    # blind_bags ,
    # bags_backpacks ,
    # jewelry ,
c = Color(
    pic =  "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcStRi8ykIJl_CDyn508bW1KUu3pYh_bRtwtnFneipaXGIOwg8PpKdurF2f4W6zEX0lsSQy6dOZA7mQEY2Ewp5bMxF6SiUKDkQ ", 
    des =   "Whether you're curled up with your favorite book or watching your favorite series, do it in warmth and classic style with the Ribbed Plush Throw Blanket from Room Essentials™. This plush blanket features a ribbed design with a plush construction, bringing texture and a touch of timeless appeal to your decor. The ultra-soft fabric helps you stay warm and cozy, and the solid color pairs easily with your furniture and throw pillows. Simply throw this plush blanket over the back of a chair or sofa for convenient comfort whenever you need it ",
    price = "10.00",
    link = "https://www.target.com/p/ribbed-plush-throw-blanket-blush-room-essentials-8482/-/A-83773141?ref=tgt_adv_xsf&AFID=google&CPNG=Home%2BDecor&adgroup=67-10 "
)

    # things = d1, 
    # places = d2,
    # states_coutries = d3

d = Dream(
    pic =  "https://www.google.com/imgres?q=japan&imgurl=https%3A%2F%2Fcdn.britannica.com%2F95%2F1795-050-9EFCC4F0%2FJapan-map-features-locator.jpg&imgrefurl=https%3A%2F%2Fwww.britannica.com%2Fplace%2FJapan&docid=3Vy9319Q5zvZ6M&tbnid=iAskBt0cK-lb-M&vet=12ahUKEwjlt_jx3piJAxWGEzQIHWeyEoUQM3oECGcQAA..i&w=1600&h=1115&hcb=2&ved=2ahUKEwjlt_jx3piJAxWGEzQIHWeyEoUQM3oECGcQAA", 
    des =  "Japan is an island country in East Asia. It is located in the Pacific Ocean off the northeast coast of the Asian mainland, and is bordered on the west by the Sea of Japan and extends from the Sea of Okhotsk in the north to the East China Sea in the south.",
    price =  "10,000" ,
    link = "https://www.expedia.com/Destinations-In-Japan.d89.Flight-Destinations"
)


    # food = b1, 
    # drinks = b2,
    # beauty = b3,
    # clothing_stores = b4,
    # miscellaneous = b5,

bt = Birthday_thing(
    pic =  "https://store.crunchyroll.com/on/demandware.static/-/Sites-crunchyroll-master-catalog/default/dw7dd190f2/rightstuf/4535123716430_figure-monkey-d-luffy-gear-5-ver-portrait-of-pirates-one-piece-altd.jpg", 
    des =  "Celebrating its 20th anniversary, the P.O.P. series brings an all-new masterpiece to the “MAXIMUM” brand, revealing the new form of Luffy in the climax of the Wano Country arc - GEAR5!",
    price =  "228.64",
    link = "https://store.crunchyroll.com/products/monkey-d-luffy-gear-5-ver-portrait-of-pirates-one-piece-figure-4535123716430.html"
)


if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        db.session.query(User).delete()
        db.session.add_all([main, c, d, bt])
        db.session.commit()
        print("Deleting things...")