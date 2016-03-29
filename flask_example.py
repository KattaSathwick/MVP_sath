from flask import Flask, render_template
import MySQLdb
import json
import re
app = Flask(__name__)
conn = MySQLdb.connect(host="localhost", user = "root", db = "twitter_ratings", passwd="ubuntu", charset="utf8", use_unicode=True).cursor()

query = "select rating from Rating;"
conn.execute(query)
ratings = conn.fetchall()

query2 = "select title from Movie;"
conn.execute(query2)
titles = conn.fetchall()

query3 = "select reference_url from Movie;"
conn.execute(query3)
urls = conn.fetchall()

query4 = "select description from Movie;"
conn.execute(query4)
descriptions = conn.fetchall()

@app.route("/")
def hello():
    context={}
    for i,j,k in zip(titles,ratings,urls):
	title = i[0]
	rating = j[0]
	url = k[0]
	context.update({title:{rating:url}})
    return render_template('basic.html',context=context)


'''
@app.route("/description")
def desc():
    context = {}
    for m,n in zip(titles,descriptions):
        title = m[0]
        description =n[0]
        context.update({title:description})
    return render_template('next_desc.html',context=context)
'''
if __name__ == "__main__":
    app.run(debug=True)
