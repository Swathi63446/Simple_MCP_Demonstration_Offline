Simple MCP Demonstration (Offline)

Description:
This project demonstrates an offline MCP (Model Context Protocol) agent that can answer general queries from a mock database and provide tool-based responses like weather information—without using any API keys or internet services. The goal is to understand and showcase the workflow and importance of MCPs in AI systems.

Features

General Queries: Answers questions using mock_database.json

Tool Queries (Weather): Returns mock weather info via a local MCP server

Fully offline, modular, and self-contained

Implements client-server interaction using Python + FastAPI

File Structure
mcps_project/
│
├─ agent_host.py        # Handles user input and manages queries
├─ mcp_client.py        # Sends requests to the MCP server
├─ mcp_server.py        # FastAPI server providing tool responses
├─ mock_database.json   # Offline database of general knowledge

How It Works

User types a query in agent_host.py

Agent detects query type:

General query → searches mock_database.json

Tool query → sends request to MCP server via MCPClient

MCP server processes the request and returns a response

Agent prints the result back to the user

Setup & Run

Install dependencies:

pip install fastapi uvicorn requests


Start the MCP server:

python -m uvicorn mcp_server:app --reload


In a new terminal, start the agent:

python agent_host.py


Try example queries:

weather in Bangalore
what is MCP
search for AI
tell me about Python


Exit:

exit

Highlights

Fully offline demonstration of MCP-based agent architecture

Shows how AI agents can interact with tools and databases locally

Easy to extend with new tools or database entries