import requests

class MCPClient:
    def __init__(self, server_url):
        self.server_url = server_url.rstrip("/")

    def call_tool(self, tool, **params):
        """
        Call MCP server tool (weather or search_db)
        """
        payload = {"tool": tool, "params": params}
        response = requests.post(f"{self.server_url}/mcp_tool", json=payload)
        return response.json()
