import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool


# Set environment variables for API keys
os.environ.get["OPENAI_API_KEY"]
os.environ.get["SERPER_API_KEY"]

# Instantiate the web search tool
serper_tool = SerperDevTool()

# Define the Senior Support Representative agent
support_agent = Agent(
    role="Senior Support Representative",
    goal="Be the most friendly and helpful support representative in your team",
    backstory=(
        "You work at CrewAI ([https://www.crewai.com/](https://www.crewai.com/)) and are now working on providing "
        "support to {customer}, a super important customer for your company. "
        "You have access to a web search tool that can search the internet and CrewAI's website. "
        "To find information in the documentation, use the web search tool with queries like 'site:www.posidex.com [topic]'. "
        "If you can't find the information there, perform a general web search. "
        "Make sure to provide full and complete answers, and make no assumptions."
    ),
    llm="gpt-4o-mini",
    allow_delegation=False,
    verbose=True,
    memory=True
)

# Define the Support Quality Assurance Specialist agent
support_quality_assurance_agent = Agent(
    role="Support Quality Assurance Specialist",
    goal="Get recognition for providing the best support quality assurance in your team",
    backstory=(
        "You work at Posidex Technologies ([https://www.crewai.com/](https://www.crewai.com/)) and are now working with your team "
        "on a request from {customer} ensuring that the support representative is "
        "providing the best support possible.\n"
        "You need to make sure that the support representative is providing full "
        "complete answers, and make no assumptions."
    ),
    llm="gpt-4o-mini",
    memory=True,
    verbose=True
)

# Define the inquiry resolution task
inquiry_resolution = Task(
    description=(
        "{customer} just reached out with a super important ask:\n"
        "{inquiry}\n\n"
        "{person} from {customer} is the one that reached out. "
        "Make sure to use everything you know to provide the best support possible."
        "You must strive to provide a complete and accurate response to the customer's inquiry."
    ),
    expected_output=(
        "A detailed, informative response to the customer's inquiry that addresses "
        "all aspects of their question.\n"
        "The response should include references to everything you used to find the answer, "
        "including external data or solutions. Ensure the answer is complete, "
        "leaving no questions unanswered, and maintain a helpful and friendly tone throughout."
    ),
    tools=[serper_tool],
    agent=support_agent,
)

# Define the quality assurance review task
quality_assurance_review = Task(
    description=(
        "Review the response drafted by the Senior Support Representative for {customer}'s inquiry. "
        "Ensure that the answer is comprehensive, accurate, and adheres to the "
        "high-quality standards expected for customer support.\n"
        "Verify that all parts of the customer's inquiry have been addressed "
        "thoroughly, with a helpful and friendly tone.\n"
        "Check for references and sources used to find the information, "
        "ensuring the response is well-supported and leaves no questions unanswered."
    ),
    expected_output=(
        "A final, detailed, and informative response ready to be sent to the customer.\n"
        "This response should fully address the customer's inquiry, incorporating all "
        "relevant feedback and improvements.\n"
        "Don't be too formal, we are a chill and cool company but maintain a professional and friendly tone throughout."
    ),
    agent=support_quality_assurance_agent,
)

# Create the crew with agents and tasks
crew = Crew(
    agents=[support_agent, support_quality_assurance_agent],
    tasks=[inquiry_resolution, quality_assurance_review],
    verbose=True,
    memory=True
)

# Conversational loop
print("Welcome to CrewAI Customer Support")
customer = input("Please enter the customer name: ")
person = input("Please enter the person's name: ")

while True:
    inquiry = input("How can I assist you today? (Type 'exit' to end): ")
    if inquiry.lower() == "exit":
        print("Thank you for contacting CrewAI Customer Support. Goodbye.")
        break
    inputs = {
        "customer": customer,
        "person": person,
        "inquiry": inquiry
    }
    crew.kickoff(inputs=inputs)
