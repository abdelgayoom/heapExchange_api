
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
POST  api/v1/auth/register
~~~~
##### login
~~~~
POST  api/v1/auth/login
~~~~
##### logout 
~~~~
POST  api/v1/auth/logout
~~~~
##### list users or create one
~~~~
GET POST HEAD OPTIONS   api/v1/users
~~~~
##### get user detail or update it or delete it 
~~~~
GET PUT PATCH DELETE HEAD OPTIONS api/v1/users/{userID}
~~~~
##### get list of the posts or create one
~~~~
GET POST HEAD OPTIONS   api/v1/post
~~~~
##### get post detail or update it or delete it
~~~~
GET PUT PATCH DELETE HEAD OPTIONS api/vi/post/{postID}
~~~~
##### get questions list or create one
~~~~
GET POST HEAD OPTIONS   api/v1/question
~~~~
##### get question detail or update it or delete it
~~~~
GET PUT PATCH DELETE HEAD OPTIONS  api/v1/question/{questionID}
~~~~
