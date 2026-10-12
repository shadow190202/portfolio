"""FastAPI application entrypoint for the Developer Portfolio."""
from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr

from app.config import settings
from app.data import PORTFOLIO_DATA

app = FastAPI(
    title=settings.APP_NAME,
    description="Production-ready developer portfolio powered by FastAPI and modern UI.",
    version="1.0.0",
)

# Ensure static directories exist (safely handled for serverless read-only runtimes)
try:
    settings.STATIC_DIR.mkdir(parents=True, exist_ok=True)
    (settings.STATIC_DIR / "css").mkdir(parents=True, exist_ok=True)
    (settings.STATIC_DIR / "js").mkdir(parents=True, exist_ok=True)
    settings.TEMPLATES_DIR.mkdir(parents=True, exist_ok=True)
except Exception:
    pass

# Mount static and assets files
if settings.ASSETS_DIR.exists():
    app.mount("/assets", StaticFiles(directory=str(settings.ASSETS_DIR)), name="assets")

if settings.STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(settings.STATIC_DIR)), name="static")

templates = Jinja2Templates(directory=str(settings.TEMPLATES_DIR))


class ContactMessage(BaseModel):
    name: str
    email: EmailStr
    subject: Optional[str] = "Portfolio Inquiry"
    message: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the main portfolio landing page with dark slate theme."""
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "data": PORTFOLIO_DATA,
            "year": datetime.now(timezone.utc).year,
            "is_home": True,
        },
    )


@app.get("/projects", response_class=HTMLResponse)
@app.get("/project", response_class=HTMLResponse)
async def projects_detail_page(request: Request):
    """Render the detailed projects page displaying full architectures and telemetry."""
    return templates.TemplateResponse(
        request=request,
        name="projects_page.html",
        context={
            "data": PORTFOLIO_DATA,
            "year": datetime.now(timezone.utc).year,
            "is_home": False,
        },
    )


@app.get("/api/health")
async def health_check():
    """Service health verification endpoint."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "app": settings.APP_NAME,
    }


@app.get("/api/projects")
async def get_projects():
    """Retrieve structured portfolio projects."""
    return {
        "success": True,
        "count": len(PORTFOLIO_DATA["projects"]),
        "projects": PORTFOLIO_DATA["projects"],
    }


@app.post("/api/contact")
async def submit_contact(
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form("General Inquiry"),
    message: str = Form(...),
):
    """Handle contact form submissions with validation and feedback."""
    name_clean = name.strip()
    email_clean = email.strip()
    msg_clean = message.strip()

    if not name_clean or not email_clean or not msg_clean:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "error": "All required fields (name, email, message) must be completed.",
            },
        )

    if "@" not in email_clean or "." not in email_clean:
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "error": "Please provide a valid email address.",
            },
        )

    # In a production environment, send email or forward to webhook/database
    return {
        "success": True,
        "message": f"Thank you, {name_clean}! Your message has been received. I'll get back to you shortly at {email_clean}.",
        "received_at": datetime.now(timezone.utc).isoformat(),
    }
