# thi-labs

Учебный FastAPI-сервис. `GET /health` возвращает `{"status": "OK"}`.

## Локальная проверка

Python 3.12 и uv:

```bash
uv sync --locked
uv run --frozen ruff check app tests
uv run --frozen pytest
uv run --frozen python -m py_compile app/*.py
```

Запуск приложения: `uv run uvicorn app.main:app --reload`.

## CI

GitHub Actions запускает один job на Ubuntu при push в `main` и
`lab1-ci-setup`, а также при создании и обновлении PR в `main`.
Шаги: checkout, Python 3.12 с кэшем pip, установка зависимостей,
Ruff, pytest с покрытием, проверка компиляции Python.
Порог покрытия приложения - 80%; при ошибке build пропускается.
Отчеты покрытия и тестов сохраняются на 14 дней даже при падении тестов.

`uv.lock` фиксирует зависимости проекта. Для CI используется его экспорт
`requirements-ci.txt` с точными версиями и SHA-256, который pip устанавливает
с `--require-hashes`. После изменения зависимостей обновите экспорт:

```bash
uv export --frozen --all-groups --no-emit-project --output-file requirements-ci.txt
```

Ключ кэша зависит от `requirements-ci.txt`, ОС и версии Python.
Build проверяет синтаксис модулей сервиса: этому небольшому Python-приложению
не нужна отдельная сборка фронтенда или Docker-образа.

Материалы лабораторной работы и отчет находятся в `reports/lab1/`.
