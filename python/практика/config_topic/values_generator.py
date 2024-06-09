import numpy as np
from configparser import ConfigParser

# определилил функцию для генерации N случайных чисел
def generate_random_numbers(min_value: int, max_value: int, n_values: int) -> list:
    return list(
        np.random.randint(min_value, max_value, n_values)
    )

if __name__ == "__main__":
    # читаем конфиг
    config = ConfigParser()
    config.read('config.ini')

    # определяем конфигурационные переменные
    MIN_VALUE = int(config['random_numbers']['min_value'])
    MAX_VALUE = int(config['random_numbers']['max_value'])
    N_VALUES = int(config['random_numbers']['n_values'])

    # используем функцию 
    random_numbers = generate_random_numbers(MIN_VALUE, MAX_VALUE, N_VALUES)
    print(random_numbers)