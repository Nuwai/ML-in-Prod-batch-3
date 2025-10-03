
```bash

uv init
uv venv

ls -la
source .venv/bin/activate


uv add mcp arxiv
uv add anthropic python-dotenv nest_asyncio
 
```



### 2. start inspector server
```bash
npx @modelcontextprotocol/inspector uv run research_server.py
```



### 3. Start Client and Server
```bash
# run MCP client
uv run mcp_chatbot.py
```





## Connecting to Reference Servers

Check connect_refer_server.py
### Open-source MCP Servers
In this [repo](https://github.com/modelcontextprotocol/servers), you can find a collection of reference implementations for the MCP servers, as well as references to community built servers and additional resources. You will use two of the reference servers to integrate their tools in your MCP chatbot:
- [fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch): provides the `fetch` tool which fetches a URL from the internet and extracts its contents as markdown.
- [filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem): provides several tools for interacting with the files and directories within a directory that you specify.

You can check the readme file of each server to check the features they expose and how to run them.  

### Server configuration sample
```json
 {
        "mcpServers": {
            
            "filesystem": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    "."
                ]
            },
            
            "research": {
                "command": "uv",
                "args": ["run", "research_server.py"]
            },
            
            "fetch": {
                "command": "uvx",
                "args": ["mcp-server-fetch"]
            }
        }
    }
```


### Test fetch mcp server
tell me about this man https://github.com/tharhtetsan

