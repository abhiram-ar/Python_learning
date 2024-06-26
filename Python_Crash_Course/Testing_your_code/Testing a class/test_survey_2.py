import unittest
from survey import AnonymousSurvey

class TestAnonumousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""
    

    # The unittest.TestCase class has a setUp() method that 
    # allows you to create these objects once and then 
    # use them in each of your test methods
    def setUp(self):
        """create a survey and a set of responsed for use in all test methods"""
        question = "what language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['english', 'malayalam', 'hindi']

        
    def test_store_single_response(self):
        """Test that a single response is stored properly."""

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    
    def test_store_three_responses(self):
        """test that three individial responses are stored properly"""

        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()

