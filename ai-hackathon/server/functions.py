from .src import responder
import pandas as pd

### Chat variables ###


chat_corpus = {
    "greeting" : "Could you please tell me about your educational background?",
    "education" : "hey",
    "reason" : "yo"
}

index = 0

chat_log = pd.DataFrame()

greeting_responses = ["HI", "HEY", "HELLO", "GREETINGS", "GREETING", "SUP", "WHATS UP","HOWDY","YO"]


### Chatbot response ###

def botResponse(text):
    global index
    chat_index = list(chat_corpus.keys())[index]
    # Response to greeting message
    if chat_index == "greeting":
        text_grams = responder.word_grams(text)
        for gram_index in range(0,len(text_grams)):
            if text_grams[gram_index] in greeting_responses:
                reply = chat_corpus.get(chat_index)
                index = index + 1
                chat_log.loc[index,"index"] = index
                chat_log.loc[index,"response"] = text
            else:
                reply = "Sorry, please reply with a proper greeting response"
    else:
        reply = chat_corpus.get(chat_index)
    return reply

