from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import sys

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            'math':{
                "command": sys.executable,
                "args":[
                    "MathServer.py"
                ],
                "transport":"stdio"
            },
            'weather':{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable-http"
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(
        model="llama-3.3-70b-versatile"
    )
    agent = create_react_agent(
        model, tools
    )

    math_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is 3 + 5 * 17"}]})
    print(math_response["messages"][-1].content)

    weather_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather in New York?"}]})
    print(weather_response["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())