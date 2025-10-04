Today Date (04-10-2025)
python sdk for Streamable HTTP was in active development. So we will use with SSE with port 8001.



Streamable HTTP: You can also use FastMCP to create a remote server using the transport "Streamable HTTP". The code would be again the same for tool, resource and prompt definitions. But when you run the server, you specify the transport as:

mcp.run(transport="streamable-http")
And when you initiate the FastMCP server you have two options:

# Stateful server (maintains session state)
```python
mcp = FastMCP("research")
```

# Stateless server (no session persistence)
```python
mcp = FastMCP("research", stateless_http=True)
```
Stateless can be used when you want the server to handle simple, independent requests (no memory of previous interactions with the same client). Stateful can be used when you want the server to handle multiple requests that are part of a workflow and you want the server to remember the Client information and context across multiple request


## Test with inspector
### start inspector server for Tools, Prompt template
```bash
npx @modelcontextprotocol/inspector uv run research_server.py
```
Transport type : sse
URL : http://localhost:8001/sse

