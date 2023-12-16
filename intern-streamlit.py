import streamlit as st
import requests

def search_github_repositories(keyword, username):
    url = f'https://api.github.com/search/repositories?q={keyword}+user:{username}&per_page=50'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        result = [{"name": item['name'], "description": item['description'], "url": item['html_url']} for item in data['items']]
        return result
    else:
        print("検索に失敗")
col1, col2 = st.columns(2)
with col1:
    keyword = st.text_input("keyword")
with col2:
    username = st.text_input("username")
if st.button("検索"):
    results = search_github_repositories(keyword, username)
    for r in results:
        with st.expander(r['name']):
            st.write(r['description'])