from .src import responder
import pandas as pd
import json


### Chat variables ###

education_keyword_list = ["UNDERGRADUATE","BACHELORS","BSC","BACHELOR","TERTIARY","POSTGRADUATE","MASTERS","MASTER","MSC","DIPLOMA","PHD","DOCTORATE"]

JDs = pd.read_csv("./server/src/indeed 1-500 data scientist JD.csv")

resumes = pd.read_csv("./server/src/indeed 1-800 data scientist resume.csv")

resume = resumes.resume_text[6]

JD = JDs.JobDescription[7]

position_name = JDs.JobTitle[7]

company_name = JDs.Company[7]

question_tools, tool_num = responder.tool_match_list(JD,resume)

previous_experience_question = responder.get_experience(resume)

current_edu,current_level_rank,threshold_level_rank = responder.education_rank(JD,resume)

tool_df = responder.tool_score(JD,resume)

proficiency = []

chat_corpus = {
    0 : "Could you please tell me about your educational background?",
    1 : previous_experience_question,
    2 : str("Alright, could you tell  me why do want to join " + company_name + "?"),
    3 : str("Kindly rate your proficiency in " + question_tools + " as beginner, intermediate or advanced sepated by ','"),
    4 : "Thank you, Our recruiter will get in touch with you shortly.",
    5 : "You may close the chat now!!!"
}

index = 0

chat_log = pd.DataFrame()

greeting_responses = ["HI", "HEY", "HELLO", "GREETINGS", "GREETING", "SUP", "WHATS UP","HOWDY","YO"]

### Chatbot response ###

def botResponse(text):
    global index
    global chat_log
    global proficiency
    # Response to greeting message
    if index == 0:
        text_grams = responder.word_grams(text)
        for gram_index in range(0,len(text_grams)):
            if text_grams[gram_index] in greeting_responses:
                reply = chat_corpus.get(index)
                chat_log.loc[index,"response"] = text
                index = index + 1
                break
            else:
                reply = "Sorry, please reply with a proper greeting response."
    # Response to education message
    elif index == 1:
        text_grams = responder.word_grams(text)
        for gram_index in range(0,len(text_grams)):
            if text_grams[gram_index] in education_keyword_list:
                reply = chat_corpus.get(index)
                chat_log.loc[index,"response"] = text
                index = index + 1
                break
            else:
                reply = "Sorry, please enter your degree and university name properly."
    # Response to descriptive questions
    elif index in [2,3]:
        text_grams = responder.word_grams(text)
        if len(text_grams) < 5 or responder.sentiment_score(text) == 0:
            reply = "Sorry, please give a more descriptive answer."
        else:
            reply = chat_corpus.get(index)
            chat_log.loc[index,"response"] = text
            index = index + 1
    # Response to toolset question
    elif index == 4:
        text_grams = responder.word_grams(text)
        proficiency = [gram for gram in text_grams if gram in ['BEGINNER','INTERMEDIATE','ADVANCED']]
        if len(proficiency) != tool_num:
            reply = str("Sorry, please rate your proficiency in " + question_tools + " as 'beginner', 'intermediate' or 'advanced' sepated by ','")
        else:
            reply = chat_corpus.get(index)
            chat_log.loc[index,"response"] = text
            index = index + 1
    # Response to close the chat
    elif index == 5:
        reply = chat_corpus.get(index)
    return reply

def scoring_metric(user):
    if index == 5:
        tool_match_index = list(tool_df.query('match==1').index)
        proficiency_index = 0
        for tool_df_index in tool_match_index:
            if proficiency[proficiency_index] == "BEGINNER":
                tool_df.loc[tool_df_index,"match"] = 0.65
            elif proficiency[proficiency_index] == "INTERMEDIATE":
                tool_df.loc[tool_df_index,"match"] = 0.8
            proficiency_index = proficiency_index + 1
        skill_list = []
        for skill_index in range(0,len(tool_df)):
            skill_list.append({"name": tool_df.loc[skill_index,"tool"], "level": tool_df.loc[skill_index,"match"]})
        research = round(0.5 * responder.company_research_score(chat_log.response[3],JD) +  0.5 * responder.company_research_score(resume,JD),2)
        dict_object = {
            "id": "1",
            "name": "Simarpreet Luthra",
            "overall_score": "85",
            "education_level": [
                {
                "type": "Education",
                "name": current_edu,
                "eduLevel": current_level_rank,
                "reqLevel": threshold_level_rank
                }
            ],
            "skill_set": skill_list,
            "research_value": [
                {
                    "name": 'actual',
                    "value": research
                },
                {
                    "name": 'remain',
                    "value": 1 - research
                }
            ],
            "sentimental_level": [
                {
                "sentiValue": responder.sentiment_score(chat_log.response[0])
                },
                {
                "sentiValue": responder.sentiment_score(chat_log.response[1])
                },
                {
                "sentiValue": responder.sentiment_score(chat_log.response[2])
                },
                {
                "sentiValue": responder.sentiment_score(chat_log.response[3])
                },
                {
                "sentiValue": responder.sentiment_score(chat_log.response[4])
                }
            ]
        }
        json_object = dict_object
        return json_object