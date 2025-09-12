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