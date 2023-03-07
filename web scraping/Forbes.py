
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

# Set up the Selenium webdriver
path = "/home/nzangi/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=path)
# driver = webdriver.Chrome()
driver.get("https://www.forbes.com/real-time-billionaires/")
time.sleep(5)  # wait for the page to load

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")

# Find the table with class 'table'
table = soup.find("table", {"class": "table"})

if table is None:
    print("Error: could not find table on Forbes rich 100 list page")
else:
    # Extract table headers
    headers = []
    for th in table.find_all("th"):
        headers.append(th.text.strip())

    # Extract table rows
    rows = []
    for tr in table.find_all("tr")[1:11]:  # extract only the first 10 rows
        row = []
        for td in tr.find_all("td"):
            row.append(td.text.strip())
        if len(row) > 0:
            rows.append(row)

    # Create a DataFrame using the extracted data
    df = pd.DataFrame(rows, columns=headers)

    # Save the DataFrame to an Excel file
    df.to_excel("forbes_top_10_richest.xlsx", index=False)
    print("File saved")

# Quit the Selenium webdriver
driver.quit()

