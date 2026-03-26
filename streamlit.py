import streamlit as st
import requests
import json

# Настройка страницы
st.set_page_config(
    page_title="Text Processing App",
    page_icon="📝",
    layout="centered"
)

# Заголовок приложения
st.title("📝 Text Processing Application")
st.markdown("---")


# Функция для отправки GET запроса
def send_get_request(text):
    """Отправляет текст через GET запрос на /{text}"""
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
    return "Please enter some text"


# Функция для отправки POST запроса
def send_post_request(text):
    """Отправляет текст через POST запрос на /predict/"""
    if text:
        try:
            # Замените localhost:8000 на ваш реальный адрес сервера
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
    return "Please enter some text"


# Основной интерфейс
st.subheader("✍️ Input Text")

# Поле для ввода текста
user_input = st.text_area(
    "Enter your text here:",
    height=150,
    placeholder="Type or paste your text here...",
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
        "📨 Оценить текст POST",
        type="primary",
        use_container_width=True
    )


# Основной интерфейс
st.subheader("✍️ Несколько текстов!")

# Поле для ввода текста
user_input1 = st.text_area(
    "Enter your text here:",
    height=150,
    placeholder="Введите тексты через /...",
    key="text_input"
)

col3 = st.columns(1)


with col3:
    # Кнопка для POST запроса
    postSeveral_button = st.button(
        "📨 Оценить несколько текстов! POST",
        type="primary",
        use_container_width=True
    )


st.markdown("---")

# Обработка GET запроса
if postSeveral_button:
    if user_input.strip():
        with st.spinner("Sending POST request..."):
            result = send_get_request(user_input)

            st.subheader("📤 GET Request Result")
            st.success("Request sent successfully!")

            # Отображение результата
            with st.container():
                st.markdown("**Response:**")
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.code(result, language="json")
    else:
        st.warning("⚠️ Please enter some text before sending")

if get_button:
    if user_input.strip():
        with st.spinner("Sending GET request..."):
            result = send_get_request(user_input)

            st.subheader("📤 GET Request Result")
            st.success("Request sent successfully!")

            # Отображение результата
            with st.container():
                st.markdown("**Response:**")
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.code(result, language="json")
    else:
        st.warning("⚠️ Please enter some text before sending")



# Обработка POST запроса
if post_button:
    if user_input.strip():
        with st.spinner("Sending POST request..."):
            result = send_post_request(user_input)

            st.subheader("📨 POST Request Result")
            st.success("Request sent successfully!")

            # Отображение результата
            with st.container():
                st.markdown("**Response:**")
                if isinstance(result, dict):
                    st.json(result)
                else:
                    st.code(result, language="json")
    else:
        st.warning("⚠️ Please enter some text before sending")

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