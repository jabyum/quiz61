from database import get_db
from database.models import *

# дз добавление вопросов
def add_question_db():
    ...
# дз вывод 20 вопросов данной сложности
def get_20_questions_db():
    ...

# получение таблицы лидеров
def get_top5_db(level):
    with next(get_db()) as db:
        top5 = db.query(Rating).filter_by(level=level).order_by(Rating.correct_answers.desc()).all()
        #[[id, user_id, correct_answer, level],[id, user_id, correct_answer, level],[id, user_id, correct_answer, level]....]
        filter_info = [[rating.user_id, rating.correct_answers] for rating in top5]
        #[[user_id, correct_answer],[user_id, correct_answer],,[user_id, correct_answer],,[user_id, correct_answer],]
        return filter_info[:5]



