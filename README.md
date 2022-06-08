# onlineAouctionAPI
## Check
**GET** click [here](https://onlineauctionapi.herokuapp.com/) to go to the website
## Sign Up
**POST** [https://onlineauctionapi.herokuapp.com/signup](https://onlineauctionapi.herokuapp.com/signup)   
describe: this is for signing up to the website   
required parameters: fname, lname, email, password      
response: `{"status": "success", "message": "welcome to ${fname} ${lname}" }`   
response: `{"status": "error", "message": "you already exist, go to the sign in page" }`   
response: `{"status": "error", "message": "you are missing some arguments"}`
## Sign In
**POST** [https://onlineauctionapi.herokuapp.com/signin](https://onlineauctionapi.herokuapp.com/signin)   
describe: this is for signing ip to the website;   
required parameters: email, password;    
response: 
```
{"status": "success", 
"message": "welcome to {} {}", 
"fname": "fisrt name", 
"lname": "last name", 
"email": "email", 
"password": "password"}
```    
response: `{"status": "error", "message": "you don't exist, you could sign up in the sign-up page, or try again"}`  
## Delete account   
**POST**  [https://onlineauctionapi.herokuapp.com/delete](https://onlineauctionapi.herokuapp.com/delete)   
describe: delete a user account;  
required parameters: email, password;  
response: `{"status": "success", "message": "you deleted {} account and it's sales, you could always sign up again"}`  
response: `{"status": "error", "message": "the {} account does not exist"}`
## Get Sales  
**POST** [https://onlineauctionapi.herokuapp.com/getsales](https://onlineauctionapi.herokuapp.com/getsales)   
describe: this is for getting the list of sales for the home page   
required parameters: email, password, amount;   
response: `{"status": "error", "message": "I don't recognize you"}`  
response:`{"status": "error", "message": "you need to give a valid amount number"}`    
response: array of up to "amount" objects of sales:
```
{"status": "success",
 "message": [{ 
            "saleid": "saleid",
            "admin": "admin email",
            "chat": "the chat id",
            "details": "it is good ", 
            "high": "buyer mail",
            "image": "link to a image",
            "name": "sale name",
            "price": "20202",   
            "sold": true,
            "admin":1,
            "offers: 0,
            "saved":0
        }, 
        { 
            "saleid": "saleid",
            "admin": "admin email",
            "chat": "the chat id",
            "details": "it is good ", 
            "high": "buyer mail",
            "image": "link to a image",
            "name": "sale name",
            "price": "20202", 
            "admin":0,
            "offers: 1,
            "saved":1 
        } ]
```
## Sales
**POST** [https://onlineauctionapi.herokuapp.com/sales](https://onlineauctionapi.herokuapp.com/sales)    
describe: this is for a admin to post a new sale   
required parameters: admin, password, image, details, price, name;     
response: `{"status": "success", "message": "you have crated a new sale"}`   
response: `{"status": "error", "message": "you are missing some details"}`  
response: `{"status": "error", "message": "you already have a sale with this name"}`
response: `{"status": "error", "message": "I don't recognize you"}`  
## Bid
**POST** [https://onlineauctionapi.herokuapp.com/bid](https://onlineauctionapi.herokuapp.com/bid)     
describe: this is for to bid on a sale   
required parameters: email, password, id, price;    
response: `{"status": "success", "message": "you have updated the sale"}`  
response: `{"status": "error", "message": "you need to bid higher"}`    
response: `{"status": "error", "message": "I don't recognize you"}`  
## Like
**POST** [https://onlineauctionapi.herokuapp.com/like](https://onlineauctionapi.herokuapp.com/like)    
describe: when someone likes or unlikes a sale, it will appear or disappear from the liked list
required parameters: email, password, id, like (false for remove like or true for like);   
response: `{"status": "success", "message": "your remove like was successful"}`    
response: `{"status": "success", "message": "your like was successful"}`   
response: `{"status": "error", "message": "I don't recognize you"}`    
response: `{"status": "error", "message": "you are missing some details"}`  
## Remove  
**POST** [https://onlineauctionapi.herokuapp.com/remove](https://onlineauctionapi.herokuapp.com/remove)    
describe: admin remove a sale
required parameters: email, password, id, price;  
response: `{"status": "success", "message": "you removed the sale {}"}`  
response: `{"status": "error", "message": "the sale does not exist"}`  
response: `{"status": "error", "message": "I don't recognize you"}`  
## my sales  
**POST** [https://onlineauctionapi.herokuapp.com/mysales](https://onlineauctionapi.herokuapp.com/mysales)    
dscribe: get users sales that he created;   
required parameters: email, password;  
response: `{"status": "error", "message": "you did not create a sale yet"}`  
response: `{"status": "error", "message": "I don't recognize you"}`   
response: this is an array of his sales
```
{"status": "success",
 "message": [
        {
            "admin": "chaimsh1@gmail.com",
            "chat": "chat id",
            "details": "sdfghjk",
            "high": "no one gave a bid yet",
            "image": "sdfghj",
            "name": "sdfgh",
            "price": 300.0,
            "saleid": 9,
            "sold": false
        }
    ]}
```  
## my saved  
**POST** [https://onlineauctionapi.herokuapp.com/mysaved](https://onlineauctionapi.herokuapp.com/mysaved)    
dscribe: get users saved (liked) sales;   
required parameters: email, password;  
response: `{"status": "error", "message": "you have no saved sales"}`  
response: `{"status": "error", "message": "I don't recognize you"}`   
response: this is an array of his saved sales
```
{"status": "success",
 "message": [
        {
            "admin": "chaimsh1@gmail.com",
            "chat": "chat id",
            "details": "sdfghjk",
            "high": "no one gave a bid yet",
            "image": "sdfghj",
            "name": "sdfgh",
            "price": 300.0,
            "saleid": 9,
            "sold": false
        }
    ]}
```  
## my offers   
**POST** [https://onlineauctionapi.herokuapp.com/myoffers](https://onlineauctionapi.herokuapp.com/myoffers)    
dscribe: get users sales that he put in an offer (bid);   
required parameters: email, password;  
response: `{"status": "error", "message": "you did not bid on a sale yet"}`    
response: `{"status": "error", "message": "I don't recognize you"}`     
response: this is an array of his offered sales
```
{"status": "success",
 "message": [
        {
            "admin": "chaimsh1@gmail.com",
            "chat": "chat id",
            "details": "sdfghjk",
            "high": "no one gave a bid yet",
            "image": "sdfghj",
            "name": "sdfgh",
            "price": 300.0,
            "saleid": 9,
            "sold": false
        }
    ]}
```
## socket io
the link to connect to the socket is [https://onlineauctionapi.herokuapp.com/](https://onlineauctionapi.herokuapp.com/) the socket does not completely work yet