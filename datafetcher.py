import urllib
import json
import os

class FetchCoordinates:

	def __init__(self,cityname):
		 #constructor
		print 'Cityname is',cityname
		self.query=cityname
		print 'in __init__ query is ',self.query	
	serviceurl="https://maps.googleapis.com/maps/api/geocode/json?"
	def __execute__(self):
		if(len(self.query)<1):
			print 'Enter proper data' #i.e a null string

		url=self.serviceurl+urllib.urlencode({'sensor':'false','address':self.query})
		print url
		try:
			print 'Fetching data...'
			data=urllib.urlopen(url).read()
                        
		except:
			return 'Data not found'

		#json parsing
		try:
			js=json.loads(data)
		except:
				js=None
		if 'status' not in js or js['status']!='OK':
			return "Failure in parsing data"
		
		return str(js['results'][0]['geometry']['location']['lat'])+","+str(js['results'][0]['geometry']['location']['lng'])
