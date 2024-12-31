import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "7d132c12-055f-454a-87c4-c85c75ab98a1"
FLOW_ID = "471ab90d-4f55-4463-bb43-cd781d5e7cbd"
APPLICATION_TOKEN = APPLICATION_TOKEN = os.environ.get("APP_TOKEN")
ENDPOINT = "ragdev"  # The endpoint name of the flow

def run_flow(message: str) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{ENDPOINT}"

    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
    }

    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    st.title("Happy New Year Natan,Lets Create a Quest")
    
    message = st.text_area("Mention What Kind Of Quest you Desire To be Generated", placeholder="Put details here")
    
    if st.button("Generate Quest"):
        if not message.strip():
            st.error("Error? Contact DECA asap")
            return
    
        try:
            with st.spinner("Generating Quest,Breathe In Breathe Out"):
                response = run_flow(message)
            
            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()