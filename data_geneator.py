import random
import string

user_ids = list(range(1, 1000))
recipient_ids = list(range(1,100))

def generate_message() -> dict:

    user1 = random.choice(recipient_ids)
    user2 = random.choice(user_ids)

    message = ''.join(random.choice(string.ascii_letters) for _ in range(32))

    return {
        'user1': user1,
        'user2': user2,
        'msg': message
    }


# if __name__ == '__main__':
#     print(generate_message())
