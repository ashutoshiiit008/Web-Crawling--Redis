import requests
from BeautifulSoup import BeautifulSoup
import redis

red_con = redis.StrictRedis(host='localhost', port=6379, db=0)


# Create a new instance of the Firefox driver
def crawl():

	url = 'http://www.rchiips.org/state-report-rch2.html'
	
	response = requests.get(url)	
	data = []
	imp = response.text.encode('utf-8')
	# print imp 

	Soup_obj = BeautifulSoup(imp)
	pdf_list = []
	for i,x in enumerate(Soup_obj.findAll('option')):
		if i > 0 :
			# print x 
			pdf_list.append(x.get('value')) 
		

	for pdf in pdf_list:
		if len(pdf) > 0 :
			url = 'http://www.rchiips.org/' + pdf
			red_con.sadd('DLHS', url)

if __name__ == '__main__':
    
    crawl()
