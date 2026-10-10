# Лабораторная работа 1

Итоговый отчет: `Отчет_лабораторная_1.docx` (3 страницы).

Репозиторий: https://github.com/wonderfau1t/thi-labs

Ветка: `lab1-ci-setup`; открытый PR: https://github.com/wonderfau1t/thi-labs/pull/1

## Проверенные запуски

| Состояние | Коммит | PR workflow run | Покрытие | Build |
| --- | --- | --- | --- | --- |
| Первый успешный PR | `4a7ffab` | [38032421563](https://github.com/wonderfau1t/thi-labs/actions/runs/38032421563) | 100% | success |
| Непокрытая функция | `b39bdc3` | [38032487727](https://github.com/wonderfau1t/thi-labs/actions/runs/38032487727) | 60% | skipped |
| После отката | `e57f1a6` | [38032551522](https://github.com/wonderfau1t/thi-labs/actions/runs/38032551522) | 100% | success |

Эксперимент: в `app/main.py` добавлена функция `experimental_score` без теста.
Тест `/health` продолжил проходить, но `pytest-cov` завершил проверку с кодом 1
из-за покрытия ниже 80%. Эксперимент отменен через `git revert`.
Итоговый код приложения и теста совпадает с исходным.

## Доказательства

В `evidence/` сохранены:

- `initial-success.*`, `failed.*`, `restored-success.*`: скриншоты реальных страниц
  GitHub Actions, исходные логи CLI и JSON со статусами job и шагов.
- Одноименные каталоги: скачанные `coverage.xml` и `test-results.xml`.
- `experiment.patch` и `revert.patch`: точные изменения эксперимента и отката.
- `local-tests.txt`: локальный запуск pytest до отправки CI.

На CI XML публикуются даже при неуспешном запуске и хранятся 14 дней.
Локальные копии в этом каталоге остаются в Git независимо от этого срока.
Процент покрытия и сообщение об остановке доступны в текстовых логах;
скриншоты показывают статусы всех этапов.

## Документация

- [Синтаксис workflow и условия шагов](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax)
- [actions/checkout](https://github.com/actions/checkout)
- [setup-python и кэш pip](https://github.com/actions/setup-python#caching-packages-dependencies)
- [actions/upload-artifact](https://github.com/actions/upload-artifact)
- [pytest-cov и порог покрытия](https://pytest-cov.readthedocs.io/en/latest/config.html)
