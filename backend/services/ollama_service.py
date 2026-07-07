import requests


class OllamaService:

    def explain(self, best_model, metrics):

        prompt = f"""
You are a Senior Data Scientist.

The best model selected is:

{best_model}

Model Metrics:

{metrics}

Explain:

1. Why this model is the best.
2. Compare it with the other models.
3. Mention strengths and weaknesses.
4. Suggest how to improve the model.
5. Keep the explanation simple for beginners.

Return in markdown format.
"""

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        response.raise_for_status()

        return response.json()["response"]
    

    
    def chat(self, data):

        prompt = f"""
    You are Insight AutoML AI Assistant.

    You are an expert Data Scientist and Machine Learning Engineer.

    Here is the dataset information:

    Dataset Shape:
    {data["dataset_info"]["shape"]}

    Columns:
    {data["dataset_info"]["columns"]}

    Missing Values:
    {data["dataset_info"]["missing_values"]}

    Data Types:
    {data["dataset_info"]["dtypes"]}

    Statistics:
    {data["dataset_info"]["statistics"]}

    Model Performance:
    {data["metrics"]}

    User Question:
    {data["question"]}

    Rules:
    - Answer only using the information provided.
    - Explain in simple English.
    - If the user asks for suggestions, provide practical ML advice.
    - Format the response using Markdown.
    """

   

        response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3",
                    "prompt": prompt,
                    "stream": False
                }
            )

        response.raise_for_status()

        return response.json()["response"]