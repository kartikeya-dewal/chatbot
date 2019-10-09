from .src import responder
import pandas as pd

### Chat variables ###

JDs = pd.read_csv("./server/src/indeed 1-500 data scientist JD.csv")

resumes = pd.read_csv("./server/src/indeed 1-800 data scientist resume.csv")

resume = resumes.resume_text[6]

JD = JDs.JobDescription[6]

company_name = JDs.Company[6]

question_tools, tool_num = responder.tool_match_list(JD,resume)


chat_corpus = {
    0 : "Could you please tell me about your educational background?",
    1 : "Why did you leave your previous job?",
    2 : str("What attracts you about this role and " + company_name + "?"),
    3 : str("Kindly rate your proficiency in " + question_tools + " as beginner, intermediate or advanced sepated by ','"),
    4 : "Thank you, you may close the chat now\nOur recruiter will get in touch with you shortly."
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
        text_grams = responder.word_grams(text,2,2)
        for gram_index in range(0,len(text_grams)):
            if text_grams[gram_index] in responder.word_grams(university,2,2):
                reply = chat_corpus.get(index)
                index = index + 1
                chat_log.loc[index,"index"] = index
                chat_log.loc[index,"response"] = text
                break
            else:
                reply = "Sorry, please enter your degree and university name properly."
    elif index in [2,3]:
        text_grams = responder.word_grams(text)
        if len(text_grams) < 10 or responder.sentiment_score(text) == 0:
            reply = "Sorry, please give a more descriptive answer."
        else:
            reply = chat_corpus.get(index)
            index = index + 1
            chat_log.loc[index,"index"] = index
            chat_log.loc[index,"response"] = text
    elif index == 4:
        text_grams = responder.word_grams(text)
        text_grams = [gram for gram in text_grams if gram in ['BEGINNER','INTERMEDIATE','ADVANCED']]
        if len(text_grams) != tool_num:
            reply = str("Sorry, please rate " + question_tools " as 'beginner', 'intermediate' or 'advanced' sepated by ','")
        else:
            reply = chat_corpus.get(index)
            index = index + 1
            chat_log.loc[index,"index"] = index
            chat_log.loc[index,"response"] = text
    elif index == 5:
        reply = chat_corpus.get(index)
    return reply

