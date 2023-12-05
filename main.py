import pytest
import requests
import sys
from io import StringIO
import allure

class TestProgram:
    def setup_method(self):
        self.http_session = requests.Session()

    def teardown_method(self):
        self.http_session.close()

    @allure.feature("HTTP")
    @allure.story("Successful Request")
    @allure.title("Test a successful HTTP request")
    @pytest.mark.feature("HTTP")
    @pytest.mark.story("Successful Request")
    def test_http_request_success(self):
        url = "https://api.sampleapis.com/futurama/questions"
        response = self.http_session.get(url)
        assert response.status_code == 200

    @allure.feature("HTTP")
    @allure.story("Successful Request")
    @allure.title("Test a successful HTTP request")
    @pytest.mark.feature("String Processing")
    @pytest.mark.story("Split JSON Content")
    def test_split_json_content_into_lines(self):
        json_content = "Question 1\r\nQuestion 2\r\nQuestion 3"
        questions = json_content.split("\r\n")
        assert questions is not None
        assert len(questions) == 3

    @allure.feature("HTTP")
    @allure.story("Successful Request")
    @allure.title("Test a successful HTTP request")
    @pytest.mark.feature("Console Output")
    @pytest.mark.story("Print Questions")
    def test_print_questions_to_console(self):
        questions = ["Question 1", "Question 2", "Question 3"]
        with StringIO() as captured_output:
            sys.stdout = captured_output
            for question in questions:
                print(question)
            console_output = captured_output.getvalue()
            assert console_output == "Question 1\nQuestion 2\nQuestion 3\n"

    @pytest.mark.feature("Exception Handling")
    @pytest.mark.story("Handle Exception")
    def test_handle_exception(self):
        exception = Exception("Test Exception")
        with StringIO() as captured_output:
            sys.stdout = captured_output
            print(f"Произошла ошибка: {str(exception)}")
            console_output = captured_output.getvalue()
            assert console_output == "Произошла ошибка: Test Exception\n"

if __name__ == "__main__":
    pytest.main(args=[__file__, "--junitxml=C:/Users/zxceb/PycharmProjects/kt5/reports/pytest_results.xml"])
    import subprocess
    subprocess.call(['allure', 'generate', 'allure-results'])
    subprocess.call(['allure', 'open', 'allure-report'])
