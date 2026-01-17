# Быстрый старт

## 1) Копирование репозитория

```bash
git clone https://github.com/zteewt/Video-prompt-generator.git
```

## 2) Создание виртуального окружения (Linux)
```bash
python3 -m venv .venv
```

## 3) Установка зависимостей
```bash
pip install -r requirements.txt
```


*В папке /docs по желанию можете заменить файл document.docx с абзацами для промптинга и промпт с инструкциями prompt.txt для генерации своих кастомных промптов*


## 4) Запуск файла async_csv_table_create.py

После этого в папке /docs перезапишется таблица с промптами prompts_table.csv



Таблица prompt_tables.csv состоит из полей `id`- нумерация строк, `paragraph` - исходный абзац, `response` - сгенерированный промпт под этот абзац.



## (P.s. также в репозитории присутствует синхронная версия программы для ознакомления)
