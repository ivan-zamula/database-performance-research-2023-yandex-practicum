# Тестирование производительности базы данных Vertica

## DEPLOY
```To work with Vertica
1. Install library: pip install vertica-python
2. Run docker image: docker run -p 5433:5433 jbfavre/vertica:latest 
By default connection settings:
connection_info = {
    'host': '127.0.0.1',
    'port': 5433,
    'user': 'dbadmin',
    'password': '',
    'database': 'docker',
    'autocommit': True,
}
```


## Результаты тестирования

### 10 000 записей
>insert_n_rows 3.5113564829953248
> 
>select 53.47355746199901

### 100 000 записей
> insert_n_rows 113.39303540000401
>
>select 471.92345036800543
___
0 - 100_000 записей
> insert_n_rows 8.887385299000016
insert_n_rows 55.6763745069984
insert_n_rows 54.154789288004395
insert_n_rows 59.35205978699378
insert_n_rows 53.69366186399566
insert_n_rows 86.90965074500127
insert_n_rows 94.24409165100224
insert_n_rows 69.29766119499982
insert_n_rows 55.188060713000596
> 
> insert_butch_by_n_rows 537.4039882840007
> 
> select 53.44767376600066
___
100_000 - 200_000
> insert_n_rows 3.823438632993202
insert_n_rows 59.79938667600072
insert_n_rows 55.76105885799916
insert_n_rows 57.245263163000345
insert_n_rows 82.3048320520029
insert_n_rows 67.45234399299807
insert_n_rows 69.80424502899405
insert_n_rows 61.072100027995475
insert_n_rows 60.13205049499811
> 
> insert_butch_by_n_rows 517.3949923120017
> 
> select 64.12203759299882
___
200_000 - 300_000 
> insert_n_rows 65.23101360400324
insert_n_rows 128.55550577199756
insert_n_rows 113.24413843599905
insert_n_rows 90.15780221099703
insert_n_rows 69.36354325999855
insert_n_rows 76.89695590900374
insert_n_rows 67.81901307799853
insert_n_rows 104.33090728600655
insert_n_rows 74.675208198998
> 
> insert_butch_by_n_rows 790.274850572001
> 
> select 93.32209145300294
___
300_000 - 400_000
> insert_n_rows 7.1747932199941715
insert_n_rows 129.35929746900365
insert_n_rows 131.34591577500396
insert_n_rows 127.42202372400061
insert_n_rows 129.59908447899943
insert_n_rows 82.04253431500547
insert_n_rows 64.7671449430054
insert_n_rows 74.10559338099847
insert_n_rows 100.5019293430014
> insert_butch_by_n_rows 846.3997208260043
> select 86.00308687999495
___
400000 - 500000
> insert_n_rows 1.968236163003894
insert_n_rows 58.91851174800104
insert_n_rows 50.96419819300354
insert_n_rows 55.618352290002804
insert_n_rows 54.448488098998496
insert_n_rows 56.25175005700294
insert_n_rows 49.50273802900483
insert_n_rows 52.70439551400341
insert_n_rows 51.14450057900103
> 
> insert_butch_by_n_rows 431.5213716090002
> 
> select 49.57446510400041
___
500000 - 600000
> insert_n_rows 4.502843854003004
insert_n_rows 54.2287915650013
insert_n_rows 51.940028842000174
insert_n_rows 49.95928593399731
insert_n_rows 50.74299574899487
insert_n_rows 50.392318427002465
insert_n_rows 50.76418311500311
insert_n_rows 52.3198518470017
insert_n_rows 49.846679262002
> 
> insert_butch_by_n_rows 414.6971933879977
> 
> select 50.71871967500192
___
600000 - 700000
> insert_n_rows 4.8520554620045
insert_n_rows 51.86871541199798
insert_n_rows 50.13139016400237
insert_n_rows 51.301233989004686
insert_n_rows 51.147613241002546
insert_n_rows 50.1500699169992
insert_n_rows 50.82794056399871
insert_n_rows 51.49861413900362
insert_n_rows 50.10996976800379
> 
> insert_butch_by_n_rows 411.8878194019999
> 
> select 50.95093275800173
___
700000 - 800000
> insert_n_rows 5.252270098004374
insert_n_rows 50.812182433001
insert_n_rows 50.68407458800357
insert_n_rows 52.18302785600099
insert_n_rows 53.323438519000774
insert_n_rows 54.89147739199689
insert_n_rows 53.94426258000021
insert_n_rows 54.58701677600038
insert_n_rows 55.40059378500155
> 
> insert_butch_by_n_rows 431.0785890249972
> 
> select 53.467933667998295
___
800000 - 900000
> insert_n_rows 5.915815972999553
insert_n_rows 52.26848897000309
insert_n_rows 56.09174362500198
insert_n_rows 51.923684762004996
insert_n_rows 50.076928511000006
insert_n_rows 57.30876744999841
insert_n_rows 56.482299196002714
insert_n_rows 52.01231204400392
insert_n_rows 52.97355129500647
> 
> insert_butch_by_n_rows 435.0538110030029
> 
> select 51.51999442200031
___
900000 - 1000000
> insert_n_rows 6.258530869999959
insert_n_rows 51.126611790001334
insert_n_rows 49.9615403469943
insert_n_rows 53.43478814000264
insert_n_rows 55.50610896800208
insert_n_rows 50.45609855999646
insert_n_rows 50.3466546119962
insert_n_rows 55.1562531189993
insert_n_rows 51.47771695200208
> 
> insert_butch_by_n_rows 423.7245225890001
> 
> select 51.633177989002434
___
