from flask import Flask, render_template, redirect, request
from flask_pymongo import PyMongo
import predict_gender

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/gender")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)


# Route that will trigger the scrape function
@app.route("/predict")
def predict():

    # Run the scrape function
    gender = predict_gender.

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)