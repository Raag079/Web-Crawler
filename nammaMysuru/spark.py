##1. Add this to .bashrc 
##export SPARK_HOME=/home/pi/spark-2.0.0-bin-hadoop2.7
##export PATH=$PATH:$SPARK_HOME/bin
##2. Google Python spark API for information 
##3. Go to Spark/conf, copy log4j.properties.template to log4j.properties then change category to warn to get rid of too many console things 
		#log4j.rootCategory=WARN, console 

import sys 
from bs4 import BeautifulSoup
import urllib
import urllib2

from pyspark.sql import SparkSession

#list = {1,2,3,4,5}
movieList = ['Mungaru Male 2 Kannada Movie official trailer', 'Inception English Movie official trailer', 'Race 2 Hindi Movie official trailer'] 
#movieList = ['Mungaru Male 2 Kannada Movie official Trailer']

def getYouTubeString(searchText): 
	query = urllib.quote(searchText)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	vid = soup.findAll(attrs={'class':'yt-uix-tile-link'})
	##Out of all results get url for first result 
	dataFirst = vid[1]['href']
	movieVideo = dataFirst[dataFirst.find('=')+1:] 	
	##Store Video ID in dictionary 
	return movieVideo

def main(argv):
	spark = SparkSession.builder.appName('test').getOrCreate()
	sc = spark.sparkContext
	log4j = sc._jvm.org.apache.log4j 
	log4j.LogManager.getRootLogger().setLevel(log4j.Level.WARN)
	rdd = sc.parallelize(argv)
	result = rdd.map(getYouTubeString).collect()
	print result

if __name__ == '__main__':
	main(sys.argv)
