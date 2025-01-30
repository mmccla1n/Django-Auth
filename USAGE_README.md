To build container, execute cmd: 
    docker compose up -d --build

After building execute the following commands, to make migrations in container:
    docker-compose exec api python manage.py makemigrations
    docker-compose exec api python manage.py migrate

Their is a dum,y data injection script that will inject data into the database.
To use, execute the following commands:
    docker exec -it <CONTAINER_ID> OR <CONTAINER_NAME> bash
    python manage.py shell < inject.py

Following Resources are available:
    User signup = http://localhost:8001/user_accounts/signup
    Tradetoken = http://localhost:8001/user_accounts/get-token
    View all posts = http://localhost:8001/api/v1/posts/
    View all users = http://localhost:8001/api/v1/users/
    View single user = http://localhost:8001/api/v1/users/<user_id_int>/
    List view of all the categories, post request available as well = http://localhost:8001/api/v1/categories/
    Detail view of a specific category. update and delete = http://localhost:8001/api/v1/categories/<post_id_int>     
    List view of all the posts for a given category, post =  http://localhost:8001/api/v1/categories/<category_id_int>/posts
    Detail view of a specific post in a specific category, update = http://localhost:8001/api/v1/categories/<category_id_int>/posts/<post_id_int>
