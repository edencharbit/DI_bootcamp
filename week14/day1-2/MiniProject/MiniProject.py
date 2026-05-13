# import pandas as pd
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import chromedriver_autoinstaller
# import time
#
# # --- INITIALISATION ---
#
# chromedriver_autoinstaller.install()
#
# # Options pour que la fenêtre ne se ferme pas tout de suite si tu veux voir
# options = webdriver.ChromeOptions()
#
# driver = webdriver.Chrome(options=options)
#
# url = "https://www.inmotionhosting.com/shared-hosting"
#
# try:
#     # STEP 1: FETCH —
#     print(f"Chargement de la page : {url}...")
#     driver.get(url)
#
#     time.sleep(5)
#     html_content = driver.page_source
#
#     # STEP 2: PARSE —
#     soup = BeautifulSoup(html_content, 'html.parser')
#
#     # STEP 3: EXTRACT —
#     # On cible les cartes de produits (InMotion utilise souvent 'p-card')
#     plans = soup.find_all('div', class_='p-card')
#
#     extracted_data = []
#
#     for plan in plans:
#         name_tag = plan.find('h3')
#         price_tag = plan.find('span', class_='price')
#
#         if name_tag:
#             name = name_tag.get_text(strip=True)
#             price = price_tag.get_text(strip=True) if price_tag else "N/A"
#
#             extracted_data.append({
#                 "Plan Name": name,
#                 "Price": price
#             })
#
#
#     df = pd.DataFrame(extracted_data)
#
#     print("\n--- Données récoltées ---")
#     print(df)
#
#     # Sauvegarde en CSV pour ton portfolio
#     df.to_csv('inmotion_results.csv', index=False, encoding='utf-8')
#     print("\nFichier 'inmotion_results.csv' créé avec succès.")
#
# finally:
#     # On ferme le navigateur proprement
#     driver.quit()

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import chromedriver_autoinstaller
import time

# 1. Init
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

url = "https://www.inmotionhosting.com/shared-hosting"

try:
    driver.get(url)

    print("Attente du chargement des éléments...")
    time.sleep(8)

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    # STEP 3: EXTRACT
    extracted_data = []


    plans = soup.find_all('h3')

    for plan in plans:
        name = plan.get_text(strip=True)

        parent = plan.find_parent()
        price_tag = parent.find('span', class_='price') if parent else None

        if not price_tag and parent:
            price_tag = parent.find(string=lambda text: '$' in text)

        price = price_tag.get_text(strip=True) if hasattr(price_tag,
                                                          'get_text') else str(
            price_tag).strip()

        if any(keyword in name for keyword in
               ['Core', 'Launch', 'Power', 'Pro', 'Shared']):
            extracted_data.append({
                "Plan Name": name,
                "Price": price if price != "None" else "Check on the website"
            })

    # --- FINAL ---
    df = pd.DataFrame(extracted_data)

    if df.empty:
        print(
            "⚠️ Data Frame is empty")
    else:
        print("\n--- Data ---")
        print(df)

finally:
    driver.quit()