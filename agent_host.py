"""
Offline MCP Agent Host
Fully offline. No OpenAI API calls required.
Handles:
- Weather queries via MCP server
- Search queries via MCP server
- General queries via mock_database.json
"""

import os
import json
from mcp_client import MCPClient

# Load mock database
with open("mock_database.json", "r") as f:
    db = json.load(f)

def search_mock_database(query):
    """
    Return first matching entry in mock database containing a keyword from query.
    """
    lower_query = query.lower()
    for entry in db:
        if any(word in entry["text"].lower() for word in lower_query.split()):
            return entry["text"]
    return "Sorry, I couldn't find an answer in the mock database."

def process_query(query, client):
    lower = query.lower()

    # WEATHER TOOL
    if "weather in" in lower:
        try:
            city = lower.split("weather in")[-1].strip()
            tool_res = client.call_tool("weather", city=city)
            return f"Here is the weather info: {tool_res['result']}"
        except Exception as e:
            return f"Error fetching weather: {e}"

    # SEARCH TOOL
    elif "search for" in lower or "find" in lower:
        try:
            if "search for" in lower:
                keyword = lower.split("search for")[-1].strip()
            else:
                keyword = lower.split("find")[-1].strip()
            tool_res = client.call_tool("search_db", keyword=keyword)
            return f"Found entries: {tool_res['result']}"
        except Exception as e:
            return f"Error searching database: {e}"

    # GENERAL QUERY: search mock database
    else:
        return search_mock_database(query)

if __name__ == "__main__":
    # MCP server URL (default: localhost)
    server_url = os.getenv("MCP_SERVER_URL", "http://127.0.0.1:8000")
    client = MCPClient(server_url)

    print("Welcome to the Offline MCP-based Agent host.")
    print("Type 'exit' or 'quit' to stop.\n")

    while True:
        inp = input("You: ").strip()
        if inp.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        out = process_query(inp, client)
        print("Agent:", out)
