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
    
    def test_store_three_responses(self):
        """test that three individial responses are stored properly"""

        question = "what language did you firt learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['english', 'malayalam', 'hindi']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == "__main__":
    unittest.main()


# there is some repetiion going on this test code
# to avoid this refer test_survey_2.py
