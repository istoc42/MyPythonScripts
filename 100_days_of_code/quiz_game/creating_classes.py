class User:
    def __init__(self, user_id, username):      # Called everytime a new object is made with a class
        self.id = user_id
        self.username = username
        self.followers = 0      # Default attributes don't need to be passed in and are automatically created when an object is created.
        self.following = 0

    def follow(self, user):     # pass in the user they want to follow
        user.followers += 1
        self.following += 1

user_1 = User("001", "Derrick") # "user_1" is an object made from the "User" class.
user_2 = User("002", "Billy Butcher")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)