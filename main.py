from pymongo import MongoClient
import pprint
client=MongoClient('mongodb://localhost:27017/')

document={
	"user_id":1,
	"name":"Akash",
	"user_type":"customer",
	"order":[
			{
				"order_id":100,
				"user_id":1,
				"total":500,
				"order_details":
				{
					"restuarnt_id":"abc",
					"menu_id":10,
					"qty":5,
					"amount":100
				}
			},
			{
				"order_id":200,
				"user_id":1,
				"total":1000,
				"order_details":
				{
					"restuarnt_id":"abc",
					"menu_id":15,
					"qty":2,
					"amount":50
				}
			}
	]
}
document2={
	"restuarnt_id":"abc",
	"restuarnt_name":"kathi king",
	"location_id":20,
	"restuarnt_type":3,
	"descrition":"please visit at king's home",
	"menu":
	{
		"id":1,
		"restuarnt_id":"abc",
		"category_id":1000,
		"menu_item":"paneer",
		"description":"kadhai paneer",
		"price":100
	},
	"order_details":[
				{
					"order_id":100,
					"menu_id":10,
					"qty":5,
					"user_id":1,
					"amount":100
				},
				{
					"order_id":200,
					"menu_id":15,
					"user_id":2,
					"qty":2,
					"amount":50
				}
			]

}
db=client.examples
db.user.insert(document)
for a in db.user.find():
	pprint.pprint(a)