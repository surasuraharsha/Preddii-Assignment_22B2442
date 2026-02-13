from groq import Groq


client = Groq(api_key="")  # Add your API Key here 

def extract_vehicle_specs(context, query):
    prompt = f"""
You are a vehicle service manual assistant.

Context:
{context}

Question:
{query}
Rules:
- Answer ONLY using the provided context
- Do NOT use prior knowledge or external information
- If a value is not explicitly present in the context, do NOT include it in the output
- Do NOT guess, infer, assume, or estimate
- For Torque,there are 3 possible unit values.at max 2 unit values are available in pdf. extract them only if exist
- Do NOT invent part numbers, fluids, materials, or specifications
- If query is expecting textual answer like reasons, actions etc, return in textual explanation format
- if value is - , tell value not mentioned in pdf
- If no valid answer exists in the context, return an empty JSON array []
- If a specification is given in multiple units, include all units as separate JSON objects
- Do NOT mix or convert units
- Use the exact JSON schema provided
- Use consistent component naming and spec_type values
- Return only the minimum number of JSON objects required
- Ignore procedural text, notes, and unrelated specifications
- Return ONLY valid JSON

format for textual explanation:
  [
  {{
    "Answer": ""
  }}
]


format for ranges of values:
[
  {{
    "component": "",
    "spec_type": "",
    "Range": "",
    "unit": ""
  }}
]


Format for TORQUE and Capacities and for other metrics:
[
  {{
    "component": "",
    "spec_type": "",
    "value": "",
    "unit": ""
  }}
]

format for part number or any non-metric items(which have no units) :
[
  {{
    "component": "",
    "spec_type": "",
    "value": ""
  }}
]




"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You extract structured vehicle specifications."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message.content