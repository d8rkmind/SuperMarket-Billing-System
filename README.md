# Supermarket Billing REST API
Backend assignment 1 task implemented using Django and Sqlite3 as database .The whole project was contained inside a python virtual envionment so to manage Python packages for different python packages for this project
# 1. Introduction 
## 1.1 Purpose of this document 
To give the overview of the project with Endpoints , Methods, Request and Response JSON provided by the working of the code 
## 1.2 Overview 
The Supermarket management system is the part of the problem statement given below as an assignment task 
~~~
You are required to create REST APIS for a supermarket application. It is a
self-service store offering a wide variety of food, beverages and household
products, organised into various categories.
The categories can have subcategories. Subcategories have items under
them. Items can be sold by Units. Every item has a price for which it can be
sold.
Following are the product requirements that you are expected to :
		1. Get all items.
		2. Get all items of a category with all the details.
		3. Get all items of a sub-category with all the details.
		4. Put items into the database ( db of your choice ).
		5. Update item details. 
~~~
## 1.3 Product capabilities
- Ability to send several types of requests to the   ```/items```  endpoint.
- Handles all item searches, category searches, subcategory searches, and amount-based searches.
- Handles searches, updates, and input to the respected database.
- Output serialized and responded as JSON format  

# 2. Operations of API
The API's operation will be thoroughly detailed in this section about the following topics .
- Database
- Endpoints 
- Methods 
- Response JSON

## 2.1 Database 
With considering the current status of the project the database is implemented in ***sqlite3*** and *serializers from are used django.core* is used to serialize the data objects from the Models creates with the following specification:  
### 2.1.1 Model used : 
The current model is  created on the  basis of the data given in as sample output 
|Name|Type  |
|--|--|
|name|models.CharFeild(max_length=255)  |
|category|models.CharFeild(max_length=255)|
|subcategory|models.CharFeild(max_length=255)|
|amount|models.IntegerFeild()|
### 2.1.2 Database : 
As Above mentioned the database is implemented using sqlite3 as it is by default database with Django 
|name|category|subcategory|amount|
|--|--|--|--|
|limca|food|beverage|100|
|potato|food|vegetable|25|
|mango|food|fruit|50|
|milkybar|food|candy|10
|parker|stationery|pen|20

## 2.2 Endpoints
All requests received to the server are currently handled at the ```/items``` endpoint, and any additional requests to endpoints other than those listed above will be returned with the following output and a status code of  **404** which is applied using wildcard at *urls.py* file.

**POC :**
 *1. senting get request to ```/items``` . Response of the claim* 

```
[
   {
      "model":"store.store",
      "pk":1,
      "fields":{
         "name":"limca",
         "category":"food",
         "subcategory":"beverage",
         "amount":100
      }
   }
]
```
*2. sending get request to any other end point*
```
{"404": "Endpoint not found", "avaliable_endpoint": "/items"}
```
All the requests are processed based upon the request received at the above mentioned endpoint

## 2.3 Methods 
As previously stated, all contact with the server is done using GET, POST, PUT, and PATCH requests, which are dependent on the REST query values provided with the request.

-	**GET**   ---> Read Data from the server based on query's
-	**POST** ---> Create NEW record
-	**PUT** ---> If the record exists then update else create a new record
-	**PATCH** ---> Update an existing record only 

