# Результаты тестирования пользовательских сценариев

## SCORE: Пустая база
### SCORE: Pattern: INSERT + SELECT DEFAULT NO DELAY
> transaction = 1000, documents count = 10000, time = 0.02300889999969513 \
> transaction = 1000, documents count = 100000, time = 0.21794859999954497 
> 
> transaction = 5000, documents count = 10000, time = 0.02212229999986448 \
> transaction = 5000, documents count = 100000, time = 0.2179684000002453 

### SCORE: Pattern: INSERT + SELECT AVERAGE NO DELAY
> transaction = 1000, documents count = 10000, time = 0.017910700000356883 \
> transaction = 1000, documents count = 100000, time = 0.17355370000041148 
> 
> transaction = 5000, documents count = 10000, time = 0.017705600000226696 \
> transaction = 5000, documents count = 100000, time = 0.1805822000005719 

### SCORE: Pattern: ONLY SELECT AVERAGE DELAYED
> transaction = 1000, documents count = 10000, time = 0.0016661999998177635 \
> transaction = 1000, documents count = 100000, time = 0.0034406000004310044 
> 
> transaction = 5000, documents count = 10000, time = 0.0019083000006503426 \
> transaction = 5000, documents count = 100000, time = 0.0037413999998534564 

## SCORE: Полная база (1 000 000 документов)
### SCORE: Pattern: INSERT + SELECT DEFAULT NO DELAY
> transaction = 1000, documents count = 10000, time = 0.44465500000023894 \
> transaction = 1000, documents count = 100000, time = 0.5466115999997783 
> 
> transaction = 5000, documents count = 10000, time = 0.4031016000008094 \
> transaction = 5000, documents count = 100000, time = 0.5715571999999156 

### SCORE: Pattern: INSERT + SELECT AVERAGE NO DELAY
> transaction = 1000, documents count = 10000, time = 0.021446700000524288 \
> transaction = 1000, documents count = 100000, time = 0.15717339999991964 
> 
> transaction = 5000, documents count = 10000, time = 0.022098899999946298 \
> transaction = 5000, documents count = 100000, time = 0.1496723000000202 

### SCORE: Pattern: ONLY SELECT AVERAGE DELAYED
> transaction = 1000, documents count = 10000, time = 0.010330699999940407 \
> transaction = 1000, documents count = 100000, time = 0.011899499999344698 
> 
> transaction = 5000, documents count = 10000, time = 0.00941919999968377 \
> transaction = 5000, documents count = 100000, time = 0.007649300000593939 


## Прочие данные
- данные тестирования остальных пользовательских кейсов содержится в файле [use_case.log](use_case.log.md):
  - SCORE (AVERAGE)
  - LIKES BY FILM (COUNT)
  - LIKES BY USER (COUNT)
  - BOOKMARKS (COUNT)



## Методика тестирования
> Записываемые документы состоят из 4 полей (id, user_id, movie_id, score). \
> Для генерации использована стандартная функция range возвращающая генератор, \
> который используется для создания генератора-заполнителя. \
> Используемая библиотека ClickHouse_driver. \
> Запись при помощи команды execute('INSERT INTO ... VALUES') принимающей генератор с данными \
> Запись пакетами производилась с предварительно подготовленным сетом. \
> Чтение производится согласно сценарию использования, используется COUNT, AVG().
