"""Developer server runner script for Portfolio website."""
import sys
import uvicorn
from app.config import settings

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

if __name__ == "__main__":
    print(f"Starting Portfolio Server on http://{settings.HOST}:{settings.PORT}")
    print("Theme based on hero-background-img.jpg (Dark Slate Texture)")
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
    )
