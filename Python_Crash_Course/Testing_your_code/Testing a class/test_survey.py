import unittest
from survey import AnonymousSurvey

class TestAnonumousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""

        question = "what language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English',my_survey.responses)


if __name__ == "__main__":
    unittest.main()

