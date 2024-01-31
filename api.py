from fastapi import FastAPI, HTTPException
from data import books

app = FastAPI()

@app.get("/book/id:{id}")
def get_book(id: int):
    for book in books:
        if book['id'] == id:
            return book
    else:
        raise HTTPException(status_code=404, detail="Book ID not found")
    
@app.get("/book/genre:{genre}")
def get_books_by_genre(genre: str):
    matching_books = [book for book in books if book['genre'] == genre]
    if not matching_books:
        raise HTTPException(status_code=404, detail="Genre not found")
    return matching_books