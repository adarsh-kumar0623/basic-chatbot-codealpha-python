import nltk
from nltk.chat.util import Chat, reflections

welcome_message = """
Hi there!  I'm a chatbot. Feel free to ask me questions or chat with me about anything that interests you. 

Here are some things I can help you with:
* Basic information
* Answering simple questions

To exit the conversation, just type 'quit' or 'goodbye'.
"""

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, nice to meet you! What would you like to talk about today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hi! ", "Hey there! ", "Hello! What can I do for you today?"]
    ],
    [
        r"what is your name?",
        ["I'm chatbot, I was created to help people like you."]
    ],
    [
        r"who created you?",
        ["I was created by Shishir."]
    ],
    [
        r"how are you?",
        ["I'm doing well, thanks for asking!  How can I assist you today?"]
    ],
    [
        r"sorry (.*)",
        ["No worries, mistakes happen.  What else can I help you with?"]
    ],
    [
        r"quit|goodbye",
        ["Goodbye!  It was nice talking to you. ", "See you later! "]
    ],
    [
        r"(.) weather (.)",
        ["While I can't directly access weather information, I can suggest some reliable weather services you can check out."]
    ],
    [
        r"(.*) (location|city) ?",
        ["As a virtual assistant, I don't have a physical location. But I can access information about many places."]
    ],
    [
        r"(.) (help|support) (.)",
        ["I can definitely help you with basic information and answer simple questions. What would you like to know?"]
    ],
    [
    
        r"what are your hobbies?",
        ["I enjoy processing information and learning new things. How about you?"]
    ],
    [
        r"what do you think about (.*)",
        ["As an AI, I don't have personal opinions. However, I can provide information about %1."]
    ],
    [
        r"tell me a joke",
        ["Why did the chicken cross the road? To get to the other side! Want another one?"]
    ],
    [
        r"explain artificial intelligence",
        ["Artificial intelligence, or AI, is the simulation of human intelligence in machines that are programmed to think like humans and mimic their actions."]
    ]
]

reflections = {
    "i am": "you are",
    "i'm": "you are",
    "we are": "you are",
    "are we": "are you",
    "was I": "were you",
    "I was": "were you",
    "I have": "you have",
    "do I have": "do you have",
    "because": "so",
    "why": "because",
    "could you": "will you",
    "will you": "can I",
    "can I": "could you",
    "you're welcome": "you're welcome",
    "my pleasure": "you're welcome",
    "everything": "almost everything",
}

def basic_chatbot():
    print(welcome_message)
    chat = Chat(pairs, reflections)
    chat.converse()

if _name_ == "_main_":
    basic_chatbot()