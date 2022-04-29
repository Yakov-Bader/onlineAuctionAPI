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
