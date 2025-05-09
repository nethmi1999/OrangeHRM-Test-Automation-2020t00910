# OrangeHRM Automation

This project is a test automation framework for the OrangeHRM application using Selenium and Pytest.

## Prerequisites

Before running the tests, ensure you have the following installed:
1. Python 3.7 or higher
2. Google Chrome browser
3. ChromeDriver (automatically managed by `chromedriver-autoinstaller`)

## Installation

### 1.Clone the repository:

```bash
   git clone https://github.com/nethmi1999/OrangeHRM-Test-Automation-2020t00910.git
   ```
### 2.Create a virtual environment (optional)
```bash
   python -m venv venv
   venv\Scripts\activate  
   ```
### 3.Install the required dependencies:

```bash
   pip install -r requirements.txt
   ```
### 4.Install the required dependencies one by one(If necessary)

```bash
   pip install selenium
   pip install pytest
   pip install pytest-html
   pip install pytest-xdist
   pip install chromedriver-autoinstaller
   ```

## Configuration

The application configuration is located in `Config.py`. Update the following variables as needed:
- `APP_URL`: The URL of the OrangeHRM application.
- `LOGIN_USER`: The username for login.
- `LOGIN_PASS`: The password for login.
- `TIMEOUT_DURATION`: The maximum wait time for elements to load.
- `DELAY_DURATION`: The sleep time between actions.

## Running the Tests

```bash
   pytest TestCases/TestOrangeHRM.py
   ```

#### Logs

* Logs are saved in the Logs directory with a timestamped filename

## Project Structure
```
OrangeHRM-Test-Automation-2020t00910/
├── Logs/                    # Log files (auto-generated)
├── PageObjects/             # Page Object Model classes
├── TestCases/               # Test case scripts
├── Utilities/               # Utility modules (e.g:- Logger)
├── Config.py                # Configuration file
├── conftest.py              # Pytest fixtures
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies 
```

##### Notes

* Ensure the Chrome browser version matches the ChromeDriver version managed by chromedriver-autoinstaller