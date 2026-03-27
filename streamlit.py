import streamlit as st
import requests
import json
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Оценка текста",
    page_icon="📝",
    layout="centered"
)

# Заголовок приложения
st.title("📝 Приложение для оценки текста")
st.markdown("---")


# Функция для отправки GET запроса
def send_get_request(text):
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


# Функция для отправки POST запроса
def send_post_request(text):
    if text:
        try:
            url = "http://localhost:8000/predict/"

            # Отправляем POST запрос с JSON телом
            payload = {"text": text}
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                return response.json() if response.headers.get('content-type') == 'application/json' else response.text
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Connection error: {str(e)}"
    return "Пожалуйста, введите текст"

def send_post_several_text_request(text):
    if text:
        try:
            url = "/predict_multiple/"
                # Ввести url для нескольких текстов
                # "http://localhost:8000/predict/batch"

            print("Работает!!!")

            # Отправляем POST запрос с JSON телом
            payload = {"text": text}
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                return response.json() if response.headers.get('content-type') == 'application/json' else response.text
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Connection error: {str(e)}"
    return "Пожалуйста, введите текст"


# Основной интерфейс
st.subheader("✍️ Ввод текста")

# Поле для ввода текста
user_input = st.text_area(
    "Enter your text here:",
    height=150,
    placeholder="Введите или вставьте свой текст...",
    key="text_input"
)

# Создание двух колонок для кнопок
col1, col2 = st.columns(2)

with col1:
    # Кнопка для GET запроса
    get_button = st.button(
        "📤 Оценить текст GET",
        type="primary",
        use_container_width=True
    )

with col2:
    # Кнопка для POST запроса
    post_button = st.button(
        "📨 Оценить текст через POST запрос",
        type="primary",
        use_container_width=True
    )


# Основной интерфейс
st.subheader("✍️ Несколько текстов!")

# Поле для ввода текста
user_input1 = st.text_area(
    "Enter your text here:",
    height=150,
    placeholder="Введите или вставьте свои тексты через /...",
    key="text_input_several"
)





    # Кнопка для POST запроса
postSeveral_button = st.button(
    "📨 Оценить несколько текстов! Через POST запрос",
    type="primary",
    use_container_width=True
)


st.markdown("---")

# Обработка GET запроса
if postSeveral_button:
    if user_input1.strip():
        with st.spinner("Отправляем POST запрос..."):

            textU = user_input1.split('/')

            result = send_get_request(textU)

            st.subheader("📨 Результат POST запроса")
            st.success("Запрос успешно отправлен!")

            # Отображение результата
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

            st.subheader("📤  Результат GET запроса")
            st.success("Запрос успешно отправлен!")

            # Отображение результата
            with st.container():
                st.markdown("**Ответ:**")
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.code(result, language="json")
    else:
        st.warning("⚠️ Пожалуйста, введите текст перед отправкой")



# Обработка POST запроса
if post_button:
    if user_input.strip():
        with st.spinner("Отправляем POST запрос..."):
            result = send_post_request(user_input)

            st.subheader("📨 Результат POST запроса")
            st.success("Запрос успешно отправлен!")

            # Отображение результата
            with st.container():
                st.markdown("**Response:**")
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.code(result, language="json")
    else:
        st.warning("⚠️ Пожалуйста, введите текст перед отправкой")

# Дополнительная информация



# Стилизация (опционально)
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