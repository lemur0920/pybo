from models import Question, Answer
from datetime import datetime
from database import SessionLocal

# q = Question(subject='FastAPI 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=datetime.now())
db = SessionLocal()
# q = db.get(Question, 2)
q = db.get(Question, 2)
a = Answer(question = q, content='네 자동으로 생성됩니다.', create_date=datetime.now())
# db.add(a)
# db.commit()
# db.delete(q)
# q.subject = 'FastAPI Model Question'
