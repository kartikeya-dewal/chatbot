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

dict_object = {
    "register_id": "id_230987410258",
    "register name": "Jone Doe",
    "overall_match_rate": "85",
    "education_level": {
        "name": "PHD in Computer Science",
        "current_edu_level": 4,
        "threshold_level": 3
    },
    "skill_set": {
        "HTML": 1,
        "PHP": 0.5,
        "Javascript": 0.8,
        "R": 0.3,
        "Python": 0.1,
        },
    "research_value": {
        "actual" : 0.8,
        "remaining" : 0.2
    },
    "sentimental_level": {
        "1": "0.1",
        "2": "0.2",
        "3": "0.1",
        "4": "0.2",
        "5": "0.1"
    }
}

json_object = json.dumps(dict_object)

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
            index = index + 1
            chat_log.loc[index,"index"] = index
            chat_log.loc[index,"response"] = text
    # Response to close the chat
    elif index == 5:
        reply = chat_corpus.get(index)
    return reply
