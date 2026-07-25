# Library Management

Простая система управления библиотекой на Python: книги, каталог, выдача и возврат.

Подходит для изучения ООП, отладки в Cursor и написания unit-тестов.

## Возможности

- создание книг (`Book`)
- хранение книг в библиотеке (`Library`)
- добавление книг в каталог
- просмотр списка книг
- выдача книги читателю
- возврат книги в библиотеку
- поиск книги по названию

## Структура проекта

```
library_management/
├── book.py              # класс Book
├── library.py           # класс Library
├── main.py              # точка входа, демо-сценарий
├── test_book.py         # тесты для Book
├── test_library.py      # тесты для Library
├── README.md
└── .vscode/
    └── launch.json      # конфигурации отладки Cursor / VS Code
```

## Требования

- Python 3.10+ (подойдёт и более новая версия)
- Cursor (или VS Code) с расширением **Python**  
  (для отладки используется `debugpy`, оно обычно ставится вместе с расширением)

Дополнительные библиотеки не нужны: проект использует только стандартную библиотеку Python.

## Как запустить программу

Из корня проекта:

```bash
python main.py
```

или:

```bash
python3 main.py
```

В терминале появится список книг, затем сообщения о выдаче и возврате.

## Как запустить тесты

Из корня проекта:

```bash
python -m unittest discover -v
```

Запуск одного файла:

```bash
python -m unittest test_book.py -v
python -m unittest test_library.py -v
```

Запуск одного теста:

```bash
python -m unittest test_library.TestLibrary.test_borrow_book_makes_book_unavailable -v
```

## Отладка в Cursor

### 1. Breakpoint (точка останова)

1. Открой нужный файл, например `main.py` или `library.py`.
2. Кликни слева от номера строки — появится красная точка.
3. Хорошие места для старта:
   - `main.py` — создание библиотеки
   - `library.py` → `add_book`
   - `library.py` → `borrow_book`
   - `library.py` → `return_book`

Когда выполнение дойдёт до breakpoint, выполнение остановится.

### 2. Запуск отладки

Есть несколько способов:

**Способ A — текущий файл**

1. Открой `main.py`.
2. Нажми `F5` или кнопку **Run and Debug**.
3. Выбери конфигурацию `Python Debugger: Current File`
   (или `Python: Main`, если добавишь конфиг ниже).

**Способ B — через панель**

1. Открой вкладку **Run and Debug** (иконка «play with bug»).
2. Выбери конфигурацию в выпадающем списке.
3. Нажми зелёную кнопку Start Debugging.

**Способ C — без launch.json**

1. Открой `main.py`.
2. Справа сверху нажми на стрелку рядом с Run.
3. Выбери **Python Debugger: Debug Python File**.

### 3. Панель отладки: что смотреть

После остановки на breakpoint:

| Панель | Зачем нужна |
|---|---|
| **Variables** | текущие значения переменных (`self`, `book`, `title`, `library_1.books`) |
| **Watch** | выражение, за которым хочешь следить, например `len(library_1.books)` |
| **Call Stack** | цепочка вызовов: `main` → `borrow_book` → ... |
| **Breakpoints** | список всех точек останова |

Полезно смотреть:

- `self` — текущий объект (`Book` или `Library`)
- `self.books` — список книг в библиотеке
- `book.is_available` — доступна ли книга

### 4. Кнопки управления

| Действие | Обычно | Что делает |
|---|---|---|
| Continue | `F5` | продолжить до следующего breakpoint |
| Step Over | `F10` | выполнить текущую строку, не заходя внутрь функции |
| Step Into | `F11` | зайти внутрь вызываемой функции/метода |
| Step Out | `Shift+F11` | выйти из текущей функции на уровень выше |
| Restart | | перезапустить отладку |
| Stop | `Shift+F5` | остановить отладку |

**Практика для новичка:**

1. Breakpoint на `library_1.borrow_book("1984")` в `main.py`.
2. `F11` (Step Into) — зайдёшь в `borrow_book`.
3. `F10` (Step Over) — пройдёшь цикл построчно.
4. В Variables смотри, как меняется `book.is_available`.

### 5. Debug Console

Во время паузы можно выполнять Python-выражения в **Debug Console**, например:

```python
library_1.books
len(library_1.books)
self.book_1984.is_available
```

Это удобно, чтобы проверить состояние без изменения кода.

## Как правильно создать debug-конфиг

Конфигурации лежат в `.vscode/launch.json`.

### Минимальный рабочий вариант

Уже есть конфиг «текущий файл»:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    }
  ]
}
```

Он запускает **тот файл, который сейчас открыт**.  
Если открыт `library.py`, отладка этого файла как скрипта обычно бесполезна — запускай `main.py` или тесты.

### Конфиги этого проекта

В `.vscode/launch.json` уже добавлены рабочие конфигурации:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Main",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/main.py",
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}"
    },
    {
      "name": "Python: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}"
    },
    {
      "name": "Python: All Tests",
      "type": "debugpy",
      "request": "launch",
      "module": "unittest",
      "args": ["discover", "-v"],
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}"
    },
    {
      "name": "Python: Current Test File",
      "type": "debugpy",
      "request": "launch",
      "module": "unittest",
      "args": ["${file}", "-v"],
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}"
    }
  ]
}
```

### Что означают поля

| Поле | Смысл |
|---|---|
| `name` | имя в списке Run and Debug |
| `type` | `"debugpy"` — отладчик Python |
| `request` | `"launch"` — запустить программу самим Cursor |
| `program` | путь к `.py` файлу |
| `module` | запуск модуля (`unittest`), вместо `program` |
| `args` | аргументы командной строки |
| `console` | куда выводить print: лучше `integratedTerminal` |
| `cwd` | рабочая папка; для этого проекта — корень репозитория |

### Как создать конфиг через UI

1. Открой **Run and Debug**.
2. Нажми **create a launch.json file**.
3. Выбери **Python Debugger**.
4. Выбери шаблон:
   - **Python File** — текущий файл
   - **Module** — для `unittest`
5. Отредактируй JSON под проект (см. пример выше).

### Частые ошибки

1. **Отлаживаешь не тот файл**  
   Открыт `book.py`, а запускаешь Current File — программа почти сразу завершится, потому что там нет `main`.  
   Решение: используй конфиг `Python: Main`.

2. **ImportError: No module named 'book'**  
   Запуск не из корня проекта.  
   Решение: в конфиге укажи `"cwd": "${workspaceFolder}"`.

3. **Breakpoint серый / не срабатывает**  
   Код не доходит до этой строки, или отладка запущена для другого файла/теста.

4. **Нет debugpy / не стартует debugger**  
   Установи расширение Python в Cursor и повтори запуск.

## Классы проекта (кратко)

### `Book`

- `title` — название
- `author` — автор
- `is_available` — доступна ли книга
- `__str__` — красивый вывод книги

### `Library`

- `add_book(book)` — добавить книгу
- `display_books()` — напечатать все книги
- `borrow_book(title)` — выдать книгу
- `return_book(title)` — вернуть книгу
- `get_book(title)` — найти книгу или вернуть `None`

## Быстрый чеклист для ученика

1. Запусти `python main.py`.
2. Запусти тесты: `python -m unittest discover -v`.
3. Поставь breakpoint в `borrow_book`.
4. Запусти `Python: Main` через `F5`.
5. Пройди код через Step Into / Step Over.
6. В Variables посмотри `self.books` и `is_available`.
