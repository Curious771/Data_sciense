
import numpy as np 

def random_predict(number:int=1) -> int:
    """_рандомно угадываем число_

    Args:
        number (int, optional): _загаданное число_. Defaults to 1.

    Returns:
        int: _число попыток_
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint (1, 101)
        if number == predict_number:
            break
    return (count)

print(f'Количество попыток:{random_predict()}')

def score_game(random_predict) -> int:
    """_за какое количество попыток в среднем угадываем число_

    Args:
        random_predict (_type_): _функция угадывания_

    Returns:
        int: _dсреднее количетво попыток_
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1)
    random_array = np.random.randint(1, 101, 1000) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) #находим среднее количество попыток
    print(f'Ващ алгоритм в среднем угадывает за {score} попыток')
    return score
score_game(random_predict)
# RUN
if __name__ == '_main_':
    score_game(random_predict)