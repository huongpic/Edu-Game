import streamlit as st
import random

# Thiết lập giao diện Streamlit
st.set_page_config(page_title="Math Game for Grade 3", layout="centered")
st.title("Math Game for Grade 3 🎲")
st.markdown("Chọn đáp án đúng để ghi điểm!")

# Khởi tạo session state
if "score" not in st.session_state:
    st.session_state.score = 0
if "question" not in st.session_state:
    st.session_state.question = ""
if "correct_answer" not in st.session_state:
    st.session_state.correct_answer = 0
if "choices" not in st.session_state:
    st.session_state.choices = []
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "selected_answer" not in st.session_state:
    st.session_state.selected_answer = None

# Hàm tạo câu hỏi mới
def generate_question():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(["+", "-", "*", "//"])

    if operation == "+":
        st.session_state.correct_answer = num1 + num2
        st.session_state.question = f"{num1} + {num2} = ?"
    elif operation == "-":
        num1, num2 = max(num1, num2), min(num1, num2)
        st.session_state.correct_answer = num1 - num2
        st.session_state.question = f"{num1} - {num2} = ?"
    elif operation == "*":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        st.session_state.correct_answer = num1 * num2
        st.session_state.question = f"{num1} × {num2} = ?"
    else:  # //
        num2 = random.randint(1, 10)
        num1 = num2 * random.randint(1, 10)
        st.session_state.correct_answer = num1 // num2
        st.session_state.question = f"{num1} ÷ {num2} = ?"

    # Tạo 4 đáp án
    st.session_state.choices = [st.session_state.correct_answer]
    while len(st.session_state.choices) < 4:
        wrong_answer = st.session_state.correct_answer + random.randint(-10, 10)
        if wrong_answer != st.session_state.correct_answer and wrong_answer >= 0 and wrong_answer not in st.session_state.choices:
            st.session_state.choices.append(wrong_answer)
    random.shuffle(st.session_state.choices)
    st.session_state.feedback = ""
    st.session_state.selected_answer = None

# Tạo câu hỏi ban đầu nếu chưa có
if not st.session_state.question:
    generate_question()

# Hiển thị điểm số
st.markdown(f"**Score: {st.session_state.score}**")

# Hiển thị câu hỏi
st.markdown(f"<h3 class='text-center'>{st.session_state.question}</h3>", unsafe_allow_html=True)

# Xử lý lựa chọn đáp án
cols = st.columns(2)
for i, choice in enumerate(st.session_state.choices):
    with cols[i % 2]:
        if st.button(str(choice), key=f"choice_{i}"):
            st.session_state.selected_answer = choice

# Xử lý logic khi chọn đáp án
if st.session_state.selected_answer is not None:
    if st.session_state.selected_answer == st.session_state.correct_answer:
        st.session_state.feedback = '<span style="color:green;">Correct! Great job!</span>'
        st.session_state.score += 10
        generate_question()
    else:
        st.session_state.feedback = '<span style="color:red;">Try again!</span>'
        generate_question()

# Hiển thị phản hồi
if st.session_state.feedback:
    st.markdown(f"<div class='text-center mt-4 text-lg'>{st.session_state.feedback}</div>", unsafe_allow_html=True)

# Thêm CSS tùy chỉnh
st.markdown("""
<style>
button {
    font-size: 1.2rem;
    width: 100%;
    background-color: #3B82F6;
    color: white;
    padding: 1rem;
    border-radius: 0.5rem;
}
button:hover {
    background-color: #2563EB;
}
</style>
""", unsafe_allow_html=True)
