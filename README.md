# Развертывание приложения

Клонируем репозиторий и заходим в его корень:
```shell
git clone https://github.com/quantum73/quiz.git
cd quiz/
```

Затем, собираем контейнеры с помощью команды:
```shell
docker-compose up -d
```

Если контейнеры установятся корректно, то вы должны увидеть в завершении приблизительно такой вывод:
```shell
...
...
Creating quiz_db_1 ... done
Creating quiz_app_1 ... done
```

Убедимся, что все контейнеры установились и запустились корректно командой:
```shell
docker ps
```

В случае текущего приложения, всё установилось и работает корректно, если в выводе находятся 2 контейнера:
```shell
CONTAINER ID   IMAGE      COMMAND                  CREATED          STATUS          PORTS                                                                                                                 NAMES
f3453293dc98   quiz_app   "/home/api/entrypoin…"   25 seconds ago   Up 24 seconds   0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp, 0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   quiz_app_1
e2462fc6ebb3   postgres   "docker-entrypoint.s…"   25 seconds ago   Up 25 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp                                                                             quiz_db_1
```

Теперь можно отправлять запросы по адресу `http://127.0.0.1:5000/questions/`. <br>
Запросы можно делать через утилиты `Postman` или `curl`.

Рассмотрим пример корректного запроса через `curl`:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"questions_num":3}' http://127.0.0.1:5000/questions/
```

Возвращаемый ответ - последний сохранившийся вопрос:
```shell
{"answer":"\"Wuthering Heights\"","created_at":"2014-02-11 23:10:13.366000","id":"3","question":"\"I must go, Cathy\", said Heathcliff, seeking to extricate himself from his companion's arms in this novel","question_id":"40610"}
```

Также рассмотрим примеры некорректных запросов. <br>
Например, передадим число, меньше 1:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"questions_num":-1}' http://127.0.0.1:5000/questions/

[{"loc":["questions_num"],"msg":"value must be greater then 0","type":"assertion_error"}]
```
Или передадим строку, вместо числа:
```shell
curl -X POST -H "Content-Type: application/json" -d '{"questions_num":"some string"}' http://127.0.0.1:5000/questions/

[{"loc":["questions_num"],"msg":"value is not a valid integer","type":"type_error.integer"}]
```