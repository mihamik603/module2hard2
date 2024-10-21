import random
def generate_pairs(n):
    pairs = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                pair = (i, j)
                if pair not in pairs and (j, i) not in pairs:
                    pairs.append(pair)
    return pairs


def generate_password(num):
    pairs = generate_pairs(num)
    result = ""
    for pair in pairs:
        pair_string = f"{pair[0]}{pair[1]}"
        sum_of_pair = sum(pair)
        if num % sum_of_pair == 0:
            result += pair_string

    return result


random_number = random.randint(3, 20)
print(f"Сгенерированное число: {random_number}")

password = generate_password(random_number)
print(f"Сгенерированный пароль: {password}")
