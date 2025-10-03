

### start inspector server for Tools, Prompt template
```bash
npx @modelcontextprotocol/inspector uv run research_server.py
```

### Start Client and Server
```bash


# run MCP client
uv run mcp_chatbot.py
```

### Test set
tell me about this man url https://github.com/tharhtetsan
what is 1+1

search about 3 MLOps latest papers and summize for me

@folders

@mlops

/prompts 

/prompt fetch url=https://github.com/tharhtetsan

/prompt generate_search_prompt topic=yolov11 num_papers=2


## Add to Cloude


```bash
# check uv path
which uv
eg: /opt/anaconda3/envs/ths_dev/bin/uv
```


edit claude_desktop_config.json
```json
{
  "mcpServers": {
    "research_server": {
      "command": "/opt/anaconda3/envs/ths_dev/bin/uv",
      "args": [
        "--directory",
        "/Users/tharhtet/Documents/github/ML-in-Prod-batch-3/7_App_development/mcp/mcp_intro/resourceAndPrompt_template",
        "run",
        "research_server.py"
      ]
    }
  }
}
```