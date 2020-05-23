
### overview 

 api version for [heapExchange](https://github.com/abdelgayoom/heapExchange)
 later i'm gonna make single page application for the frontend with React and Redux


### installation
~~~~
git clone https://github.com/abdelgayoom/heapExchange_api.git
~~~~
##### create virtual environment in terminal
~~~~
python3 -m venv heapExchange_api/venv
source heapexchange_api/venv/bin/activate
~~~~
##### Install requirements
~~~~
cd heapExchange_api
pip3 install -r requirements.txt
~~~~

#### run
~~~~
python3 manage.py runserver
~~~~

### Endpoints

##### create new account (register)
~~~~
api/v1/auth/register
~~~~
##### login
~~~~
api/v1/auth/login
~~~~
##### logout 
~~~~
api/v1/auth/logout
~~~~
##### users list
~~~~
api/v1/users
~~~~
##### user detail
~~~~
api/v1/users/{userID}
~~~~
##### post list
~~~~
api/v1/post
~~~~
##### posts detail
~~~~
api/vi/post/{postID}
~~~~
##### questions list
~~~~
api/v1/question
~~~~
##### question detail
~~~~
api/v1/question/{questionID}
~~~~