### 2.3.1 The GET Method
The Get method is used to retrieve or obtain information from the server using a URL. This project reads data using specific queries that are tailored to the question given.
#### Response of different type of GET requests 
1. Accessing all data elements at ```GET /items```
```
request url : http://localhost:8000/items
```
```
# response as json : 
[
   {
      "model":"store.store",
      "pk":1,
      "fields":{
         "name":"limca",
         "category":"food",
         "subcategory":"beverage",
         "amount":100
      }
   },
   {
      "model":"store.store",
      "pk":2,
      "fields":{
         "name":"potato",
         "category":"food",
         "subcategory":"vegetable",
         "amount":25
      }
   },
   {
      "model":"store.store",
      "pk":3,
      "fields":{
         "name":"mango",
         "category":"food",
         "subcategory":"fruit",
         "amount":50
      }
   },
   {
      "model":"store.store",
      "pk":4,
      "fields":{
         "name":"milkybar",
         "category":"food",
         "subcategory":"candy",
         "amount":10
      }
   },
   {
      "model":"store.store",
      "pk":8,
      "fields":{
         "name":"parker
         ",
         "category":"stationery",
         "subcategory":"pen",
         "amount":20
      }
   }
]
``` 
2.	Accessing only specific element using fixed key values ```['name','category','subcategory','amount']```  	 :
```
# requests urls : 
	1 - http://localhost:8000/items?name=limca
	2 - http://localhost:8000/items?category=food
	3 - http://localhost:8000/items?subcategory=fruit
	4 - http://localhost:8000/items?amount=50
```
```
#response of request 1 as example response 
[
   {
      "model":"store.store",
      "pk":1,
      "fields":{
         "name":"limca",
         "category":"food",
         "subcategory":"beverage",
         "amount":100
      }
   }
]
```
Any request with other parameters will be retuned with **400** response and if the specified value of the parameter is not available in database it returns **404** response 

### 2.3.2 The POST Method 
The post method is used for inserting new items in the backend database where each value is inserted to the database : 
**POC of POST request:**
```
import requests

def main():
    res = requests.post("http://localhost:8000/items?name=parker&category=stationery&subcategory=pen&amount=20")
    print(res.content)
if __name__ =="__main__":
    main()
```
The user needs to enter all data-value pairs or else will receive **400** response instead of **200** response 

### 2.3.3 The PUT Method 
In this method the resource is first identified from URL and if it exists, then it is updated, otherwise, a new resource is created .
**POC of PUT request**
```
import requests

def main():
    res = requests.put("http://localhost:8000/items?name=parker&category=stationery&subcategory=pen&amount=20")
    print(res.content)
if __name__ =="__main__":
    main()
```
The user needs to enter all data-value pairs or else will receive  **400**  response instead of  **200**  response
### 2.3.4 The PATCH Method 
The PATCH method is used to update the values of already existing the  properties.
**POC of PATCH request:**
```
import requests

def main():
    res = requests.put("http://localhost:8000/items?name=parker&category=stationery&subcategory=pen&amount=20")
    print(res.content)
if __name__ =="__main__":
    main()
```
The user needs to enter all data-value pairs or else will receive  **400**  response instead of  **200**  response. But if the data is already in the database then they will be presented wit **417** response 

## 2.4 Response JSON 

All the response from the server uses JsonResponse function (*from django.http import JsonResponse*) to respond the json data and the data's which is directly from the is received from serializers .serialize function (*from django.core import serializers*) . Below is the Sample Response from ```http://localhost:8000/items```

```
[
   {
      "model":"store.store",
      "pk":1,
      "fields":{
         "name":"limca",
         "category":"food",
         "subcategory":"beverage",
         "amount":100
      }
   },
   {
      "model":"store.store",
      "pk":2,
      "fields":{
         "name":"potato",
         "category":"food",
         "subcategory":"vegetable",
         "amount":25
      }
   },
   {
      "model":"store.store",
      "pk":3,
      "fields":{
         "name":"mango",
         "category":"food",
         "subcategory":"fruit",
         "amount":50
      }
   },
   {
      "model":"store.store",
      "pk":4,
      "fields":{
         "name":"milkybar",
         "category":"food",
         "subcategory":"candy",
         "amount":10
      }
   },
   {
      "model":"store.store",
      "pk":8,
      "fields":{
         "name":"parker",
         "category":"stationery",
         "subcategory":"pen",
         "amount":20
      }
   }
]
``` 

# 3. Conclusion 
Supermarket chains or individual stores are the targeted audience of this POC project .They could use it to manage their chain of stores and maintain clear records and analyse their sales . Since everything is online it would be convenient to sync all the data across various stores at different locations.
