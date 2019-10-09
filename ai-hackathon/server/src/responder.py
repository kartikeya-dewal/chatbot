# DataFrame creation and manipulation
import pandas as pd

# Text manipulation libraries

import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
import string

# Document processing corpus

toolsets = {
    "PROGRAMMING": ["PYTHON","C++","C#","JAVA","C","JAVASCRIPT","RUBY","SCALA","RAILS","JULIA","PHP",".NET","SWIFT"],
    "STATISTICAL": ["SAS","R","MINITAB","MATLAB","SPSS","RSTUDIO"],
    "BIGDATA": ["SPARK","CLOUDERA","HADOOP","MAPREDUCE","HIVE"],
    "CLOUD": ["AWS","AZURE","GCP","GOOGLE CLOUD","WATSON","ALIBABA CLOUD"],
    "VISUALISATION" : ["TABLEAU","POWER BI","SHINY","POWERBI"],
    "FRONTEND": ["REACT","HTML","CSS","D3","ANGULER","VUE","BOOTSTRAP"],
    "DATABASE": ["ORACLE","MYSQL","POSTGRESQL","MONGODB","DB2","ELASTIC","SQL","NOSQL"],
    "CRYPTO":["BLOCKCHAIN","BITCOIN","ETHERIUM"],
    "SPREADSHEET": ["EXCEL","GOOGLE SHEETS","OPENOFFICE","LIBREOFFICE"] 
}

education_keywords = {
"UNDERGRADUATE": ["UNDERGRADUATE","BACHELORS","BSC","BACHELOR","TERTIARY"],
"POSTGRADUATE":["POSTGRADUATE","MASTERS","MASTER","MSC","DIPLOMA"],
"DOCTORATE":["PHD","DOCTORATE"]
}

education_level_ranks = {
    "UNDERGRADUATE": 1,
    "POSTGRADUATE": 2,
    "DOCTORATE": 3
}


# Text processing functions

def word_grams(text, min=1, max=1):
    words = []
    for punct in list(string.punctuation):
        if punct == "'": 
            text = text.replace(punct,"")
        else:
            text = text.replace(punct," ")
    text = text.replace("’","")
    text= text.upper()
    for n in range(min, max+1):
        for ngram in nltk.ngrams(text.split(), n):
            words.append(' '.join(str(word) for word in ngram))
    return words

def toolset_list(text):
    tools = pd.DataFrame()
    tools["tool"] = ""
    tools["type"] = ""
    index = 0
    terms = word_grams(text,1,2)
    for tool_type in toolsets:
        for tool in toolsets.get(tool_type):
                if tool in terms and tool not in tools["tool"]:
                    tools.loc[index,"tool"] = tool
                    tools.loc[index,"type"] = tool_type
                    index = index + 1
    return tools

def company_research_score(response,JD):
    text = set(word_grams(response))
    stopwords = set([stopword.upper() for stopword in nltk.corpus.stopwords.words('english')])
    residual = text - stopwords
    intersection = set(word_grams(JD)).intersection(res)
    similarity = len(intersection)
    if similarity <= 5:
        research = 0.1 * similarity
    elif similarity > 5 and similarity <= 10:
        research = 0.5 + 0.1 * (similarity - 5)
    else:
        research = 1
    return round(research,2)

def get_JD_education(JD):
    edu = []
    terms = word_grams(JD)
    for level in education_keywords:
        for keyword in education_keywords.get(level):
                if keyword in terms and level not in edu:
                    edu.append(level)
    if 'DOCTORATE' in edu:
        education_level = 'DOCTORATE'
    elif 'POSTGRADUATE' in edu:
        education_level = 'POSTGRADUATE'
    else:
        education_level = 'UNDERGRADUATE'
    return education_level

def get_resume_education(resume):
    text = resume.upper()
    lines = nltk.tokenize.LineTokenizer().tokenize(text)
    for line_num in range(0,len(lines)):
        line = lines[line_num]
        if line == 'EDUCATION':
            degree = lines[line_num+1]
            university = lines[line_num+2]
            break
    return degree, university

def get_experience(resume):
    text = resume.upper()
    lines = nltk.tokenize.LineTokenizer().tokenize(text)
    for line_num in range(0,len(lines)):
        line = lines[line_num]
        if line == 'WORK EXPERIENCE':
            position = lines[line_num+1]
            company = lines[line_num+2]
            timeline = lines[line_num+3]
            break
    if "PRESENT" in timeline.upper():
        question = str("Great, why do you want to leave your current job as " + position + " at " + company + "?")
    else:
        question = str("Great, why did you leave your previous job as " + position + " at " + company + "?")
    return question

def education_rank(JD,resume):
    current_level = 'UNDERGRADUATE'
    current_edu, _ = get_resume_education(resume)
    current_edu_words = word_grams(current_edu)
    for word in current_edu_words:
        for level in education_keywords:
            if word in education_keywords.get(level):
                current_level = level
                break
    current_level_rank = education_level_ranks.get(current_level)
    threshold_level = get_JD_education(JD)
    threshold_level_rank = education_level_ranks.get(threshold_level)
    return current_edu,current_level_rank,threshold_level_rank

def overall_education_score(JD,resume):
    _,current_level_rank,threshold_level_rank = education_rank(JD,resume)
    if current_level_rank < threshold_level_rank:
        score = 0
    elif current_level_rank == 3:
        score = 1
    elif current_level_rank == 2:
        score = 0.8 + 0.05*(current_level_rank/threshold_level_rank)
    else:
        score = 0.8
    return round(score,2)

def sentiment_score(text):
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score['compound']

def tool_score(JD,resume):
    tool_match = pd.DataFrame()
    required_tools = toolset_list(JD)
    candidate_tools = toolset_list(resume)
    for index in range(0,len(required_tools)):
        tool = required_tools.loc[index,"tool"]
        tool_type = required_tools.loc[index,"type"]
        if tool in list(candidate_tools["tool"]):
            tool_match.loc[index,"tool"] = tool
            tool_match.loc[index,"type"] = tool_type
            tool_match.loc[index,"match"] = 1
        elif tool not in list(candidate_tools["tool"]) and tool_type in list(candidate_tools["type"]):
            tool_match.loc[index,"tool"] = tool
            tool_match.loc[index,"type"] = tool_type
            tool_match.loc[index,"match"] = 0.5
        else:
            tool_match.loc[index,"tool"] = tool
            tool_match.loc[index,"type"] = tool_type
            tool_match.loc[index,"match"] = 0
    return tool_match

def tool_match_list(JD,resume):
    tool_df = tool_score(JD,resume)
    tool_df_subset = tool_df.query('match == 1')
    tool_list = list(tool_df_subset.tool)
    num = len(tool_list)
    sep = ", "
    tools = sep.join(tool_list)
    return tools, num

