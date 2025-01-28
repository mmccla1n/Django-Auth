"""
This script can be used to inject into database during development, if needed.

Usage: python manage.py shell < inject.py
"""


from users_app.models import Users
from posts_app.models import Posts
from categories_app.models import Categories

# Creating categories
electronic_ctg = Categories( category = "Electronics" )
electronic_ctg.save()

services_ctg = Categories( category = "Services" )
services_ctg.save()

vehicles_ctg = Categories( category = "Vehciles")
vehicles_ctg.save()


# Create user 1
user_1 = Users(
	first_name = 'John',
    last_name = 'Smith',
    email = 'john_smith@email.com'
)
# Save user
user_1.save()

# Create post for user

user_1_post = Posts(
    post = 'Selling southpark themed laptop',
    user_id = user_1,
    category_id = electronic_ctg
)

user_1_post.save()

# Create user 2
user_2 = Users(
	first_name = 'Alice',
    last_name = 'Brown',
    email = 'alice_brown@email.com'
)
# Save user
user_2.save()

# Create post for user

user_2_post = Posts(
    post = 'Hiring software developers for AI robotics startup at Skynet',
    user_id = user_2,
    category_id = services_ctg
)

user_2_post.save()

# Create user 3
user_3 = Users(
	first_name = 'Peter',
    last_name = 'Griffin',
    email = 'peter_griffin@email.com'
)
# Save user
user_3.save()

# Create post for user

user_3_post = Posts(
    post = 'PeterCopter for sale, good condition, 1 crash',
    user_id = user_3,
    category_id = vehicles_ctg
)

user_3_post.save()

print('Injection Complete')






