AI Agents Using CrewAI Framework
=================================

This repository contains a collection of AI agents built using the CrewAI Framework. These agents leverage cutting-edge models such as OpenAI, Groq, and Ollama to perform a variety of tasks ranging from generating blog posts, summarizing YouTube videos, to analyzing stock market data. Each agent is designed to interact with specific models and tools, enabling them to perform their roles efficiently.

Agents Overview
--------------

1. **BlogWriter AI Agent**
	* Model: Ollama
	* Purpose: Generate engaging and SEO-optimized blog posts for social media sharing.
	* Features: Utilizes DuckDuckGo for research. Writes in a friendly tone, using tables for data representation. Incorporates trending keywords and SEO best practices.
2. **CustomerSupport AI Agent**
	* Model: OpenAI
	* Purpose: Provide customer support and answer questions.
	* Features: SerperAPI Key to understand customer queries to provide accurate and relevant answers.
3. **Automation AI Agent**
	* Model: OpenAI
	* Purpose: Scrape data from websites using the SeleniumScraperTool.
	* Features: Uses this Tool to automate web browsing. Scrapes data from websites using CSS selectors.
4. **YoutubeVideoResearcher AI Agent**
	* Model: OpenAI
	* Purpose: Search and summarize YouTube videos.
	* Features: Uses YouTubeVideoSearchTool for video analysis. Highlights key points and provides markdown-formatted summaries. Handles errors gracefully if videos are unavailable.

Technical Requirements
----------------------

* Python Version: 3.11.0
* Dependencies: Listed in `requirements.txt`.

Setup and Installation
----------------------

1. Create a Virtual Environment: `python -m venv myenv`
2. Activate the Virtual Environment: `cd myenv/Scripts/Activate`
3. Install Dependencies: `pip install -r requirements.txt`
4. Run the Application: `python <agent_file>.py`

Note: Make sure to replace API keys with your own in the environment variables.