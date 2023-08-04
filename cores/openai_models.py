import requests
import streamlit as st

@st.cache_data(ttl=172800)
def get_gpt_models(api_key):
    headers = {
        'authority': 'api.openai.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,id;q=0.8,es;q=0.7',
        'authorization': f'Bearer {api_key}',
        'origin': 'https://api.openai.com/v1/models',
        'referer': 'https://api.openai.com/v1/models',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    url = 'https://api.openai.com/v1/models'
    response = requests.get(url, headers=headers)

    rsp = response.json()
    return [model['id'] for model in rsp['data'] if 'gpt' or 'davinci' in model['id'].lower()]
