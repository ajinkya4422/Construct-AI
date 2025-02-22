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
        ["We are closely monitoring energy consumption to ensure optimal efficiency and sustainability throughout the project. Our system continuously tracks energy usage patterns, helping us identify areas where improvements can be made..Real-time energy consumption data for different project phases.The Project Insights page provides a detailed overview of energy usage, including historical trends, real-time data, and alerts for unusual spikes. By leveraging these insights, we can take proactive measures to reduce energy waste and enhance overall project performance. "]
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