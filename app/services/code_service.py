import json
from app.retrieval.retriever import get_retriever
from app.llm.llm import get_llm
from app.utils.file_manager import safe_write
from app.services.git_service import commit_changes


def generate_and_apply(query: str):
    try:
        retriever = get_retriever()
        llm = get_llm(json_mode=True)

        docs = retriever.invoke(query)
        context = "\n".join([d.page_content for d in docs])

        prompt = f"""
[INST]
You are a specialized AI that ONLY outputs JSON for file updates. 
DO NOT speak. DO NOT explain. DO NOT output markdown.
ONLY return a single JSON object with the following structure:
{{
  "file_path": "the/path/to/file.py",
  "code": "the FULL and COMPLETE content of the file"
}}

CONTEXT:
{context}

TASK:
{query}
[/INST]
"""

        response = llm.invoke(prompt)
        with open("data/last_response.txt", "w", encoding="utf-8") as f:
            f.write(response)

        print(f"RAW RESPONSE length: {len(response)}", flush=True)

        def safe_json_parse(text):
            text = text.strip()
            # Still clean Python-style escapes LLMs sometimes produce inside JSON
            text = text.replace("\\'", "'")
            
            # If the LLM still wrapped it in markdown in JSON mode (unlikely but possible)
            if "```json" in text:
                text = text.split("```json")[-1].split("```")[0].strip()
            elif "```" in text:
                text = text.split("```")[-1].split("```")[0].strip()
            
            return json.loads(text)

        data = safe_json_parse(response)
        
        if not isinstance(data, dict) or "file_path" not in data or "code" not in data:
            return {
                "error": "LLM response is JSON but missing required schema.",
                "json_data": data
            }

        safe_write(data["file_path"], data["code"])
        commit_changes(f"AI Update: {query[:50]}")

        return {
            "file_path": data.get("file_path", ""),
            "code": data.get("code", "")
        }
    except Exception as e:
        import traceback
        return {"error": str(e), "traceback": traceback.format_exc()}