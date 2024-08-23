import requests
from fastapi import HTTPException
from dotenv import load_dotenv
from .config import configure_headers, configure_api_url

url = configure_api_url()
headers = configure_headers()

def query(prompt):
    try:
        payload = {"inputs": prompt}
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error querying API: {str(e)}")
