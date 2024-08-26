from board_solver import board_solver 
from board_converter import board_converter
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import numpy as np
from credentials import credentials
from bs4 import BeautifulSoup

# Ensure that your chrome driver is present in the directory same as the python file to be executed.
service = Service(executable_path=r'./chromedriver')

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(service=service, options=options)

# Set to true if playing for first time, since linkedin shows some tutorial for the game, handling has been done for it.
first_time = True


driver.get("https://www.linkedin.com/games/queens/")
driver.implicitly_wait(10)

# Enter credentials
credentials().enterCredentials(driver)

# Sign in btn is a btn with data-litms-control-urn = login-submit
sign_in_btn = driver.find_element(By.CSS_SELECTOR, "button[data-litms-control-urn='login-submit']")
sign_in_btn.click()

try:
    start_btn = driver.find_element(By.CSS_SELECTOR, "button.launch-footer__btn--start")
    start_btn.click()
except:
    pass

if (first_time):
    try:
        # the skip is artdeco-modal__dismiss
        skip_btn = driver.find_element(By.CSS_SELECTOR, "button.artdeco-modal__dismiss")
        skip_btn.click()
    except:
        pass

time.sleep(1)
queens_grid = driver.find_element(By.ID, "queens-grid")
soup = BeautifulSoup(queens_grid.get_attribute("outerHTML"), "html.parser")

boardConverter = board_converter(soup)
board = boardConverter.convertHtmlBoardToArray()

solver = board_solver(board, board.shape)
sol = solver.solve()

print("Board:\n", board)
print("Solution:\n", sol)

# Obtaining the queens positions and transforming them to the format requested by the game
indexes = np.argwhere(sol == 1)
print("Queens Indices:\n", indexes)
queens = [ queen[0] * board.shape[0] + queen[1] for queen in indexes]

# Check if today's game has already been solved.
# try:
#     results_btn = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div[1]/div[2]/div/div/main/div/div[4]/button")
#     print("You have already completed today's game.")
#     driver.quit()
# except:
#     pass

# Now we play the game
for queen in queens:
    queen_pos = driver.find_element(By.CSS_SELECTOR, f"div[data-cell-idx='{queen}']")
    queen_pos.click()
    time.sleep(1)
    queen_pos.click()
    time.sleep(1)
    
time.sleep(10)
driver.quit()

print(board)