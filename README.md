![CI](https://github.com/arosyri/config-lib/actions/workflows/ci.yml/badge.svg)
# ConfigLib

**ConfigLib** — це Python-бібліотека для роботи з конфігураційними файлами у форматах **YAML** та **JSON**, з підтримкою валідації на основі **JSON Schema**.

---

## Можливості

- Завантаження YAML або JSON конфігурацій
- Валідація даних згідно з JSON-схемою
- Обробка помилок при завантаженні та перевірці
- Unit-тести для всіх компонентів
- Автоматичне CI на GitHub Actions

---

## Приклад структури файлів

### config.yaml

```yaml
host: localhost
port: 8080
```
### schema.json
````json
{
  "type": "object",
  "properties": {
    "host": {"type": "string"},
    "port": {"type": "integer"}
  },
  "required": ["host", "port"]
}
````
---
##  Як запустити

### 1. Встановити залежності
````bash
pip install -r requirements.txt
````
###  2. Використати бібліотеку
````python
from configlib import parser, schema, validator

cfg = parser.load_config("config.yaml")
sch = schema.load_schema("schema.json")
validator.validate_config(cfg, sch)
````
### 3. Запустити тести
````bash
PYTHONPATH=. pytest
````
##  CI / GitHub Actions
Автоматичний запуск `pytest` при кожному push та pull request.

## Design Document
Документ з архітектурою, плануванням та описом знаходиться у гілці main, назва - ConfigLib Design Document

## Автор

Каріна Корчова(IM-34)

Навчальний проєкт — Лабораторна робота №4

Методології та технології розробки ПЗ
