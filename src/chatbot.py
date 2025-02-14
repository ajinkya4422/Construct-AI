import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs
pairs = [
    [
        r"what is the project status",
        ["The project is currently on track. You can check the detailed status on the Project Insights page."]
    ],
    [
        r"how is the budget utilization",
        ["The budget utilization is within the planned limits. You can view the budget details on the Project Insights page."]
    ],
    [
        r"tell me about supply chain issues",
        ["The supply chain is currently stable. Any disruptions will be highlighted in the notifications."]
    ],
    [
        r"what is the energy consumption",
        ["Energy consumption is being monitored closely. You can view the energy usage details on the Project Insights page."]
    ],
    [
        r"how can I upload documents",
        ["You can upload documents on the Document Management page. Click on 'Go to Document Management' to access it."]
    ],
    [
        r"thank you",
        ["You're welcome! Let me know if you need further assistance."]
    ],
    [
        r"quit",
        ["Bye! Feel free to ask if you have more questions."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase your question?"]
    ]
]

def initialize_chatbot():
    return Chat(pairs, reflections)