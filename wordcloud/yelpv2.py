import yelpapi 

key = ""
secret = ""
token = ""
token_secret = ""


yelp_api = yelpapi.YelpAPI(key, secret, token, token_secret)
search_results = yelp_api.search_query(term='Mexican', location='Baltimore', limit=10)
x =  search_results['businesses']
for result in x:
	business_id = result['id']
	business_search = yelp_api.business_query(id=business_id)
	y = business_search['reviews']
	print business_id
	print len(y)
	for z in y:
		excerptlist = []
		excerptlist.append(z['excerpt'])
		print excerptlist
