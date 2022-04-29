# onlineAouctionAPI
## check
**GET** click [here](https://onlineauctionapi.herokuapp.com/) to go to the website
## sign up
**POST** [https://onlineauctionapi.herokuapp.com/signup](https://onlineauctionapi.herokuapp.com/signup)    
required parameters: name, email, password, password2      
response: `{"status": "ok", "message": "welcome to ${name} ${email}" }`   
response: `{"status": "error", "message": "you already exist, link to sign in page" }`   
response: `{"status": "error", "message": "you are missing some arguments"}`
## sign in
**GET** [https://onlineauctionapi.herokuapp.com/signin](https://onlineauctionapi.herokuapp.com/signin)   
required parameters: email, password    
response: `{"status": "ok", "message": "welcome, here i need a link to the website, for render :)"}`    
response: `{"status": "error", "message": "you dont exist, i need a link to the sign up page, or reload to let his try again"}`
##sales
**GET** [https://onlineauctionapi.herokuapp.com/sales](https://onlineauctionapi.herokuapp.com/sales)   
no parameters needed;   
response array of 10 objects of sales:`[{   
        "admin": "admin email",
        "chat": "the chat id",
        "details": "it is good ", 
        "high": "buyer name",
        "image": "link to image",
        "name": "saleName",
        "price": "20202",   
        "sold": true }]`   
