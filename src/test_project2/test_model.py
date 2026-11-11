import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

api_key = os.getenv("DASHSCOPE_API_KEY")
base_url = os.getenv("DASHSCOPE_BASE_URL")

if not api_key or not base_url:
    raise RuntimeError(
        "请在 .env 中设置 DASHSCOPE_API_KEY 和 DASHSCOPE_BASE_URL"
    )

llm = ChatOpenAI(
    model="qwen3.8-flash",
    api_key=api_key,
    base_url=base_url,
    timeout=30,
)

response = llm.invoke("请只回复：连接成功")
print(response.content)