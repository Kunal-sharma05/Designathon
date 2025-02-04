from fastapi import FastAPI
from db.database import engine
from routers.user import router as user_router
from routers.vocabulary_lesson import router as vocabulary_router
from routers.speech_lesson import router as speech_router
from routers.practice_test import router as practice_router
from routers.test_report import router as test_router
from routers.pronunciation_lesson import router as pronunciation_router
from db.database import base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

base.metadata.create_all(bind=engine)

app.include_router(user_router, tags=["User"])
app.include_router(vocabulary_router, tags=["Vocabulary Lessons"])
app.include_router(practice_router, tags=["Practice Test"])
app.include_router(pronunciation_router, tags=["Pronunciation Lesson"])
app.include_router(test_router, tags=["Test Reports"])
app.include_router(speech_router, tags=["Speech Lessons"])
