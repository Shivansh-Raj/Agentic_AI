# Understanding `client.py` and MCP

## What is `client.py`?
`client.py` is an application that uses the **Model Context Protocol (MCP)** to give a large language model (in this case, Groq's LLaMA 3.3 model) the ability to access external tools running on different servers. 

Rather than the AI model trying to guess the weather or calculate math entirely in its head, it routes those requests to actual functions running outside of its environment.

## The Purpose and Benefits

### 1. Separation of Concerns (Modularity)
Instead of putting all your python functions inside one gigantic AI script, you divide them:
- **MathServer**: Handles mathematical calculations. Runs as its own independent process (connected via Standard I/O or `stdio`).
- **WeatherServer**: Handles fetching weather data. Runs independently on a local HTTP port (connected via `streamable-http`).

### 2. Universal Tool Access via MCP
MCP is like a standard "USB cable" for AI. 
If a server follows the MCP standard, any AI agent can connect to it and automatically understand what tools it offers. In `client.py`, the AI connects to both servers, asks them "what can you do?", and merges their capabilities dynamically.

### 3. Agentic Routing using LangGraph
`client.py` uses LangGraph's `create_react_agent`. The agent loop does the following:
1. It receives your question (e.g. "What is 3 + 5 * 17").
2. It looks at the united list of tools it got from the MCP servers.
3. It realizes it needs to call `add` and `multiply` to answer perfectly!
4. It tells `client.py` to route the execution request to the **MathServer**.
5. Once the MathServer returns `88`, the AI formulates the final answer to the user.

## Why use this over regular LangChain Tools?
If you build your tools as MCP servers, they become completely independent of LangChain. You could use the exact same `MathServer` and `WeatherServer` with a completely different framework, or even plug it directly into Claude Desktop or other enterprise LLM tools, without changing the server code at all.
