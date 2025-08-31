# server.py
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.resource("data://config")
def get_config() -> dict:
    """Provides the application configuration."""
    return {"theme": "dark", "version": "1.0"}

@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> dict:
    """Retrieves a user's profile by ID."""
    return {"id": user_id, "name": f"User {user_id}", "status": "active"}

@mcp.prompt
def analyze_data(data_points: list[float]) -> str:
    """Creates a prompt asking for analysis of numerical data."""
    formatted_data = ", ".join(str(point) for point in data_points)
    return f"Please analyze these data points: {formatted_data}"

if __name__ == "__main__":
    mcp.run()  # Default: uses STDIO transport