from survey import AnonymousSurvey

#define a question, and make a survey.
question = "what language did you first learn to speak"
my_survey = AnonymousSurvey(question)

#show the question and store the responses to the question.
my_survey.show_question()
print("enter 'q' to exit anytime")
while True:
    response = input("Language : ")
    if response == "q":
        break
    my_survey.store_response(response)

#show result of the survey
print("\n Thank you everyone for participating in the survey")
my_survey.show_results()