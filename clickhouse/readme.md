# Исследование затрачиваемого времени на добавление и считывание записей в ClickHouse

## DEPLOY
> Запустить docker и проверить его статус `docker info` \
> Развернуть нужный docker-compose командой \
>   ` docker-compose -f docker-compose.performance.yml up -d --build` \
>   ` docker-compose -f docker-compose.use_case.yml up -d --build` \
> Результаты в контейнере tests, либо в интерактивном формате \
> Собрать образ и запустить контейнеры кластера ClickHouse. \
> При необходимости, запустить в интерактивном режиме нужный тест.

## Исследования производительности
- [Research](results/performance.md)

## Исследования пользовательских сценариев
- [Research](results/use_case.md)