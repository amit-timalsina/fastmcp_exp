from fastmcp import Client
import asyncio
async def main():
    # Connect via stdio to a local script
    async with Client("server.py") as client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")
        result = await client.call_tool("hello", {"name": "John"})
        print(f"Result: {result}")
        result = await client.call_tool("multiply", {"a": 5, "b": 3})
        print(f"Result: {result}")
        result = await client.read_resource("data://config")
        print(f"Result: {result}")
        result = await client.read_resource("users://123/profile")
        print(f"Result: {result}")
        result = await client.get_prompt("analyze_data", {"data_points": [1, 2, 3, 4, 5]})
        print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())