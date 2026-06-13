{
    "book1": {
        "tittle": "Lord of the rings",
        "Author": "Greta",
        "Year": "2024",
        "genre": "Science Fiction"
    },
    "book2": {
        "tittle": "Princess Diana",
        "Author": "Erina",
        "Year": "2025",
        "genre": "Science "
    },
    "book3": {
        "tittle": "God",
        "Author": "Erina",
        "Year": "2022",
        "genre": "Science"
    },
}







from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def home():
    return {
    "book1": {
        "tittle": "Lord of the rings",
        "Author": "Greta",
        "Year": "2024",
        "genre": "Science Fiction"
    },
    "book2": {
        "tittle": "Princess Diana",
        "Author": "Erina",
        "Year": "2025",
        "genre": "Science "
    },
    "book3": {
        "tittle": "God",
        "Author": "Erina",
        "Year": "2022",
        "genre": "Science"
    },
}


