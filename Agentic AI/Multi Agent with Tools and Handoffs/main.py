from dotenv import load_dotenv
import os
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig, function_tool
import asyncio
load_dotenv()

@function_tool
def current_location():
    return "I'm currently in the office."

@function_tool
def breaking_news():
    return "There are no significant breaking news at the moment."


async def main():
    
    MODEL_NAME = "gemini-2.0-flash"
    GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")

    external_client = AsyncOpenAI(
            api_key = GEMINI_API_KEY,
            base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
        )

    model = OpenAIChatCompletionsModel(
            model= MODEL_NAME,
            openai_client = external_client
        )
    config = RunConfig(
            model = model,
            model_provider = external_client
        )


    agent = Agent(
            name= "plant_agent",
            instructions= "You are a helpful assistant that can give a helpful and friendly concise explanation about photosynthesis ",
            model = model
    )

    main_agent = Agent(
        name= "main_agent",
        instructions= "You are a helpful assistant that can answer questions about various topics, including your current location, breaking news, and photosynthesis.",
        tools=[current_location, breaking_news],
        handoffs =[agent],
        model = model
    )

  
    result = await Runner.run(main_agent,
                              """
                               1. What is my current location?
                               2. What is the latest breaking news?
                               3. What is photosynthesis?
                               """,
                               run_config=config
                               )
        # result = await Runner.run(main_agent,
        #                       """
        #                        3. What is photosynthesis?
        #                        """,
        #                        run_config=config
        #                        )
    
    print('='*80)
    print("Result:", result.last_agent.name, "\n")
    print(result.new_items)
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())

