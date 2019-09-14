from flask import Flask,render_template,redirect,request,url_for
from attraction_list import filter_region,filtering,filtered_name
from models.db import db

app=Flask(__name__)
@app.route("/")
def home_1():
    return render_template("home.html")
@app.route("/",methods=['POST'])
def home():
    region1=request.form['radio']

    data1=filter_region(region1)
    
    return redirect('/filter_output/{0}'.format(region1))



@app.route('/filter_output/<place>')
def filtering2(place):
    data1=filter_region(place)
    # data1 = request.args['data1']
    # data1= session['data1']
    return render_template('screen3.html',data=data1)
@app.route('/details/<places>')
def details(places):

    data1=filtered_name(places)
    data2=data1[0]

    return render_template('screen4.html',data=data2)
@app.route('/iframe/<places>')
def iframe_detail(places):
    data1=filtered_name(places)
    data2=data1[0]
    return render_template('smallscreen4.html',data=data2)



@app.route('/filter_output',methods=['POST'])
def filtering1():
    season = request.form.get('Season')
    region = request.form.get('Region')
    geography = request.form.get('Geography')
    data = filtering(season, region, geography)
    return redirect(url_for('/filter_output//{0}/{1}/{2}'.format(season,region,geography)))
    
   

if __name__=="__main__":
    app.run(debug=True)