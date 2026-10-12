# Developer Portfolio Website

A modern, high-performance portfolio website built with **Python (FastAPI)**, **Tailwind CSS**, and interactive client-side JavaScript. Designed with a dark slate texture aesthetic derived from `assets/images/hero-background-img.jpg`.

---

## 🎨 Theme & Visual Design

- **Backdrop**: Deep slate and matte charcoal textured finish from `hero-background-img.jpg` with layered radial lighting gradients.
- **Hero Section**: Features the cutout developer portrait (`assets/images/my-image-hero-section.png`) with ambient backlighting, glowing status pills, and key metrics.
- **Featured Projects**: Flags **DocuMind** with its interactive SVG dashboard preview (`assets/images/documind-preview.svg`), architecture specifications, and live link.
- **Glassmorphic Cards**: Multi-depth border illumination, backdrop blur filters, and responsive hover transitions.
- **Color Accents**: Electric Cyan (`#38bdf8`), Deep Indigo (`#6366f1`), and Emerald (`#10b981`).

---

## 📂 Project Architecture

```
e:\portfolio\
├── .venv/                      # Python virtual environment (Python 3.14)
├── assets/                     # Media & asset directory
│   └── images/
│       ├── documind-preview.svg        # DocuMind RAG preview illustration
│       ├── hero-background-img.jpg     # Textured dark slate background theme
│       ├── my-image-hero-section.png   # Cutout developer portrait
│       └── my-image-hero-section.svg   # Vector portrait variant
├── app/
│   ├── __init__.py
│   ├── config.py              # Environment configuration & directory paths
│   ├── data.py                # Structured dataset (Profile, Projects, Skills, Timeline)
│   └── main.py                # FastAPI application & API endpoints
├── static/
│   ├── css/
│   │   └── style.css          # Slate theme custom stylesheet & animations
│   └── js/
│       └── main.js            # Smooth scroll, active scrollspy & AJAX contact form
├── templates/
│   ├── base.html              # Base layout with meta & Tailwind CSS
│   ├── index.html             # Master index view (compact highlights)
│   ├── projects_page.html     # Dedicated in-depth projects & architecture page
│   └── components/
│       ├── nav.html           # Glassmorphism header & multi-page navigation
│       ├── hero.html          # Hero section with portrait & statistics
│       ├── projects.html      # Compact projects showcase cards with detail links
│       ├── skills.html        # Tech stack grid across 4 domains
│       ├── experience.html    # Career & academic milestones timeline
│       ├── contact.html       # Contact info & interactive AJAX form
│       └── footer.html        # Footer with navigation & status indicator
├── tests/
│   └── test_portfolio.py      # Automated endpoint and rendering test suite (8 tests)
├── requirements.txt           # Python package dependencies
├── run.py                     # Convenience runner script (python run.py)
└── README.md
```

---

## 🚀 Quickstart Guide

### 1. Activate the Virtual Environment

**Windows PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**
```cmd
.venv\Scripts\activate.bat
```

### 2. Run the Development Server

Execute the runner script:
```powershell
python run.py
```
Or directly with Uvicorn:
```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Open your browser and navigate to:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🧪 Running the Tests

Verify all routes, template rendering, and asset mounts:
```powershell
.\.venv\Scripts\python.exe -m unittest tests/test_portfolio.py
```

---

## 🛠️ Customizing Your Content

All portfolio text, links, projects, and skills are decoupled from the HTML and managed in:
👉 [`app/data.py`](file:///e:/portfolio/app/data.py)

- **`PORTFOLIO_DATA["profile"]`**: Update your name, headline, bio, and social links.
- **`PORTFOLIO_DATA["projects"]`**: Add or modify projects, live URLs, repository links, and tech tags.
- **`PORTFOLIO_DATA["skills"]`**: Adjust proficiencies and categories.
- **`PORTFOLIO_DATA["timeline"]`**: Update career and education milestones.
