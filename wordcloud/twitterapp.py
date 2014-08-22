from TwitterAPI import TwitterAPI
import nltk
from collections import Counter
import os, time, json, datetime 
from json import JSONEncoder, load
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, json, jsonify, send_file


# create application 
app = Flask(__name__)
app.config.from_object(__name__)
app.config["DEBUG"] = True  # Only include this while you are testing your app

key = "8PN0z0v104Kvos7z2xhETftQQ"
secret = "h5UxoOSUul8pWQ1SjpsIPYBZgIAjjwPvDd9bnyhgNhidFPAZbq"
token = "27931231-gtOLN2K1A1NpJG69OjqBtvMYxW4ltqUlkLY2ydQN0"
token_secret = "N8zPKf89ZhBLrAkRnlrCeza1NpnAFuvwuqRDMquD0Vo6C"
blacklist = "a,we,We,table,It,Our,us,us.,/,/,The,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your"
splitblacklist = blacklist.split()

api = TwitterAPI(key, secret, token, token_secret)



# for item in r.get_iterator():
# textarray = []
# for item in r:  
#     textarray.append(item['text'])



@app.route('/',)
def input():
    return render_template('index.html')


#return list of words
@app.route('/ask')
def givecloud():
    wordtograph = request.args.get('word')
    words = ', '.join(getwordlist(wordtograph)) 

    return ', '.join(removedupes(words))


# get a clean list of words 
def getwordlist(word):
    r = api.request('search/tweets', {'q': word, 'lang': 'en', 'count': 100})
    textarray = []
    for item in r:
        textarray.append(item['text'])
    filteredwords = wordfilter(textarray)
    tokenizedfilteredwords = filteredwords.split()
    return tokenizedfilteredwords



def containsObject(obj, list2):
    for i in list2:
        if (i == obj):
            return True
    return False

def wordfilter(list2):
    newlist = ""
    for x in list2:
        if (containsObject(x, splitblacklist) == False) and (x[:4] != "http") and (x[:2] != "RT"):
            newlist = newlist + x
        # if (adverb(list[x], ))
    return newlist   


def containsObject(obj, list):
    for i in list:
        if (i == obj):
            return True
    return False

def removedupes(text):
    wordfrequency = getFrequency(text)
    keys = []
    for item in wordfrequency:
        keys.append(item)
    return keys
  

def getFrequency(text):
    arraytext = text.split();
    freq = Counter(arraytext)  #might not need to remove counter
    return freq
    # newfreq = {}
    # for item in freq:
    #     newfreq[item] = freq[item]
    # return newfreq







if __name__ == '__main__':
    app.run()
