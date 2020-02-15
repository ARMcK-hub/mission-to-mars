'''
Houston Flask App
Author: Andrew McKinney
Creation Date: 2020-02-14
'''

# Import Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

### DEV TOOLS ###
dev_mode = True


# Flask App Setup
app = Flask(__name__)


# MongoDB Setup
mongo = PyMongo(app, uri="mongodb://localhost:27017/houston")



#################################################
# Flask Routes
#################################################



@app.route("/")
def index():
    from_ground_control = mongo.db.ground_control.find_one()
    gc_img_list = from_ground_control['mars_hem_dict']
    return render_template("earth.html", from_ground_control=from_ground_control, gc_img_list=gc_img_list)


@app.route("/scrape")
def scraper():
    ground_control = mongo.db.ground_control
    to_ground_control = mission_to_mars.houston()
    ground_control.update({}, to_ground_control, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    # if dev_mode:
    app.run(debug=True)
