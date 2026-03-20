import json
from app.retrieval.retriever import get_retriever
from app.llm.llm import get_llm
from app.utils.file_manager import safe_write
from app.services.git_service import commit_changes


def generate_and_apply(query: str):
    retriever = get_retriever()
    llm = get_llm()

    docs = retriever.get_relevant_documents(query)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
You are a senior engineer.

Context:
{context}

Task:
{query}

Return JSON:
{{
  \"file_path\": \"repo/file.py\",
  \"code\": \"updated code\"
}}
"""

    response = llm.invoke(prompt)
    data = json.loads(response)

    safe_write(data["file_path"], data["code"])
    commit_changes("AI code update")

    return {"status": "success", "file": data["file_path"]}