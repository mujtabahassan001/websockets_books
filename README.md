I make 2 apps in this Auth and Books.
**Auth App:**
I used JWT Authentication for Token generation through login user
I make custom user, which is register and login and successfully saves to postgresql database and when we login through its credential ( email and password ) then a jwt token is obtained which is then used to add books.

**Books App:**
After passing the  bearer token we can make crud operations on books ( create, retrieve, get_all, update, partial_update, delete ) 
We integrate websockets for live notification
Whenever we create, update, partial_update and delete then a websocket notification is triggered and shown in the websocket connection
