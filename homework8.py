import logging
from pywebio.input import input, TEXT
from pywebio.output import put_text, put_success, put_error

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def quiz_app():
    user_name = input("Добро пожаловать на викторину! Как вас зовут?", type=TEXT).strip()
    logger.info(f"Пользователь {user_name} начал викторину.")

    questions = [
        ("Какая планета самая большая в Солнечной системе?", "юпитер"),
        ("Сколько континентов на Земле?", "7"),
        ("Как именуется столица Франции?", "париж"),
        ("Какой металл является основным в производстве алюминиевой фольги?", "алюминий"),
        ("Сколько цветов в радуге?", "7"),
    ]

    correct_answers = 0

    for i, (question, correct_answer) in enumerate(questions, start=1):
        user_answer = input(f"Вопрос {i}: {question}", type=TEXT).strip().lower()  # Приведение к нижнему регистру
        if user_answer == correct_answer:
            put_success("Правильно!")
            correct_answers += 1
            logger.debug(f"Пользователь {user_name} ответил верно на вопрос {i}: {question}")
        else:
            put_error("Неправильно!")
            logger.debug(
                f"Пользователь {user_name} ответил неправильно на вопрос {i}: {question}. Ответ: {user_answer}")

    total_questions = len(questions)
    percentage = (correct_answers / total_questions) * 100

    put_text(f"{user_name}, вы набрали {correct_answers} из {total_questions} баллов.")
    put_text(f"Это {percentage:.2f}% правильных ответов.")

    logger.info(
        f"Пользователь {user_name} завершил викторину с результатом {correct_answers}/{total_questions} ({percentage:.2f}%).")


if __name__ == "__main__":
    from pywebio import start_server

    start_server(quiz_app, port=8080)
