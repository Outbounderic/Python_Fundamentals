class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.followers = 0
        self.following = 0

    def new_follower(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("John", 1234)
user_2 = User("Steve", 4556)
user_1.new_follower(user_2)
print(user_1.followers)