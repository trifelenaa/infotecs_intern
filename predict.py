# -*- coding: utf-8 -*-
"""predict

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ea06OHBdA31i1v0dpBNY5H6q7GNR7pYh
"""

import pandas as pd
import joblib

# чтение данных из файлов
test_data = pd.read_csv('test.tsv', sep='\t')

# загрузка модели и векторизатора из файлов
model_boost = joblib.load('model_boost.joblib')
vectorizer = joblib.load('vectorizer.joblib')

# для лучшей модели выполним предсказание на тестовой выборке и запись результатов в файл prediction.txt
X_pred = vectorizer.transform(test_data['libs'])

test_pred = model_boost.predict(X_pred)

with open('prediction.txt', 'w') as f:
    f.write('prediction\n')
    for p in test_pred:
        f.write(f'{p}\n')

with open('explain.txt', 'w') as f:
    for i, pred in enumerate(test_pred):
        if pred == 1:
            f.write(f'File {i}: содержит зловредный код\n')
        else:
            f.write(f'\n')