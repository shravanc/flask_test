from flask import request, jsonify, render_template, url_for, request, redirect
from textblob import TextBlob

#import app.helpers.user_service as us

def index():
  if request.method == "POST":
    review = request.form['comment']

    ## DHANUSH has to code here
    tb = TextBlob(review)
    language = tb.detect_language()
    # here check if languag is not kannada render a different template
    # template loacation is app/views/users/error.html
    # in error template a link to go back to home page




    ##


    results = {"sentiment": "Nakkan", "Review": "Naanavanalla"}
    return render_template('show.html', result=result)

  return render_template('index.html')


def respond():
  fdata = request.form 
  return render_template('respond.html')
