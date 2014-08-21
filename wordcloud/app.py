import os, time, json, datetime 
from json import JSONEncoder, load
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, json, jsonify, send_file
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine, MetaData, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.expression import desc, asc
from sqlalchemy.dialects import postgresql
from varys.collection_db import Feed, Base, Site, Statistic 

# create application 
app = Flask(__name__)
app.config.from_object(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app


# sqlalchemy here:

databaselocation = "postgresql://muksit:@localhost/collection"
engine = create_engine(databaselocation)
Base.metadata.bind = engine 
FeedSession = sessionmaker(bind=engine)
session = FeedSession()






@app.route('/',)
def input():
    return render_template('index.html')


@app.route('/ask')
def idlookup():
	sitenumber = request.args.get('siteid')
	sitename = givesite(session, sitenumber)
 	sitecountry = givecountry(session, sitenumber)
 	sitelanguage = givelanguange(session, sitenumber)
 	returndata = {"sitename": sitename.encode('utf8'), "sitecountry": sitecountry.encode('utf8'), "sitelanguage": sitelanguage.encode('utf8')}
	return json.dumps(returndata)



#get json of values returned from database query
@app.route('/graph')
def getdata():
	sitenumber = request.args.get('siteid')
	sitejson = getstored(session, sitenumber)
	return sitejson

@app.route('/map')
def getmap():
	mapdata = getmapdata(session)
	return mapdata
  
@app.route('/map.json')
def returnjson():
	return send_file("static/map.json", mimetype = "application/json")
	
	

def getmapdata(session):
	last7 = session.query(Site.country, func.sum(Statistic.stored)).join(Feed) \
	.join(Statistic).filter(Site.id==Feed.site_id).filter \
	(Feed.feed_id==Statistic.feed_id).filter(Statistic.date > (datetime.date(2014, 02, 15)-datetime.timedelta(days=7))).group_by(Site.country) #change date to date.today()
	
	last7response = []	
	for array in last7:
		country = array[0]
		stored = array[1]
		last7response.append({"country": country, "articles":stored})


	averageweek = session.query(Site.country, func.sum(Statistic.stored)).join(Feed) \
	.join(Statistic).filter(Site.id==Feed.site_id).filter \
	(Feed.feed_id==Statistic.feed_id).filter(Statistic.date > (datetime.date(2014, 02, 15)-datetime.timedelta(days=182))) \
	.group_by(Site.country) #change date to date.today()
	
	averageweekresponse = []
	for array in averageweek:
		country = array[0]
		stored = array[1]
		averageweekresponse.append({"country": country, "articles": float(stored/7)})


	ratioarray = []
	for i in range(0, len(last7response)):
		country = last7response[i]["country"]
		try:
			storedratio = float(averageweekresponse[i]["articles"] / last7response[i]["articles"])
		except:
			storedratio = 0
		ratioarray.append({"country": country, "storedratio": storedratio})
		i += 1


	return jsonify(sentjson =ratioarray)

	
	
	# func.sum(Statistic.stored).label("sumstored")
	 #get array of results in format country, stored(sum of articles for last 7 days)
	# last180results = #get array of results in format country, stored(sum of articles for last 182 days)
	# average180results = #get array of results in format country, stored(sum of last 182/7)
	# trendscore180 = #get array of results in format country, ratio(sum of last 7/(sum of last 182/7))


#get array of stored values
def getstored(session, siteid):
	results = session.query(Statistic.stored, Statistic.date).join(Feed).filter(Feed.site_id ==siteid)
	response = []
	for array in results:
		articles = array[0]
		date = array[1].isoformat()
		response.append({"articles": articles, "date": date})	
	return json.dumps(response)
	


# querying sqlalchemy for sitename:
def givesite(session, siteid):
	s3 = session.query(Site.name).filter(Site.id == siteid)
	s4 = s3[0]
	return s4[0]



# country
def givecountry(session, siteid):
	c3 = session.query(Site.country).filter(Site.id ==siteid)
	c4 = c3[0]
	return c4[0]	



# language
def givelanguange(session, siteid):
	l3 = session.query(Feed.language).filter(Feed.site_id ==siteid)
	l4 = l3[0]
	return l4[0]







if __name__ == '__main__':
    app.run()