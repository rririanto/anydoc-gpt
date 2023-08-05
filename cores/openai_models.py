import requests
import streamlit as st


def get_gpt_models(api_key):
    '''
    Uncomment this if you want to get realtime models
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
    print([model['id'] for model in rsp['data']
          if 'gpt' or 'davinci' in model['id'].lower()])
    return [model['id'] for model in rsp['data'] if 'gpt' or 'davinci' in model['id'].lower()]
    '''
    return ['text-davinci-001', 'text-search-curie-query-001', 'davinci', 'text-babbage-001', 'curie-instruct-beta', 'text-davinci-003', 'davinci-similarity', 'code-davinci-edit-001', 'text-similarity-curie-001', 'text-embedding-ada-002', 'ada-code-search-text', 'text-search-ada-query-001', 'babbage-search-query', 'ada-similarity', 'gpt-3.5-turbo', 'whisper-1', 'text-search-ada-doc-001', 'text-search-babbage-query-001', 'code-search-ada-code-001', 'curie-search-document', 'text-search-davinci-query-001', 'text-search-curie-doc-001', 'gpt-3.5-turbo-0301', 'babbage-search-document', 'babbage-code-search-text', 'davinci-instruct-beta', 'davinci-search-query', 'text-similarity-babbage-001', 'text-davinci-002', 'code-search-babbage-text-001', 'babbage', 'text-search-davinci-doc-001', 'code-search-ada-text-001', 'gpt-3.5-turbo-16k-0613', 'gpt-3.5-turbo-16k', 'ada-search-query', 'text-similarity-ada-001', 'ada-code-search-code', 'ada', 'text-davinci-edit-001', 'davinci-search-document', 'curie-search-query', 'babbage-similarity', 'ada-search-document', 'text-ada-001', 'text-similarity-davinci-001', 'curie', 'curie-similarity', 'gpt-3.5-turbo-0613', 'babbage-code-search-code', 'code-search-babbage-code-001', 'text-search-babbage-doc-001', 'text-curie-001']