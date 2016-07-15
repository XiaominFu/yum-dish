from flask import Flask, render_template, request, redirect, url_for
from bokeh.plotting import figure
from bokeh.embed import components
import requests
import simplejson

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET'])
def index():
  return render_template('index.html')

if __name__ == '__main__':
  #app.run(port=33507, debug=False)
  app.run(debug=False)