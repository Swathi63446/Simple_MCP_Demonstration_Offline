from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Allow cross-origin requests if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load mock database for search tool
with open("mock_database.json", "r") as f:
    mock_db = json.load(f)

@app.post("/mcp_tool")
async def mcp_tool(request: Request):
    data = await request.json()
    tool = data.get("tool")
    params = data.get("params", {})

    if tool == "weather":
        city = params.get("city", "Unknown")
        # Mock weather data
        weather_info = {
            "city": city,
            "temperature": "25°C",
            "condition": "Sunny"
        }
        return {"result": weather_info}

    elif tool == "search_db":
        keyword = params.get("keyword", "").lower()
        results = []
        for entry in mock_db:
            if keyword in entry["text"].lower():
                results.append(entry)
        if not results:
            results.append({"text": "No matching entries found."})
        return {"result": results}

    else:
        return {"result": f"Tool '{tool}' not recognized."}
