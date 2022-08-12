from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from library_app.routers import members, books, templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="library_app/static"), name="static")

app.include_router(members.router)
app.include_router(books.router)
app.include_router(templates.router)