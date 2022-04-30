# onlineAouctionAPI
## Check
**GET** click [here](https://onlineauctionapi.herokuapp.com/) to go to the website
## Sign Up
**POST** [https://onlineauctionapi.herokuapp.com/signup](https://onlineauctionapi.herokuapp.com/signup)   
describe: this is for signing up to the website   
required parameters: name, email, password, password2      
response: `{"status": "ok", "message": "welcome to ${name} ${email}" }`   
response: `{"status": "error", "message": "you already exist, link to sign in page" }`   
response: `{"status": "error", "message": "you are missing some arguments"}`
## Sign In
**GET** [https://onlineauctionapi.herokuapp.com/signin](https://onlineauctionapi.herokuapp.com/signin)   
describe: this is for signing ip to the website   
required parameters: email, password    
response: `{"status": "ok", "message": "welcome, here i need a link to the website, for render :)"}`    
response: `{"status": "error", "message": "you dont exist, i need a link to the sign up page, or reload to let him try again"}`
## Sales
**GET** [https://onlineauctionapi.herokuapp.com/sales](https://onlineauctionapi.herokuapp.com/sales)   
describe: this is for getting the list of sales for the home page   
no parameters needed;   
response array of up to 10 objects of sales:`[{ 
        "saleid": "saleid",
        "admin": "admin email",
        "chat": "the chat id",
        "details": "it is good ", 
        "high": "buyer mail",
        "image": "link to a image",
        "name": "sale name",
        "price": "20202",   
        "sold": true }]`   

**POST** [https://onlineauctionapi.herokuapp.com/sales](https://onlineauctionapi.herokuapp.com/sales)    
describe: this is for a admin to post a new sale   
required parameters: admin, image, details, price, name;     
response: `{"status": "ok", "message": "you have crated a new sale"}`   
response: `{"status": "error", "message": "you are missing some details"}`     
## Bid
**POST** [https://onlineauctionapi.herokuapp.com/bid](https://onlineauctionapi.herokuapp.com/bid)     
describe: this is for to bid on a sale   
required parameters: email, password, saleid, price;    
response: `{"status": "ok", "message": "you have updated the sale"}`
response: `{"status": "error", "message": "you need to bid higher"}`    
response: `{"status": "error", "message": "I don't recognize you"}`
