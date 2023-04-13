# Тестирование производительности базы данных Mongo

## DEPLOY
1. Выполнить команду docker compose up --no-start
2. Запустить все контейнеры, кроме backend
3. Запустить init-cluster.sh
4. Запустить контейнер backend (результаты тестов выводятся в контейнере backend)


## Результаты тестирования

### Single mongo instance:
```text
docs count: 100, batch size: 10
bulk_insert 0.04978357600066374
bulk_unordered_insert 0.04465204200005246
bulk_write_concern 0.04347370000050432
read_all 4.905400055577047e-05
get_avg_score 0.0008946050002123229

docs count: 100, batch size: 100
bulk_insert 0.028978155000004335
bulk_unordered_insert 0.028250100999684946
bulk_write_concern 0.031030692999593157
read_all 4.9930999921343755e-05
get_avg_score 0.0014616190001106588

docs count: 100, batch size: 1000
bulk_insert 0.05897014899983333
bulk_unordered_insert 0.06205104600030609
bulk_write_concern 0.040990438999870094
read_all 4.236000040691579e-05
get_avg_score 0.0015299730002880096

docs count: 1000, batch size: 10
bulk_insert 0.0972697839997636
bulk_unordered_insert 0.10546834399974614
bulk_write_concern 0.09948095799973089
read_all 3.847800053335959e-05
get_avg_score 0.0014748159992450383

docs count: 1000, batch size: 100
bulk_insert 0.05331043400019553
bulk_unordered_insert 0.05741857799966965
bulk_write_concern 0.054186903000299935
read_all 4.038499992020661e-05
get_avg_score 0.0027574650002861745

docs count: 1000, batch size: 1000
bulk_insert 0.06731873300032021
bulk_unordered_insert 0.05514233099984267
bulk_write_concern 0.048217821000434924
read_all 4.9244999900111e-05
get_avg_score 0.0018608359996505897

docs count: 10000, batch size: 10
bulk_insert 0.6544244340002479
bulk_unordered_insert 0.7532839579998836
bulk_write_concern 0.6728555660001803
read_all 3.59840005330625e-05
get_avg_score 0.006582198999240063

docs count: 10000, batch size: 100
bulk_insert 0.2096512520001852
bulk_unordered_insert 0.22193686299942783
bulk_write_concern 0.1934668639996744
read_all 4.5991999286343344e-05
get_avg_score 0.006736576000548666

docs count: 10000, batch size: 1000
bulk_insert 0.16058990500005166
bulk_unordered_insert 0.16700657599994884
bulk_write_concern 0.15497382700050366
read_all 3.5322000258020125e-05
get_avg_score 0.006396441000106279

docs count: 100000, batch size: 10
bulk_insert 7.687204212000324
bulk_unordered_insert 6.495524982000461
bulk_write_concern 6.590235575999941
read_all 5.042500015406404e-05
get_avg_score 0.059786534000522806

docs count: 100000, batch size: 100
bulk_insert 1.7593236089996935
bulk_unordered_insert 1.7737560709992977
bulk_write_concern 1.731519188000675
read_all 2.9241999982332345e-05
get_avg_score 0.059795706000841164

docs count: 100000, batch size: 1000
bulk_insert 1.2018092830003297
bulk_unordered_insert 1.2258350349993634
bulk_write_concern 1.2852073190006195
read_all 4.3076999645563774e-05
get_avg_score 0.0572379479999654
```
### Mongo cluster:
```text
docs count: 100, batch size: 10
bulk_insert 0.05503181200037943
bulk_unordered_insert 0.043676174999745854
bulk_write_concern 0.055196137000166345
read_all 2.278300053148996e-05
get_avg_score 0.0007837100001779618

docs count: 100, batch size: 100
bulk_insert 0.040685742999812646
bulk_unordered_insert 0.03891780899994046
bulk_write_concern 0.04228298299949529
read_all 3.5820000448438805e-05
get_avg_score 0.001116602000365674

docs count: 100, batch size: 1000
bulk_insert 0.0525726730002134
bulk_unordered_insert 0.04416816499997367
bulk_write_concern 0.062446382000416634
read_all 3.427500087127555e-05
get_avg_score 0.0015714979999756906

docs count: 1000, batch size: 10
bulk_insert 0.10592576399994869
bulk_unordered_insert 0.0972269439998854
bulk_write_concern 0.0959397260003243
read_all 2.515399955882458e-05
get_avg_score 0.0021869629999855533

docs count: 1000, batch size: 100
bulk_insert 0.05663987600019027
bulk_unordered_insert 0.057002021999323915
bulk_write_concern 0.05702006599949527
read_all 2.3727000552753452e-05
get_avg_score 0.0014273500000854256

docs count: 1000, batch size: 1000
bulk_insert 0.04675262000000657
bulk_unordered_insert 0.040585590000773664
bulk_write_concern 0.04688350200012792
read_all 4.114700004720362e-05
get_avg_score 0.0023449469999832218

docs count: 10000, batch size: 10
bulk_insert 0.6880112409999128
bulk_unordered_insert 0.670590438000545
bulk_write_concern 0.6804181120005524
read_all 2.8810000003431924e-05
get_avg_score 0.00778042000001733

docs count: 10000, batch size: 100
bulk_insert 0.1987592269997549
bulk_unordered_insert 0.20074776399997063
bulk_write_concern 0.21190638200005196
read_all 3.0764000257477164e-05
get_avg_score 0.007411433999550354

docs count: 10000, batch size: 1000
bulk_insert 0.15613100199971086
bulk_unordered_insert 0.16770918699967297
bulk_write_concern 0.15644198300014978
read_all 2.926500019384548e-05
get_avg_score 0.006584132000170939

docs count: 100000, batch size: 10
bulk_insert 6.174200604000362
bulk_unordered_insert 6.265957055999934
bulk_write_concern 6.2584827760001644
read_all 2.712199966481421e-05
get_avg_score 0.061497689000134415

docs count: 100000, batch size: 100
bulk_insert 1.7073595649999334
bulk_unordered_insert 1.7430407599995306
bulk_write_concern 1.7471364000002723
read_all 2.3937000150908716e-05
get_avg_score 0.06374583699926006

docs count: 100000, batch size: 1000
bulk_insert 1.255048046000411
bulk_unordered_insert 1.529100324000865
bulk_write_concern 1.4567914149993157
read_all 3.878600000462029e-05
get_avg_score 0.08331367899972975
```