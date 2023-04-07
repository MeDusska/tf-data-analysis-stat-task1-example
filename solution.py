import pandas as pd
import numpy as np


chat_id = 493548023 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    new_array = np.exp(x+31)
    return new_array.mean() # Ваш ответ
