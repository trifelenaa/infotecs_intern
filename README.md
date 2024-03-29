## Задание:

Разработать систему машинного обучения, которая по списку статически импортируемых библиотек exe файла предсказывает, является ли этот файл зловредным.

- Для выполнения задания предоставляются три выборки: обучающая, валидационная и проверочная. Выборки представлены в виде tsv файлов с тремя колонками – *is_virus* – является ли файл зловредным: *1=да*, *0=нет*; *filename* – имя файла для ознакомления; *libs* – через запятую перечисление библиотек, статически импортируемых этим файлом (мы использовали библиотеку LIEF для получения списка).

- На обучающей выборке – `train.tsv` – следует обучать модель машинного обучения.

- На валидационной выборке – `val.tsv` – требуется подсчитать, насколько хорошо модель справляется с файлами, которые она не видела при обучении. Характеристики требуется записать в текстовый файл `validation.txt` со следующим содержанием (изменив значения на ваши):
```
True positive: 2
False positive: 20
False negative: 18
True negative: 60
Accuracy: 0.6200
Precision: 0.0909
Recall: 0.1000
F1: 0.0952
```
Проверочная выборка – `test.tsv` – содержит только колонку *libs*. Для проверочной выборки требуется создать файл `prediction.txt`, в котором для каждой строки файла проверочной выборки будет содержаться один символ: либо 1 если модель предсказывает этот файл как зловредный, либо 0 иначе. Первая строка файла, соответствующая заголовку проверочной выборки должна быть “prediction”:
```
prediction
0
0
1
( … много строк пропущено … )
0
1
0
```
## Требования:

В качестве решения принимается: скрипты на Python 3.x, файлы `validation.txt`, `prediction.txt`, и, опционально `explain.txt`. Скрипты должен создавать такие же файлы в результате работы.

Должно присутствовать три скрипта: `train.py`, выполняющий обучение из обучающей выборки и записывающий модель в файл, `validate.py`, читающий модель из файла и создающий файл `validation.txt`, и `predict.py`, читающий модель из файла и создающий файлы `prediction.txt` и опционально, `explain.txt`. Каждый из трех должен запускаться без аргументов командной строки.

