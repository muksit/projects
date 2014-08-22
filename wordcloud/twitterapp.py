from TwitterAPI import TwitterAPI
import nltk




key = "8PN0z0v104Kvos7z2xhETftQQ"
secret = "h5UxoOSUul8pWQ1SjpsIPYBZgIAjjwPvDd9bnyhgNhidFPAZbq"
token = "27931231-gtOLN2K1A1NpJG69OjqBtvMYxW4ltqUlkLY2ydQN0"
token_secret = "N8zPKf89ZhBLrAkRnlrCeza1NpnAFuvwuqRDMquD0Vo6C"

api = TwitterAPI(key, secret, token, token_secret)

r = api.request('search/tweets', {'q':'gaza', 'lang': 'en', 'count': 100})
# for item in r.get_iterator():
textarray = []
for item in r:
    
    textarray.append(item['text'])

print textarray

blacklist = "a,we,We,table,It,Our,us,us.,/,/,The,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,would,yet,you,your"
splitblacklist = blacklist.split()
print splitblacklist

def containsObject(obj, list2):
    for i in list2:
        if (i == obj):
            return True
    return False

def wordfilter(list2):
    newlist = ""
    for x in list2:
        if (containsObject(x, splitblacklist) == False):
            newlist = newlist + x
        # if (adverb(list[x], ))
    return newlist   


filteredwords = wordfilter(textarray)
tokenizedfilteredwords = filteredwords.split()
print tokenizedfilteredwords


def containsObject(obj, list):
    for i in list:
        if (i == obj):
            return True
    return False
