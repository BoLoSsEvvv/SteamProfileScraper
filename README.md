# Steam Profile Scraper

## Описание
Этот скрипт позволяет парсить информацию о пользователях Steam по заданному нику. Для каждого найденного пользователя собирается следующая информация:
- Ссылка на профиль
- Никнейм
- Уровень профиля
- Количество игр
- Количество значков

Результаты сохраняются в CSV-файл `steam_data.csv`.

## Установка и запуск

### Требования
- Python 3.7 или выше
- Google Chrome
- ChromeDriver

### Установка зависимостей
1. Убедитесь, что у вас установлен Python
2. Убедитесь, что у вас установлен Google Chrome.
3. Установите зависимости из файла `requirements.txt`. Выполните следующую команду:
   ```bash
   pip install -r requirements.txt
   ```
