# Instagram Account Auto-Registration with Proxies

This Python project automates the process of registering Instagram accounts using the Selenium WebDriver and proxies to ensure anonymity and bypass rate limitations.

## Features
- Automatic registration of Instagram accounts.
- Proxy support to ensure privacy and avoid IP rate limiting.
- Error handling to manage potential issues during the registration process.

## Requirements
- Python 3.x
- Selenium
- A web driver compatible with your browser (e.g., ChromeDriver for Chrome).
- A list of proxies for use during registration.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dimakostenko19/instagram_autoreg.git
   cd instagram_autoreg

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt

Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Proxies**: Place your proxy details (host, port, username, password) in the designated section of the script. Proxies will be used to register accounts.
   
2. **User Agents**: The script uses a file containing a list of user agents (`ua.txt`). Make sure to populate this file with valid user agent strings to randomize browser behavior.

3. **Headless Mode**: You can enable headless mode in the Selenium configuration to run the automation in the background without opening a browser window.

## Usage

1. To start the automation process, run:

    ```bash
    python insta_auto_register.py
    ```

2. The script will automatically register Instagram accounts using the provided proxy and user agent details.