import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "llama3.2:3b"


def generate_insight(question, sql, columns, rows):

    # Limit rows sent to the model
    sample_rows = rows[:20]

    data = {
        "columns": columns,
        "rows": sample_rows
    }

    prompt = f"""
You are a Senior HR Data Analyst.

Your job is to analyze SQL query results and provide a concise business insight.

User Question:
{question}

SQL Used:
{sql}

Query Result:
{json.dumps(data, indent=2, default=str)}

Rules:

- Never invent numbers.
- Use ONLY the SQL result provided.
- Keep the response under 150 words.
- If there is no data, clearly say so.
- Be professional and business-focused.

Use exactly this format:

📊 HR Insight

(2-3 sentences summarizing the result.)

🔍 Possible Reason

(Explain the likely HR/business reason.)

💡 Recommendation

(Provide one practical recommendation.)
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()

    return response.json()["response"].strip()