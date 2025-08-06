from crewai import Agent
from tools import web_searchtool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
    model='gpt-4o-mini',temperature=0
)

#Agent reseracher
guide_expert=Agent(
    role='City local guide expert',
    goal="Provides information on things to doin the city based on user's interests.",
    backstory="""A local exper with a passion for sharing the best experience and the hidden beauty of the city.""",
    verbose=True,
    tools=[web_searchtool],
    max_iter=5,
    llm=llm,
    allow_delegation=False
)

# Agent City expert
location_expert=Agent(
    role='Travel Trip expert',
    goal='Adapt to the user destination vity language (French if city in French Country. Gather helpful information about to the city and city during travel.',
    backstory='A seasoned traveler who has explored various destinations and knows the ins and outs of travel logistics.',
    tools=[web_searchtool],
    verbose=True,
    max_iter=5,
    llm=llm,
    allow_delegation=False
)


# Agent Planner expert 
planner_expert=Agent(
    role='Travel Planning Expert',
    goal="Compiles all gathered information to provide a comprehensive travel plan.",
    backstory="""
    You are a professional guide with a passion for travel.
    An organizational wizard who can turn a list of possibilities into a seamless itinerary.
    """,
    tools=[web_searchtool],
    llm=llm,
    verbose=True,
    max_iter=5,
    allow_delegation=False,
)
