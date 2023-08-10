import pymongo
import etrade.logins as logins

myclient = pymongo.MongoClient(logins.database)

mydb = myclient["mydatabase"]
mycol = mydb["new_portfolio"]


def portfolio_update():
    res = list(mycol.find({}, projection={"_id": False}))
    return res
