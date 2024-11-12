# Приложение для заметок

Это простое приложение командной строки для управления заметками с использованием SQLite. Приложение позволяет пользователям создавать, просматривать, удалять, редактировать и искать заметки, хранящиеся в базе данных.

## Требования

- Python 3.x
- SQLite3 (предустановлен с Python)

## Установка

1. Склонируйте этот репозиторий или загрузите файл со скриптом.
2. Убедитесь, что Python установлен, выполнив команду:
```bash
python --version
```
3. Приложение создаст файл базы данных nts.db в той же директории, если он еще не существует.

## Использование

Для запуска приложения перейдите в директорию со скриптом и используйте следующую команду:
```bash
python <имя_скрипта.py> [опции]
```

### Опции

-    -l, --list : Показать все заметки в базе данных.
-    -c, --create : Создать новую заметку с вводом названия и многострочного текста.
-    -d ID, --delete ID : Удалить заметку по её ID.
-    -en ID, --edit-name ID : Изменить название заметки по её ID.
-    -et ID, --edit-text ID : Изменить текст заметки по её ID.
-    -f KEYWORDS, --find KEYWORDS : Искать заметки по ключевым словам. Показывает заметки, содержащие указанные ключевые слова в тексте.

### Примеры использования

- Показать все заметки:
```bash
python <имя_скрипта.py> --list
```

- Создать новую заметку:
```bash
python <имя_скрипта.py> --create
```

- Удалить заметку по ID:
```bash
python <имя_скрипта.py> --delete 1
```

- Изменить название заметки по ID:
```bash
python <имя_скрипта.py> --edit-name 1
```

- Изменить текст заметки по ID:
```bash
python <имя_скрипта.py> --edit-text 1
```

- Найти заметки по ключевым словам:
```bash
python <имя_скрипта.py> --find ключевое_слово1 ключевое_слово2
```
