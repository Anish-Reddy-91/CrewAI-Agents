import os
from langchain_openai import ChatOpenAI
from crewai import Agent, Task, Crew, Process

# Set your OpenAI API key
os.environ.get["OPENAI_API_KEY"]  # Replace with your actual API key

# Specify the OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.5
)

# Define Agents with general expertise
expert_agent = Agent(
    role="Researcher",
    goal="Gather comprehensive information on any given topic",
    verbose=True,
    backstory="You are an expert researcher with access to a wide range of reliable sources. Your goal is to provide accurate and in-depth information on any given topic.",
    llm=llm
)

analyst_agent = Agent(
    role="Analyst",
    goal="Analyze and evaluate information on any subject",
    verbose=True,
    backstory="You are a skilled analyst capable of evaluating information on any subject. You can identify key insights, comparisons, or trends based on the data provided.",
    llm=llm
)

writer_agent = Agent(
    role="Technical Writer",
    goal="Create clear, structured content on any topic",
    verbose=True,
    backstory="You are a professional writer who specializes in creating clear and engaging content from complex information. Your role is to craft well-organized documents that are easy to understand.",
    llm=llm
)

# Function to create dynamic tasks based on the user's query
def create_tasks(user_query):
    info_task = Task(
        description=f"Given the user query: {user_query}, find and compile comprehensive information from reliable sources. Include context, key concepts, and relevant data.",
        expected_output="A detailed report of the information gathered.",
        agent=expert_agent
    )
    analysis_task = Task(
        description=f"Analyze the information gathered by the researcher on the topic: {user_query}. Extract key insights, comparisons, or evaluations relevant to the user's query.",
        expected_output="An analysis report highlighting key points.",
        agent=analyst_agent
    )
    writing_task = Task(
        description=f"Create a clear, well-structured blog document based on the analysis provided for the user's query: {user_query}. Ensure the content is tailored to the query, easy to understand and engaging.",
        expected_output="A well-structured document answering the user's query.",
        agent=writer_agent,
        output_file="answer2.md"
    )
    return [info_task, analysis_task, writing_task]

# Prompt the user for a query
user_query = input("Enter a topic: ")

# Create tasks based on the user query
tasks = create_tasks(user_query)

# Create the crew with agents and tasks
crew = Crew(
    agents=[expert_agent, analyst_agent, writer_agent],
    tasks=tasks,
    process=Process.sequential,
    verbose=True
)

# Run the crew
result = crew.kickoff()