import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(
        command="python", 
        args=["your_mcp_server.py"]  # replace with actual MCP server script
    )

    async with stdio_client(params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            
            # Example: list tools
            tools = await session.list_tools()
            print("Tools available from MCP server:")
            for t in tools:
                print(f"- {t.name}: {t.description}")

if __name__ == "__main__":
    asyncio.run(main())
