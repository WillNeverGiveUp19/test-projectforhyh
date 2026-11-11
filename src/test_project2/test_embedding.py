import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

api_key = os.getenv("DASHSCOPE_API_KEY")
base_url = os.getenv("DASHSCOPE_BASE_URL")

if not api_key or not base_url:
    raise RuntimeError(
        "请在 .env 中设置 DASHSCOPE_API_KEY 和 DASHSCOPE_BASE_URL"
    )

embeddings = OpenAIEmbeddings(
    model="qwen3.7-text-embedding",
    api_key=api_key,
    base_url=base_url,
    check_embedding_ctx_length=False,
)

vectors = embeddings.embed_documents([
    "设备运行正常",
    "设备出现异常告警",
])

if len(vectors) != 2 or not vectors[0]:
    raise RuntimeError("Embedding 返回结果为空或数量不正确")

print(f"连接成功：返回 {len(vectors)} 条向量，向量维度为 {len(vectors[0])}")