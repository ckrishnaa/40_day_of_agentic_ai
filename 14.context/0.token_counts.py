from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.messages.utils import count_tokens_approximately

history = [
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
    SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
        HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
        SystemMessage("You are a friendly travel assistant for Kerala trips."),
        HumanMessage(
            "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
        ),
        AIMessage(
            "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
        ),
        HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
        SystemMessage("You are a friendly travel assistant for Kerala trips."),
        HumanMessage(
            "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
        ),
        AIMessage(
            "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
        ),
        HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
        SystemMessage("You are a friendly travel assistant for Kerala trips."),
        HumanMessage(
            "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
        ),
        AIMessage(
            "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
        ),
        HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
        SystemMessage("You are a friendly travel assistant for Kerala trips."),
        HumanMessage(
            "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
        ),
        AIMessage(
            "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
        ),
        HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
        SystemMessage("You are a friendly travel assistant for Kerala trips."),
        HumanMessage(
            "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
        ),
        AIMessage(
            "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
        ),
        HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
        SystemMessage("You are a friendly travel assistant for Kerala trips."),
    HumanMessage(
        "I want to plan a 5 day trip to Kerala in December. Budget is 40,000 rupees."
    ),
    AIMessage(
        "Sounds great! Munnar, Alleppey and Kochi make a lovely loop. Want a day-by-day plan?"
    ),
    HumanMessage("Yes please, and we love backwaters but hate crowded beaches."),
]
print("tokens used  :", count_tokens_approximately(history))
