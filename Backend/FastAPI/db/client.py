from pymongo import MongoClient

# db_client = MongoClient().local

db_client = MongoClient("mongodb+srv://test:test@cluster0.f5iu8oa.mongodb.net/test")

# "mongodb+svr://test:test@cluster0.kccyd3c.mongodb.net/test"
# "mongodb+srv://test:test@cluster0.f5iu8oa.mongodb.net/test"
# mongodb+srv://test:<db_password>@cluster0.f5iu8oa.mongodb.net/?appName=Cluster0
# mongodb+srv://test:<db_password>@cluster0.f5iu8oa.mongodb.net/?appName=Cluster0
# mongodb+srv://test:<db_password>@cluster0.f5iu8oa.mongodb.net/?appName=Cluster0+
# mongodb+srv://test:test@cluster0.f5iu8oa.mongodb.net/
# mongodb+srv://test:test@cluster0.f5iu8oa.mongodb.net/?appName=Cluster0