import os
from crewai import Agent, Task, Crew
from crewai_tools import SeleniumScrapingTool, SerperDevTool

# Set your OpenAI API key
os.environ.get["SERPAPI_API_KEY"]
os.environ.get["OPENAI_API_KEY"]

# Define the agent with the tool
agent = Agent(
    role="News Monitor Agent",
    goal="Monitor and summarize the latest news articles",
    backstory="I am an AI agent designed to keep track of the latest news and provide concise summaries.",
    tools=[SeleniumScrapingTool()],
    llm="gpt-4o-mini"
)

# Define the task for the agent with the query parameter
task = Task(
    description=f"Use the SeleniumScrapingTool to scrape the latest news articles about {query} from the specified website and provide a summary.",
    agent=agent,
    expected_output="A summary of the latest news articles related to the query."
)

# Create and run the crew
crew = Crew(
    agents=[agent],
    tasks=[task],
)

# Accept user input for the query
query = input("Enter your query: ")

# Execute the crew and print the result
result = crew.kickoff()
print(result)