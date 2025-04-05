import os
from crewai import Agent, Task, Crew
from crewai_tools import YoutubeVideoSearchTool

os.environ.get["OPENAI_API_KEY"]

# Initialize the tool for general YouTube video searches
youtube_search_tool = YoutubeVideoSearchTool()

# Define an agent that uses the tool
video_researcher = Agent(
    role="Video Researcher",
    llm="gpt-4o-mini",
    goal="Extract relevant information from YouTube videos",
    backstory="An expert researcher who specializes in analyzing video content.",
    tools=[youtube_search_tool],
    verbose=True,
)

# Example task to search for information in a specific video
research_task = Task(
    description="Search for information about machine learning frameworks in the YouTube video at {youtube_video_url}",
    expected_output="A summary of the key machine learning frameworks mentioned in the video.",
    agent=video_researcher,
)

# Create and run the crew
crew = Crew(agents=[video_researcher], tasks=[research_task])
result = crew.kickoff(inputs={"youtube_video_url": "https://youtu.be/rIyRrUAsaok?si=H-2B0Dg6xZ4Cotk9"})