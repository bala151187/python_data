from pymongo import MongoClient
import pymongo,logging,os
connectString = os.environ['MONGODB_wauth']
connection = MongoClient(connectString, connectTimeoutMS=5000)
auth_db = connection['auth']
user = auth_db['users']
user.insert_one({
  "email": "something@somewhere.com",
  "key": "abc",
  "secret": "abc"
})

token=auth_db['tokens']
token.insert_one({
 "token":"sadjhsadkasjdkja"
})

admin_db = connection['admin']
admin_db.add_user('accountUser', 'password', roles=[{'role':'readWrite','db':'admin'}])

data_db = connection['data']
account=data_db['accounts']
account.insert_one({
  "employees": 12,
  "valuation": 100,
  "name": "helloworld"
})

