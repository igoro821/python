import sys
import MySQLdb as mdb
from MySQLdb.cursors import DictCursor
import datetime
test = 'Test'
data = 'string'
user = "260"

#путь через тунель, пере этим нужно поднять этот тунель
conection = mdb.connect(host = "127.0.0.1",user = "pfusers", password = "11111", db = "products", port = 3308)
cur1 = conection.cursor(DictCursor)
for i in range (75,100):
  query = "insert into cfg_pct_tests (customer_id, name, data) values(%s,'%s','%s')" % (user,test+str(i),data)
  cur1.execute(query)
print (cur1.fetchall())

