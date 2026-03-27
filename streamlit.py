import streamlit as st
import requests
import json
from typing import Union, List, Dict, Any

st.set_page_config(
    page_title="Оценка текста",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Приложение для оценки текста")
st.markdown("---")


def send_get_request(text: str) -> Union[Dict[str, Any], str]:
    """Send GET request to the server"""
    if text:
        try:
            url = f"http://localhost:8000/{text}"

            response = requests.get(url)

            if response.status_code == 200:
                return response.json() if response.headers.get('content-type') == 'application/json' else response.text
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Connection error: {str(e)}"
    return "Пожалуйста, введите текст"


def send_post_request(text: str) -> Union[Dict[str, Any], str]:
    """Send POST request to the server"""
    if text:
        try:
            url = "http://localhost:8000/predict/"

            payload = {"text": text}
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                return response.json() if response.headers.get('content-type') == 'application/json' else response.text
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Connection error: {str(e)}"
    return "Пожалуйста, введите текст"


def send_post_several_text_request(text: str) -> Union[Dict[str, Any], str]:
    """Send POST request for multiple texts"""
    if text:
        try:
            url = "http://localhost:8000/predict/batch"

            payload = {"texts": text}
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                return response.json() if response.headers.get('content-type') == 'application/json' else response.text
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Connection error: {str(e)}"
    return "Пожалуйста, введите текст"


st.subheader("✍️ Ввод текста")

user_input: str = st.text_area(
    "Enter your text here:",
    height=150,
    placeholder="Введите или вставьте свой текст...",
    key="text_input"
)

col1, col2 = st.columns(2)

with col1:
    get_button: bool = st.button(
        "📤 Оценить текст GET",
        type="primary",
        use_container_width=True
    )

with col2:
    post_button: bool = st.button(
        "📨 Оценить текст через POST запрос",
        type="primary",
        use_container_width=True
    )

st.subheader("✍️ Несколько текстов!")

user_input1: str = st.text_area(
    "Enter your text here:",
    height=150,
    placeholder="Введите или вставьте свои тексты через /...",
    key="text_input_several"
)

postSeveral_button: bool = st.button(
    "📨 Оценить несколько текстов! Через POST запрос",
    type="primary",
    use_container_width=True
)

st.markdown("---")

if postSeveral_button:
    if user_input1.strip():
        with st.spinner("Отправляем POST запрос..."):
            texts_list: List[str] = [t.strip() for t in user_input1.split('/') if t.strip()]
            result = send_post_several_text_request(texts_list)

            st.subheader("📨 Результат POST запроса (несколько текстов)")
            st.success("Запрос успешно отправлен!")

            with st.container():
                st.markdown("**Ответ:**")
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.code(result, language="json")
    else:
        st.warning("⚠️ Пожалуйста, введите текст перед отправкой")

if get_button:
    if user_input.strip():
        with st.spinner("Отправляем GET запрос..."):
            result = send_get_request(user_input)

            st.subheader("📤 Результат GET запроса")
            st.success("Запрос успешно отправлен!")

            with st.container():
                st.markdown("**Ответ:**")
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.code(result, language="json")
    else:
        st.warning("⚠️ Пожалуйста, введите текст перед отправкой")

if post_button:
    if user_input.strip():
        with st.spinner("Отправляем POST запрос..."):
            result = send_post_request(user_input)

            st.subheader("📨 Результат POST запроса")
            st.success("Запрос успешно отправлен!")

            with st.container():
                st.markdown("**Response:**")
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.code(result, language="json")
    else:
        st.warning("⚠️ Пожалуйста, введите текст перед отправкой")

st.markdown("""
<style>
.stButton button {
    font-weight: bold;
}
.stTextArea textarea {
    font-family: monospace;
}
</style>
""", unsafe_allow_html=True)