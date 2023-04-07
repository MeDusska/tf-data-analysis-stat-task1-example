import pandas as pd
import numpy as np


chat_id = 493548023 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    left = x.max()
    right = x.max()/((1-p)**(1/len(x)))
    return left, right
