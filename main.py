import numpy as np

def game_core_v2(number):
    count = 0

    a = 1
    b = 100
    predict = (a+b)//2
    while number != predict:
        count+=1
        if (b-a)==1:
            if predict == b:
                predict = a
            else:
                predict = b
        elif number > predict:
            a = predict
            predict = (a + b) // 2
        elif number < predict:
            b = predict
            predict = (a + b) // 2
    return(count)

def score_game(game_core):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v2)

