import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для  класса AnonymousSurvey"""

    if __name__ == "__main__":
        unittest.main()

    def setUp(self):
        """Создание опроса и набора ответов для всех тестовых методов"""
        question = "test question"
        self.survey = AnonymousSurvey(question)
        self.responses = ['foo', 'bar', 'baz']

    def test_store_single_response(self):
        self.survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.survey.responses)

    def test_store_three_response(self):

        for response in self.responses:
            self.survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.survey.responses)
