import time
import pandas as pd
from bs4 import BeautifulSoup
import undetected_chromedriver as uc 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth 

# Launch undetected Chrome browser
options = uc.ChromeOptions()
# options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")

driver = uc.Chrome(version_main=137, options=options)


stealth(driver,
    languages=["en-US", "en"],
    vendor="Google Inc.",
    platform="Win32",
    webgl_vendor="Intel Inc.",
    renderer="Intel Iris OpenGL Engine",
    fix_hairline=True,
)

wait = WebDriverWait(driver, 20)


driver.get("https://starzplay.com/en/faq")
time.sleep(10)


# Wait until navigation tabs are present
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav ul li a")))

tab_html = []
tabs = driver.find_elements(By.CSS_SELECTOR, "nav.sc-drlKqa ul li a")

for idx in range(len(tabs)):
    tabs = driver.find_elements(By.CSS_SELECTOR, "nav.sc-drlKqa ul li a")  # refresh each loop
    tab_el = tabs[idx]
    tab_name = tab_el.text.strip()
    tab_el.click()

    container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.sc-gacfCG")))
    time.sleep(2)

    html_fragment = container.get_attribute("innerHTML")
    tab_html.append((tab_name, html_fragment))

try:
    driver.quit()
except Exception:
    pass

# Parse HTML to extract FAQs
faq_data = []
for tab_name, frag in tab_html:
    soup = BeautifulSoup(frag, "html.parser")
    for li in soup.select("ul > li"):
        q_tag = li.select_one("p.accordion__title")
        a_tag = li.select_one("div.accordion__text")
        if not q_tag:
            continue
        question = q_tag.get_text(strip=True)
        answer = a_tag.get_text("\n", strip=True) if a_tag else ""
        faq_data.append({
            "tab": tab_name,
            "question": question,
            "answer": answer
        })

# Save results
df = pd.DataFrame(faq_data)
df.to_csv("starzplay_faq.csv", index=False, encoding="utf-8")

with open("starzplay_faq.txt", "w", encoding="utf-8") as f:
    for row in faq_data:
        f.write(f"[Tab: {row['tab']}]\nQ: {row['question']}\nA: {row['answer']}\n\n")

print(f"Scraped {len(faq_data)} FAQs. Files saved: starzplay_faq.csv & starzplay_faq.txt")
