from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


# установка вебдрайвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# выбор ника
nickname = input("Enter a nickname: ")
URL = f"https://steamcommunity.com/search/users/#text={nickname}"
driver.get(URL)


# списки для таблицы
urls = []
nicknames = []
levels = []
games = []
badges = []



# небольшое ожидание, что бы страница точно прогрузилась и не выполнялся эксепшн
WebDriverWait(driver, 2)

# цикл для парсинга акков на одной странице
for i in range(2, 22):
    # заход на аккаунт
    try:
        # заходим на аккаунт
        button = driver.find_element(By.CSS_SELECTOR, f"div.search_row:nth-child({i}) > div:nth-child(2) > a:nth-child(1)")
        button.click()

        # ссылка на аккаунт
        get_url = driver.current_url
        urls.append(str(get_url))

        # никнейм парс
        nickname = driver.find_element(By.CSS_SELECTOR, ".profile_header_centered_persona > div:nth-child(1) > span:nth-child(1)")
        nicknames.append(nickname.text)

        # проверка скрыт ли профиль
        try:
            WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".profile_private_info")))
            levels.append(" ")
            games.append(" ")
            badges.append(" ")
            print("Профиль скрыт, скип.")
            driver.back()
            continue
        except TimeoutException:
            print("Профиль открыт, продолжаем.")

        # уровень парс
        lvl = driver.find_element(By.CSS_SELECTOR, "div.friendPlayerLevel:nth-child(1) > span:nth-child(1)")
        levels.append(lvl.text)

        # сколько игр
        games_count = driver.find_element(By.CSS_SELECTOR, ".profile_item_links > div:nth-child(1) > a:nth-child(1) > span:nth-child(2)")
        games.append(games_count.text)

        # значки
        badges_count = driver.find_element(By.CSS_SELECTOR, "div.profile_count_link_preview_ctn:nth-child(1) > div:nth-child(1) > a:nth-child(1) > span:nth-child(2)")
        badges.append(badges_count.text)
    except Exception as e:
        print("чёт не получается")
        continue
    driver.back()


driver.quit()


# cохранение в pandas  и запись в csv
df = pd.DataFrame({'URL': urls,
                   'NICKNAME': nicknames,
                   'LVL': levels,
                   'GAMES': games,
                   'BADGES': badges,
                   })
df.to_csv("steam_data.csv", index=False, sep=';')
