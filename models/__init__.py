from database import Base
from .Manga import Manga
from .Chapter import Chapter
from .Favorite import Favorite
from .Page import Page
from .Download import Download

__all__ = ["Base", "Manga", "Chapter", "Favorite", "Page", "Download"]