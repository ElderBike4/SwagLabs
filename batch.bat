pip install pipenv
pipenv install
pipenv shell
pip install selenium
pip install allure-pytest
pip install allure-behave
behave -f allure_behave.formatter:AllureFormatter -o allure-results ./features