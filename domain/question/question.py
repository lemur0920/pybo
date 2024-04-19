from models import Question, Answer
from datetime import datetime
from database import SessionLocal


db = SessionLocal()
q = Question(subject='FastAPI 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=datetime.now())
# q = db.get(Question, 2)
db.add(q)
db.commit()
print(q.id)
db.close()
# q.subject = 'FastAPI Model Question'
