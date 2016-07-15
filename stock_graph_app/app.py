from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components
import requests
import simplejson

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index',methods=['GET','POST'])
def index():
  if request.method == 'GET':
      return render_template('index.html')
  else:
      #request was a POST
      app.vars['stock'] = request.form['stock_label']
      return redirect('/stock_graph')

@app.route('/stock_graph',methods=['GET'])
def graph():
  stock = app.vars['stock']
  api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
  session = requests.Session()
  session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
  raw_data = session.get(api_url)
  company_name = raw_data.json()['name']

  plot = figure(#tools=TOOLS,
                title='Data from Quandle WIKI set for %s' % company_name,
                x_axis_label='date',
                x_axis_type='datetime')
  script, div = components(plot)	
  return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
  #app.run(port=33507, debug=False)
  app.run(debug=True)