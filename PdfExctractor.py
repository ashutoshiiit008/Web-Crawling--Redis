import redis
import os
import csv
import subprocess
import os.path
import time 
import redis
import ast

red_con = redis.StrictRedis(host='localhost', port=6379, db=0)

# import pdb;pdb.set_trace()
while True:
    rec = red_con.spop('DLHS')
    if rec:
        pdf_url = rec
        print pdf_url
        os.system('wget %s' % pdf_url)
        # 'wget' , %s , %pdf_url

    	

    else:
    	print 'Empty List'
    	break
