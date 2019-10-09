from .src import responder
import pandas as pd
import json


### Chat variables ###

education_keyword_list = ["UNDERGRADUATE","BACHELORS","BSC","BACHELOR","TERTIARY","POSTGRADUATE","MASTERS","MASTER","MSC","DIPLOMA","PHD","DOCTORATE"]

JDs = pd.read_csv("./server/src/indeed 1-500 data scientist JD.csv")

resumes = pd.read_csv("./server/src/indeed 1-800 data scientist resume.csv")

resume = resumes.resume_text[6]

JD = JDs.JobDescription[7]

company_name = JDs.Company[7]

question_tools, tool_num = responder.tool_match_list(JD,resume)

chat_corpus = {
    0 : "Could you please tell me about your educational background?",
    1 : "Great, why did you leave your previous job?",
    2 : str("Alright, could you tell  me mhat attracts you about this role and " + company_name + "?"),
    3 : str("Kindly rate your proficiency in " + question_tools + " as beginner, intermediate or advanced sepated by ','"),
    4 : "Thank you, you may close the chat now\nOur recruiter will get in touch with you shortly.",
    5 : "You may close the chat now!!!"
}

index = 0

chat_log = pd.DataFrame()

greeting_responses = ["HI", "HEY", "HELLO", "GREETINGS", "GREETING", "SUP", "WHATS UP","HOWDY","YO"]

degree, university = responder.get_resume_education(resume)

### Chatbot response ###

def botResponse(text):
    global index
    global chat_log
    # Response to greeting message
    if index == 0:
        text_grams = responder.word_grams(text)
        for gram_index in range(0,len(text_grams)):
            if text_grams[gram_index] in greeting_responses:
                reply = chat_corpus.get(index)
                index = index + 1
                chat_log.loc[index,"index"] = index
                chat_log.loc[index,"response"] = text
                break
            else:
                reply = "Sorry, please reply with a proper greeting response."
    # Response to education message
    elif index == 1:
        text_grams = responder.word_grams(text)
        for gram_index in range(0,len(text_grams)):
            if text_grams[gram_index] in education_keyword_list:
                reply = chat_corpus.get(index)
                index = index + 1
                chat_log.loc[index,"index"] = index
                chat_log.loc[index,"response"] = text
                break
            else:
                reply = "Sorry, please enter your degree and university name properly."
    # Response to descriptive questions
    elif index in [2,3]:
        text_grams = responder.word_grams(text)
        if len(text_grams) < 10 or responder.sentiment_score(text) == 0:
            reply = "Sorry, please give a more descriptive answer."
        else:
            reply = chat_corpus.get(index)
            index = index + 1
            chat_log.loc[index,"index"] = index
            chat_log.loc[index,"response"] = text
    # Response to toolset question
    elif index == 4:
        text_grams = responder.word_grams(text)
        text_grams = [gram for gram in text_grams if gram in ['BEGINNER','INTERMEDIATE','ADVANCED']]
        if len(text_grams) != tool_num:
            reply = str("Sorry, please rate your proficiency in" + question_tools + " as 'beginner', 'intermediate' or 'advanced' sepated by ','")
        else:
            reply = chat_corpus.get(index)
            chat_log.loc[index + 1,"index"] = index + 1
            chat_log.loc[index + 1,"response"] = text
            index = index + 1
    # Response to close the chat
    elif index == 5:
        reply = chat_corpus.get(index)
    return reply

def scoring_metric(user):
    if index == 0:
        dict_object = {
            "id": "1",
            "name": "Simarpreet Luthra",
            "overall_score": "85",
            "education_level": [
                {
                "type": "Education",
                "name": "Bachelor of Life Science",
                "eduLevel": 1,
                "reqLevel": 3
                }
            ],
            "skill_set": [
                {
                "name": "Python",
                "level": 0.25
                },
                {
                "name": "HTML5",
                "level": 0.5
                },
                {
                "name": "R",
                "level": 0.75
                },
                {
                "name": "Java",
                "level": 0.25
                },
                {
                "name": "PHP7",
                "level": 0.5
                }
            ],
            "research_value": [
                {
                    "name": 'actual',
                    "value": 0.8
                },
                {
                    "name": 'remain',
                    "value": 0.2
                }
            ],
            "sentimental_level": [
                {
                "sentiValue": 0.87
                },
                {
                "sentiValue": 0.8
                },
                {
                "sentiValue": -0.2
                },
                {
                "sentiValue": 0.38
                },
                {
                "sentiValue": 0.45
                }
            ]
        }
        json_object = json.dumps(dict_object)
        return json_object