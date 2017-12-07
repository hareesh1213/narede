import json
import urllib2
import MySQLdb
import time
import re

db	   = MySQLdb.connect("localhost","root","","movies_scrap_data")
cursor = db.cursor()

SEARCH_URL = "https://itunes.apple.com/search?term=movies&limit=1000"
vendor_id  = 2
created_date = time.strftime("%Y-%m-%d %H:%M:%S")
rowcount = 0
movies = []

def get_art():
	rowcount  =	0
	response = urllib2.urlopen("%s" % (SEARCH_URL))
	results = json.load(response)
	#print(results['resultCount'])
	if results['resultCount'] > 0:
		for index, result in enumerate(results['results']):
            #print ("%s. %s" % (index+1, result['trackViewUrl']))
			movie = {}

			if 'trackId' in  result: 
				movie['track_id'] =  result['trackId'] 
			else:  movie['track_id'] = '' 
			
			if 'trackName' in result:
				movie['movie_name'] = result['trackName']  
			else:  movie['movie_name'] = ''

			if 'trackViewUrl' in  result: 
				movie['movie_URL'] =  result['trackViewUrl'] 
			else:  movie['movie_URL'] = ''

			if 'artworkUrl100' in  result:
				movie['movie_art'] =  result['artworkUrl100'] 
			else:  movie['movie_art'] = ''
					
			if 'primaryGenreName' in result:	
				movie['movie_genre'] = result['primaryGenreName'] 
			else:  movie['movie_genre'] = ''

			if 'collectionPrice' in result:	
				movie['collectionPrice'] = result['collectionPrice'] 
			else: movie['collectionPrice'] = '0.00'
			
			if 'trackPrice' in result: 
				movie['trackPrice'] = result['trackPrice'] 
			else: movie['trackPrice'] = '0.00'
			
			if 'primaryGenreName' in result:	
				movie['trackRentalPrice'] = result['primaryGenreName'] 
			else: movie['trackRentalPrice'] = '0.00'
			
			if 'collectionHdPrice' in result: 
				movie['collectionHdPrice'] = result['collectionHdPrice'] 
			else: movie['collectionHdPrice'] = '0.00'
			
			if 'trackHdPrice' in result:	
				movie['trackHdPrice'] = result['trackHdPrice'] 
			else: movie['trackHdPrice'] = '0.00'
			
			if 'trackHdRentalPrice' in result: 
				movie['trackHdRentalPrice'] = result['trackHdRentalPrice'] 
			else: movie['trackHdRentalPrice'] = '0.00'
			#print(index)
			#movies[index] = movie
			#movies.append(movie)
	#get_art()
		#print(len(movies))
			#x = cursor.execute("SELECT * FROM tbl_movies")
			#print x

			'''Inserting into movies table'''
			cursor.execute("INSERT INTO tbl_movies (title,description,thumbnail_url,video_url,unique_id,vendor_id,created_date,updated_date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(movie['movie_name'],'',movie['movie_art'],movie['movie_URL'],movie['track_id'],vendor_id,created_date,created_date))
			movie_id = cursor.lastrowid
			
			'''Inserting into prices table'''
			cursor.execute("INSERT INTO tbl_prices (movie_id,vendor_id,price_value,created_date,updated_date) VALUES(%s,%s,%s,%s,%s)",(movie_id,vendor_id,movie['trackHdPrice'],created_date,created_date))
			rowcount += 1
		print("Inserted Movies = {}".format(rowcount))
if __name__ == "__main__":
	get_art()
db.commit()    		

