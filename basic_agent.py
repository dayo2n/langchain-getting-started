# Build a basic agent

import truststore                                                                                                                                 
truststore.inject_into_ssl()

from dotenv import load_dotenv # .env 파일 정의시
from langchain.agents import create_agent

load_dotenv()

def get_weather(city: str) -> str:
  """Get weather for a given city."""
  return f"It's always sunny in {city}!"
  
agent = create_agent(
  model="google_genai:gemini-2.5-flash-lite",
  tools=[get_weather],
  system_prompt="You are a helpful assistant",
)

result = agent.invoke(
  {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)

print(result["messages"][-1].content_blocks)
