"""Developer server runner script for Portfolio website."""
import uvicorn
from app.config import settings

if __name__ == "__main__":
    print(f"🚀 Starting Portfolio Server on http://{settings.HOST}:{settings.PORT}")
    print(f"🎨 Theme based on hero-background-img.jpg (Dark Slate Texture)")
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
