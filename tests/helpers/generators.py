import json
import random
import string


def replace_random_values(data):
    for key, value in data.items():
        match value:
            case 'RANDOM_ID':
                data[key] = random.randint(100, 1000)
            case 'RANDOM_PHONE':
                data[key] = "+7" + str(random.randint(1000000000, 9999999999))
            case "RANDOM_EMAIL":
                data[key] = ''.join(random.choices(string.ascii_letters + string.digits, k=8)) + "@test.ru"
            case "RANDOM_USERNAME":
                data[key] = 'username_' + ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return json.dumps(data)
