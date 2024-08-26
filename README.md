# LinkedIn Queens Game Solver

This repository contains a Python project that automates solving the LinkedIn Queens game using Selenium WebDriver.

## Introduction

This project is designed to solve the LinkedIn Queens game by automating the process of placing queens on a chessboard using Selenium WebDriver. The program interacts with the game's web interface and computes the correct positions for the queens.

 * Your goal is to have exactly one queen in each row, column, and color region.
 * Two queens cannot touch each other, not even diagonally.

## Features

- Uses your Linkedin credentials to log into Linkedin and solve the game for you.
- Utilizes Selenium WebDriver for browser automation.

## Requirements

- Python 3.x
- ChromeDriver (compatible with your version of Chrome)
    - To download the chrome driver according to your version of chrome visit: https://sites.google.com/chromium.org/driver/downloads?authuser=0

## Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/mayanktolani19/linkedin-queens-game-solver.git
   cd linkedin-queens-game-solver
    ```

2. **Create a new virtual environment and activate it**

    ```
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**

    ```
    pip install -r requirements.txt
    ```

4. **Run the main file**
    
    ```
    python main.py
    ```
