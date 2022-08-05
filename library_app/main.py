from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from library_app.routers import users, books
from library_app.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="library_app/static"), name="static")

templates = Jinja2Templates(directory="library_app/templates")

inventory = [{"bookID":"35460","title":"Star Wars: Clone Wars Adventures  Volume 6","authors":"W. Haden Blackman/Matt Fillbach/Shawn Fillbach/Ronda Pattison/Mike Kennedy/Stewart McKenney/Rick Lacy/Dan Jackson/Michael David Thomas/Joshua Elliott","average_rating":"3.78","isbn":"1593075677","isbn13":"9781593075675","language_code":"eng","  num_pages":"88","ratings_count":"176","text_reviews_count":"10","publication_date":"8/23/2006","publisher":"Dark Horse Books"},{"bookID":"17828","title":"The Master and Margarita","authors":"Mikhail Bulgakov/Michael Karpelson","average_rating":"4.30","isbn":"1411683056","isbn13":"9781411683051","language_code":"eng","  num_pages":"332","ratings_count":"493","text_reviews_count":"47","publication_date":"4/1/2006","publisher":"Lulu Press"},{"bookID":"34908","title":"Here  There Be Dragons (Chronicles of the Imaginarium Geographica  #1)","authors":"James A. Owen","average_rating":"3.86","isbn":"1416912274","isbn13":"9781416912279","language_code":"en-US","  num_pages":"326","ratings_count":"10103","text_reviews_count":"917","publication_date":"9/26/2006","publisher":"Simon & Schuster Books for Young Readers"},{"bookID":"40395","title":"A Princess of Mars (Barsoom  #1)","authors":"Edgar Rice Burroughs/John Seelye","average_rating":"3.81","isbn":"0143104888","isbn13":"9780143104889","language_code":"eng","  num_pages":"186","ratings_count":"38926","text_reviews_count":"2355","publication_date":"1/30/2007","publisher":"Penguin Books"}]

app.include_router(users.router)
app.include_router(books.router)

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})