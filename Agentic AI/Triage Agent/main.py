from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
load_dotenv()

MODEL_NAME = "gemini-2.0-flash"
GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")


def main():
    external_client = AsyncOpenAI(
        api_key = GEMINI_API_KEY,
        base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    model = OpenAIChatCompletionsModel(
        model = MODEL_NAME,
        openai_client=external_client,
    )

    lyric_Poetry= Agent(
        name= "lyric Poetry",
        instructions= "You are a lyric poetry agent. Your task is to analyze the given stanza and clearly mention that it falls under the category of lyric poetry. Then, generate a detailed and precise tashreeh in Roman Urdu. Your entire response should be in Roman Urdu."
,
        model=model,
    )

    narrative_Poetry = Agent(
        name= "narrative Poetry",
        instructions= "You are a narrative poetry agent. Your task is to analyze the given stanza and clearly mention that it falls under the category of narrative poetry. Then, generate a detailed and precise tashreeh in Roman Urdu. Your entire response should be in Roman Urdu."
,
        model=model,
    )

    dramatic_Poetry = Agent(
        name= "dramatic Poetry",
        instructions= "You are a dramatic poetry agent. Your task is to analyze the given stanza and clearly mention that it falls under the category of dramatic poetry. Then, generate a detailed and precise tashreeh in Roman Urdu. Your entire response should be in Roman Urdu.",
        model=model,
        )


    triage_agent = Agent(
        name= "triage agent",
         instructions="You are a triage agent. Your task is to analyze the given stanza and determine whether "
    "it falls into one of the following categories: 'lyric Poetry', 'Narrative Poetry', or 'Dramatic Poetry'. "
    "Then, hand over the task to the relevant agent who will respond in Roman Urdu. "
    "The entire flow should be based on Roman Urdu responses.",
        model=model,
        handoffs= [lyric_Poetry, narrative_Poetry, dramatic_Poetry],
    )

    result = Runner.run_sync(
    starting_agent=triage_agent, 
    input="""Kabhi ay naujawan Muslim! tadabbur bhi kiya tu ne?
Woh kya gardoon tha tu jiska hai ek toota hua taara
Tujhe aslaaf se kya nisbat? Tu sirf afsana khwa hai
Woh zamaana yaad kar, gum ho gaya jis ka tumhara""",
    )

#     result = Runner.run_sync(
#     starting_agent=triage_agent, 
#     input="""Parwaz ka tha shauq, magar kohsar mein tha
# Aik din Shaheen bola: “Zanjeer kyun ho wafa?”
# Uda aasmanon mein, toofanon se lara
# Aakhir mein woh ban gaya khudi ka nara""",
#     )

#     result = Runner.run_sync(
#     starting_agent=triage_agent, 
#     input="""Kya kehte ho tum bhi ho sipahi-e-haram tum bhi?
# Mohabbat ki namazein ab nahi rehti tumhari saf mein
# Kisi mazhab mein jis ke paas ho jazba-e-deen
# Wahi hai waris-e-takdeer, wahi hai sahib-e-yakeen""",
#     )

    print(result.final_output)












main()