#2023/04/06
#클래스 명으로 파스칼 케이스가 쓰이고, 그 외의 경우엔 스네이크 케이스가 많이 쓰임(PascalCase, snake_case)
class User:
    #생성자(객체 생성 시, 실행되는 메서드 initialize에서 유래)
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user) :
        user.followers += 1
        self.following += 1

user_1 = User("001", "Samanda")
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)