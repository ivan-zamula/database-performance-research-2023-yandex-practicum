# Результаты тестирования производительности

## Результаты замера записи данных в секундах без ограничения транзакции
> Запись 10 000 документов: 0.021612599957734346 \
> Считывание 10 000 документов: 0.011115900008007884

> Запись 100 000 документов: 0.22960770002100617 \
> Считывание 100 000 документов: 0.07159429998137057

> Запись 1 000 000 документов: 2.893171500065364 \
> Считывание 1 000 000 документов: 0.594265199964866

> Запись 10 000 000 документов: 29.673591499915347 \
> Считывание 10 000 000 документов: 6.254016500082798

## Результаты замера записи данных в секундах с ограничением транзакции
### Запись в пустую базу
> transaction = 1000, documents count = 100000, time = 0.34471579999808455 \
> transaction = 1000, documents count = 1000000, time = 4.006833499995992 \
> transaction = 1000, documents count = 10000000, time = 69.62092219999613
> 
> transaction = 5000, documents count = 100000, time = 0.21145959999557817 \
> transaction = 5000, documents count = 1000000, time = 2.8724071999968146 \
> transaction = 5000, documents count = 10000000, time = 69.771090000002
> 
> transaction = 10000, documents count = 100000, time = 0.21145959999557817 \
> transaction = 10000, documents count = 1000000, time = 2.8724071999968146 \
> transaction = 10000, documents count = 10000000, time = 69.771090000002
> 
> transaction = 100000, documents count = 100000, time = 0.23353820000193082 \
> transaction = 100000, documents count = 1000000, time = 2.7555170000050566 \
> transaction = 100000, documents count = 10000000, time = 68.58564060000208

### Запись в полную базу с 10 000 000 записей
> transaction = 1000, documents count = 100000, time = 0.32846380000410136 \
> transaction = 1000, documents count = 1000000, time = 3.5738207000031252 \
> transaction = 1000, documents count = 10000000, time = 64.71034620000137
> 
> transaction = 5000, documents count = 100000, time = 0.2254183999975794 \
> transaction = 5000, documents count = 1000000, time = 2.653934699999809 \
> transaction = 5000, documents count = 10000000, time = 69.12393609999708
> 
> transaction = 10000, documents count = 100000, time = 0.18617160000576405 \
> transaction = 10000, documents count = 1000000, time = 2.5645900999952573 \
> transaction = 10000, documents count = 10000000, time = 69.78025119999802
> 
> transaction = 100000, documents count = 100000, time = 0.21176089999789838 \
> transaction = 100000, documents count = 1000000, time = 2.6424262000000454 \
> transaction = 100000, documents count = 10000000, time = 74.95111380000162

## Методика тестирования
> Записываемые документы состоят из 5 полей (id, user_id, movie_id, timestamp_movie, time). \
> Для генерации использована стандартная функция range возвращающая генератор, \
> который используется для создания генератора-заполнителя. \
> Используемая библиотека ClickHouse_driver. \
> Запись при помощи команды execute('INSERT INTO ... VALUES') принимающей генератор с данными
> Запись пакетами производилась с предварительно подготовленным сетом.
