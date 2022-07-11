# onlineAouctionAPI
### Check
**GET** click [here](https://main--auctionlive.netlify.app/signin) to go to the soon working website 
### Sign Up
**POST** [https://onlineauctionapi.herokuapp.com/signup](https://onlineauctionapi.herokuapp.com/signup)   
describe: this is for signing up to the website   
required parameters: fname (string), lname (string), email (string), password (string)      
response: `{"status": "success", "message": "welcome to ${fname} ${lname}" }`   
response: `{"status": "error", "message": "you already exist, go to the sign in page" }`   
response: `{"status": "error", "message": "you are missing some arguments"}`
### Sign In
**POST** [https://onlineauctionapi.herokuapp.com/signin](https://onlineauctionapi.herokuapp.com/signin)   
describe: this is for signing in to the website;   
required parameters: email (string), password (string);    
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
### Delete account   
**POST**  [https://onlineauctionapi.herokuapp.com/delete](https://onlineauctionapi.herokuapp.com/delete)   
describe: delete a user account;  
required parameters: email (string), password (string);  
response: `{"status": "success", "message": "you deleted {} account and it's sales, you could always sign up again"}`  
response: `{"status": "error", "message": "the {} account does not exist"}`
### Get Sale  
**POST** [https://onlineauctionapi.herokuapp.com/getsale](https://onlineauctionapi.herokuapp.com/getsale)   
describe: this is for requesting a specific sale   
required parameters: email (string), password (string), id (string);   
response: `{"status": "error", "message": "I don't recognize you"}`  
response:`{"status": "error", "message": "I don't recognize this sale"}`    
response: a salse:
```
{"status": "success",
 "message": { "saleid": "saleid",
            "admin": "admin email",
            "chat": "the chat id",
            "details": "it is good ", 
            "high": "buyer mail",
            "image": "link to a image",
            "name": "sale name",
            "price": "20202",   
            "sold": true,
            "biders": ["yakov bader","chaim"],
            "likes": ["yakov bader","chaim"],
            "isadmin":true,
            "offers: false,
            "saved":false }
        }
```
### Get Sales  
**POST** [https://onlineauctionapi.herokuapp.com/getsales](https://onlineauctionapi.herokuapp.com/getsales)   
describe: this is for getting the list of sales for the home page   
required parameters: email (string), password (string), id (string);   
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
            "biders": ["yakov bader","chaim"],
            "likes": ["yakov bader","chaim"],  
            "sold": true,
            "isadmin":true,
            "offers: false,
            "saved":false
        }, 
        { 
            "saleid": "saleid",
            "admin": "admin email",
            "chat": "the chat id",
            "details": "it is good ", 
            "high": "buyer mail",
            "image": "link to a image",
            "name": "sale name",
            "biders": ["yakov bader","chaim"],
            "likes": ["yakov bader","chaim"],
            "price": "20202", 
            "isadmin":false,
            "offers: true,
            "saved":true 
        } ]
```
### Sales
**POST** [https://onlineauctionapi.herokuapp.com/sales](https://onlineauctionapi.herokuapp.com/sales)    
describe: this is for a admin to post a new sale   
required parameters: admin (string), password (string), image (string), details (string), price (double), name (string);     
response: `{"status": "success", "message": "you have crated a new sale"}`   
response: `{"status": "error", "message": "you are missing some details"}`  
response: `{"status": "error", "message": "you already have a sale with this name"}`
response: `{"status": "error", "message": "I don't recognize you"}`  
### Bid
**POST** [https://onlineauctionapi.herokuapp.com/bid](https://onlineauctionapi.herokuapp.com/bid)     
describe: this is for to bid on a sale   
required parameters: email (string), password (string), id (string), price (int);    
response: `{"status": "success", "message": "you have updated the sale"}`  
response: `{"status": "error", "message": "you need to bid higher"}`    
response: `{"status": "error", "message": "I don't recognize you"}`  
### Like
**POST** [https://onlineauctionapi.herokuapp.com/like](https://onlineauctionapi.herokuapp.com/like)    
describe: when someone likes or unlikes a sale, it will appear or disappear from the liked list
required parameters: email (string), password (string), id (string), like (boolean) (false for remove like or true for like);   
response: `{"status": "success", "message": "your remove like was successful"}`    
response: `{"status": "success", "message": "your like was successful"}`   
response: `{"status": "error", "message": "I don't recognize you"}`    
response: `{"status": "error", "message": "you are missing some details"}`  
### Remove  
**POST** [https://onlineauctionapi.herokuapp.com/remove](https://onlineauctionapi.herokuapp.com/remove)    
describe: admin remove a sale
required parameters: email (string), password (string), id (string);  
response: `{"status": "success", "message": "you removed the sale {}"}`  
response: `{"status": "error", "message": "the sale does not exist"}`  
response: `{"status": "error", "message": "I don't recognize you"}`  
### my sales  
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
            "saleid": "saleid",
            "admin": "admin email",
            "chat": "the chat id",
            "details": "it is good ", 
            "high": "buyer mail",
            "image": "link to a image",
            "name": "sale name",
            "price": "20202", 
            "isadmin":true,
            "biders": ["yakov bader","chaim"],
            "likes": ["yakov bader","chaim"],
            "offers: false,
            "saved":true,
            "sold":false
        }
    ]}
```  
### my saved  
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
            "saleid": "saleid",
            "admin": "admin email",
            "chat": "the chat id",
            "details": "it is good ", 
            "high": "buyer mail",
            "image": "link to a image",
            "name": "sale name",
            "price": "20202",
            "biders": ["yakov bader","chaim"],
            "likes": ["yakov bader","chaim"], 
            "isadmin":false,
            "offers: true,
            "saved":true,
            "sold":true
        }
    ]}
```  
### my offers   
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
            "saleid": "saleid",
            "admin": "admin email",
            "chat": "the chat id",
            "details": "it is good ", 
            "high": "buyer mail",
            "image": "link to a image",
            "name": "sale name",
            "price": "20202",
            "biders": ["yakov bader","chaim"],
            "likes": ["yakov bader","chaim"], 
            "isadmin":false,
            "offers: true,
            "saved":true,
            "sold":true
        }
    ]}
```
### get profile
**POST** [https://onlineauctionapi.herokuapp.com/getprofile](https://onlineauctionapi.herokuapp.com/getprofile)    
required params: email, password;  
response:`{"status": "error", "message": "I don't recognize you"}`  
response: this is a user profile object
```
{"status": "success", "message": {
        "email": "email@email.com",  
        "fname": "yyyyy",  
        "lname": "bbbbbb",
        "password": "shhhh, its a secret"
    }
   ```
### update profile  
**POST** [https://onlineauctionapi.herokuapp.com/updateprofile](https://onlineauctionapi.herokuapp.com/updateprofile)    
required params: email, password, newname, newlast, newpass;  
response:`{"status": "error", "message": "I don't recognize you"}`  
response:`{"status": "success", "message": "you have just updated you profile"}`   
###sell  
***POST***   
[https://onlineauctionapi.herokuapp.com/sell](https://onlineauctionapi.herokuapp.com/sell)    
required params: email, password, id;  
response: `{"status": "success", "message": "you have just sold the sale to {some email}"}`   
response: `{"status": "error", "message": "you dont own this sale"}`   
response: `{"status": "error", "message": "I don't recognize you"}`  
### message
***POST***  [https://onlineauctionapi.herokuapp.com/message](https://onlineauctionapi.herokuapp.com/message)  
required params: email, password, id, time, content  
response: `{"status": "success", "message": "grate, your message was sent"}`  
response: `{"status": "error", "message": "cant find this chat"}`  
response: `{"status": "error", "message": "I don't recognize you"}`  
### get chat 
***POST***  [https://onlineauctionapi.herokuapp.com/getchat](https://onlineauctionapi.herokuapp.com/getchat)    
required params: email, password, id;  
response: `{"status": "error", "message": "cant find this chat"}`  
response: `{"status": "error", "message": "I don't recognize you"}`  
response: array of chat messages
```
{"status": "success", "message": [
        {
            "content": "yersfgbsgb",
            "time": "0",
            "who": "email of poster"
        },
        {
            "content": "wertgvcxs",
            "time": "0",
            "who": "email of the poster "
        },
        {
            "content": "sdfghgfdfg",
            "time": "dfgfdfgf",
            "who": "hen@gmail.com"
        },
        {
            "content": "sdfghgfdfg",
            "time": "dfgfdfgf",
            "who": "hen@gmail.com"
        }}
   ```
# socket io
the link to connect to the socket is [https://onlineauctionapi.herokuapp.com/](https://onlineauctionapi.herokuapp.com/) the socket does not completely work yet
## connect 
required params: email, password;   
response: `{"status": "error", "message": "sorry, i dont recognize you"}`    
response: `{"status": "succses", "message": "welcome, now pick a chat"}`     