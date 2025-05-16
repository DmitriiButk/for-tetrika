## Описание задач

- **task1** — Декоратор строгой проверки типов аргументов функции.
- **task2** — Работа с коллекциями и сохранение данных в CSV.
- **task3** — Подсчёт времени одновременного присутствия ученика и преподавателя на уроке.

## Запуск
1. Клонируйте репозиторий и перейдите в директорию проекта:
    ```bash
    git clone https://github.com/DmitriiButk/for-tetrika.git
    cd for-tetrika
    ```

2. Создайте и активируйте виртуальное окружение:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Запустите тесты командой:
    ```bash
    python -m unittest discover tests 
    ```