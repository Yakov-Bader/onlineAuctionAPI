# onlineAouctionAPI
## Check
**GET** click [here](https://onlineauctionapi.herokuapp.com/) to go to the website
## Sign Up
**POST** [https://onlineauctionapi.herokuapp.com/signup](https://onlineauctionapi.herokuapp.com/signup)   
describe: this is for signing up to the website   
required parameters: name, email, password      
response: `{"status": "success", "message": "welcome to ${name} ${email}" }`   
response: `{"status": "error", "message": "you already exist, link to sign in page" }`   
response: `{"status": "error", "message": "you are missing some arguments"}`
## Sign In
**GET** [https://onlineauctionapi.herokuapp.com/signin](https://onlineauctionapi.herokuapp.com/signin)   
describe: this is for signing ip to the website;   
required parameters: email, password;    
response: `{"status": "success", "message": "welcome, here i need a link to the website, for render :)"}`    
response: `{"status": "error", "message": "you don't exist, you could sign up in the sign-up page, or try again"}`  
## Delete account   
**POST**  [https://onlineauctionapi.herokuapp.com/delete](https://onlineauctionapi.herokuapp.com/delete)   
describe: delete a user account;  
required parameters: email, password;  
response: `{"status": "success", "message": "you deleted {} account and it's sales, you could always sign up again"}`  
response: `{"status": "error", "message": "the {} account does not exist"}`
## Sales
**GET** [https://onlineauctionapi.herokuapp.com/sales](https://onlineauctionapi.herokuapp.com/sales)   
describe: this is for getting the list of sales for the home page   
required parameters: email, password;   
response: `{"status": "error", "message": "I don't recognize you"}`  
response: array of up to 10 objects of sales:
```
[{      "saleid": "saleid",
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
        "saved":1, 
        "sold": true } ]
```
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
required parameters: email, password, id, like (0 for remove like or 1 for like);   
response: `{"status": "success", "message": "your remove like was successful"}`    
response: `{"status": "success", "message": "your like was successful"}`   
response: `{"status": "error", "message": "I don't recognize you"}`    
response: `{"status": "error", "message": "you are missing some details"}`  
##Remove  
**POST** [https://onlineauctionapi.herokuapp.com/remove](https://onlineauctionapi.herokuapp.com/remove)    
describe: admin remove a sale
required parameters: email, password, id, price;  
response: `{"status": "success", "message": "you removed the sale {}"}`  
response: `{"status": "error", "message": "the sale does not exist"}`  
response: `{"status": "error", "message": "I don't recognize you"}`