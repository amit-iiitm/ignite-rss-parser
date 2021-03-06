from flask import Flask, json, request, render_template
import feedparser

app=Flask(__name__)

@app.route('/')
def rss_link():
	return render_template("index.html")


@app.route('/rss_feed',methods=["GET","POST"])
def render_rss():
	if request.method=="POST":
		rss_url=request.form['url']
	
	#use feedparser module to parse the incoming url
	data=feedparser.parse(rss_url)
	print rss_url
	#list to store the info of all feeds
	rss_feed_list=[]
	#'entries' key stores all the articles
	for entry in data['entries']:
		#iterate through all articles
		print entry
		try:
			#extract useful info
			title=str(entry['title'])
			link=str(entry['link'])
			summary=str(entry['summary'])
			published=str(entry['published'])
			image=""
			if 'media_content' in entry.keys():
				image=str(entry['media_content'][0]['url'])
			elif 'media_thumbnail' in entry.keys():
				image=str(entry['media_thumbnail'][0]['url'])
			elif 'links' in entry.keys():
				for link in entry['links']:
					if link['type']=='image/jpeg':
						image=link['href']
						break;
			#create a dict of vital info and append to our list
			feed_dict={'title':title,'link':link,'summary':summary,'published':published,'image':image}
			rss_feed_list.append(feed_dict)
		except Exception,e:
			print e
	#handle cases when rss can't be parsed show an error message
	if len(rss_feed_list)==0:
		return render_template("parse_error.html")
	#create a json object to send data to front end
	rss_dict={}
	rss_dict['articles']=[]
	for feed in rss_feed_list:
		rss_dict['articles'].append(feed)
	return render_template('result.html',rss_dict=rss_dict)

if __name__=="__main__":
	app.run(host='127.0.0.1',port=5000,debug=True)
			
