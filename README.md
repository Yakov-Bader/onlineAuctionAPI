# onlineAouctionAPI
## check
**GET** click [here](https://onlineauctionapi.herokuapp.com/) to go to the website
## sign up
**POST** [https://onlineauctionapi.herokuapp.com/signup](https://onlineauctionapi.herokuapp.com/signup)    
required parameters: name, email, password, password2      
response: `{"status": "ok", "message": "welcome to ${name} ${email}" }`   
response: `{"status": "error", "message": "you already exist" }`   
response: `{"status": "error", "message": "you are missing some arguments"}`

