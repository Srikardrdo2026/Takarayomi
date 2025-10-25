from fastapi import FastAPI
from routes import manga_routes, chapter_routes, page_routes, favorite_routes, download_routes

app = FastAPI(
    title="Takarayomi Backend API",
    version="1.0",
    description="Backend API for Takarayomi, providing endpoints for manga, chapters, pages, downloads, and favorites."
)

@app.get("/")
def read_root():
    return {"message": "📚 Welcome to the Takarayomi Backend API!"}


app.include_router(manga_routes.router, prefix="/api")
app.include_router(chapter_routes.router, prefix="/api")
app.include_router(page_routes.router, prefix="/api")
app.include_router(favorite_routes.router, prefix="/api")
app.include_router(download_routes.router, prefix="/api")
