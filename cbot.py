import speech_recognition as sr
import nltk
import warnings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
import string 
from gtts import gTTS
import os 

f=open('data.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()
sent_tokens = nltk.sent_tokenize(raw) 
word_tokens = nltk.word_tokenize(raw)

sent_tokens[:2]
word_tokens[:5]


lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "what's up","hey","Hello")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad to talk to you"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)




def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"Sorry what are you saying"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response


flag=True
print("JARVIS: Hy my name is jarvis!")
text="Hy my name is yanki paji!"
language = 'en'
  

myobj = gTTS(text=text, lang=language, slow=False) 
myobj.save("welcome.mp3") 
  
# Playing the converted file 
os.system("welcome.mp3") 
while(flag==True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)
        text=r.recognize_google(audio)
        print(text)
        user_response = text 
        user_response=user_response.lower()
        if(user_response!='bye'):
            
            if(user_response=='thanks' or user_response=='thank you' or user_response=='thanku'):
                flag=False
                print("You are welcome..")
                text="You are welcome.."
                language = 'en'
  

                myobj = gTTS(text=text, lang=language, slow=False) 
                myobj.save("welcome.mp3") 
  
# Playing the converted file 
                os.system("welcome.mp3")
            
            else:
                if(greeting(user_response)!=None):
                    text=greeting(user_response)
                    print("JARVIS: "+text)
            
                    language = 'en'
  

                    myobj = gTTS(text=text, lang=language, slow=False) 
                    myobj.save("welcome.mp3") 
  
# Playing the converted file 
                    os.system("welcome.mp3")
           
                else:
                    print("JARVIS: ",end="")
#                                print("JARVIS: "+text)
            
                    language = 'en'
  
                    text=response(user_response)
                    myobj = gTTS(text=text, lang=language, slow=False) 
                    myobj.save("wel.mp3") 
  
# Playing the converted file 
                    os.system("wel.mp3")
                    print(text)
                    sent_tokens.remove(user_response)
        else:
            flag=False
            print("JARVIS: Bye have a nice day")    
            text="Bye have a nice day"
            language = 'en'
  

            myobj = gTTS(text=text, lang=language, slow=False) 
            myobj.save("welcome.mp3") 
  
# Playing the converted file 
            os.system("welcome.mp3")
            
        

