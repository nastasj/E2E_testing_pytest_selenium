## How to run tests
1. Download the project `git clone https://github.com/nastasj/E2E_testing_pytest_selenium.git`
2. Create and activate virtual environment as you usually do
3. Install packages to the environment from the requirements.txt file: `pip install -r requirements.txt`
4. Make sure that the path to geckodriver.exe and chromedriver.exe is registered in the PATH
5. Run tests with the command: `pytest -v --tb = line test_feature.py` (or `pytest -v --browser_name = firefox --tb = line test_feature.py` - for Firefox, since Chrome is set as the default browser for running tests)
