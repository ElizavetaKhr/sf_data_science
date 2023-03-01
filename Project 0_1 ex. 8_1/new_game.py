import numpy as np
def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число от 1 до 100

    Returns:
        int: Число попыток
    """
    count = 0 #начальное количество попыток
    first_number = 1 #от
    second_number = 101 #до
    midle_number = 1 #переменная для среднего значения между загаданным числом
    
    while number != midle_number:
        count += 1
        midle_number = (first_number + second_number) // 2  #формула среднего значения
        if midle_number > number:
            second_number = midle_number 
        elif midle_number < number:
            first_number = midle_number
        else:
            number == midle_number
            break #выход из цикла, если угадали
    return count

def score_game(random_predict) -> int:
    """За какое количество в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] #список для сохранения количества попыток
    np.random.seed(1) #фиксируем seed для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) #загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls)) #находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')

# RUN
if __name__ == '__main__':
    score_game(random_predict)

