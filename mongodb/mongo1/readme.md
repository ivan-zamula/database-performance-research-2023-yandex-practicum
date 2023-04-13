# Тестирование производительности базы данных Mongo

## DEPLOY
2. Выполнить команду docker compose up \
   (backend - environment - recs_num - количество записей при тестировании записи/чтения)
3. Результаты тестов выводятся в контейнере backend


## Результаты тестирования

### 100 000

#### Single mongo instance:
```text
bulk_insert 1.3749485540001842
bulk_unordered_insert 1.4891654470002322
bulk_write_concern 1.6412090089997946
read_all 0.00010384799998064409
```
#### Mongo replica set:
```text
bulk_insert 3.0075475319999896
bulk_unordered_insert 2.0275530860003528
bulk_write_concern 1.8864383339996493
read_all 7.036899978629663e-05
```

### 1 000 000 

#### Single mongo instance:
```text
bulk_insert 14.372071119999873
bulk_unordered_insert 16.368305536000207
bulk_write_concern 15.467667333999998
read_all 6.862300006105215e-05
```
#### Mongo replica set:
```text
bulk_insert 27.822392084999592
bulk_unordered_insert 25.132520010999997
bulk_write_concern 2.4982203699996717
read_all 8.618800029580598e-05
```

### 10 000 000 

#### Single mongo instance:
```text
bulk_insert 125.95700847999996
bulk_unordered_insert 130.93833370100003
 bulk_write_concern 132.13751623300004
read_all 6.14379999888115e-05
```
#### Mongo replica set:
```text
bulk_insert 193.41584042099987
bulk_unordered_insert 202.761051812
bulk_write_concern 2.462650659000019
read_all 0.012231391000113945
```
