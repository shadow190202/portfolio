"""Portfolio content configuration for Shreyansh Sahu.

Centralized dataset with personal details, flagship DocuMind project, skills, and experience.
"""

PORTFOLIO_DATA = {
    "profile": {
        "name": "Shreyansh Sahu",
        "initials": "SS",
        "title": "Full-Stack Web Developer & AI Engineer",
        "subtitle": "MCA Student • Specialized in Next.js, PostgreSQL (pgvector) & Google Gemini AI",
        "badge": "Available for Full-Stack & AI Engineering Roles",
        "tagline": "Building intelligent, scalable web applications and production-ready RAG workflows.",
        "bio": (
            "Motivated Full-Stack Web Developer and MCA student with hands-on experience building scalable web applications "
            "and AI-powered solutions using Next.js, React, Node.js, PostgreSQL (pgvector), and Google Gemini AI. "
            "Skilled in component architecture, RAG workflows, vector similarity search, and clean coding principles. "
            "Passionate about building intelligent, production-ready applications."
        ),
        "location": "Indore, Madhya Pradesh, India",
        "phone": "+91-9752387516",
        "email": "shreyanshsahu1319@gmail.com",
        "hero_image": "/assets/images/my-image-hero-section.png",
        "hero_background": "/assets/images/hero-background-img.jpg",
        "social": {
            "github": "https://github.com/shadow190202",
            "linkedin": "https://linkedin.com/in/shreyansh-sahu-9503a0325",
            "email": "mailto:shreyanshsahu1319@gmail.com",
            "phone": "tel:+919752387516"
        },
        "stats": [
            {"value": "570+", "label": "Automated Tests Passed"},
            {"value": "768-dim", "label": "Gemini Vector Search"},
            {"value": "142ms", "label": "P99 RAG Query Latency"},
            {"value": "7.70", "label": "MCA Academic CGPA"}
        ]
    },
    "projects": [
        {
            "id": "documind",
            "title": "DocuMind — AI Document Intelligence & Knowledge Assistant",
            "category": "AI / Full-Stack Enterprise Platform",
            "featured": True,
            "badge": "Flagship Production System",
            "summary": (
                "An end-to-end AI document intelligence platform built with Next.js 14 App Router, React, and Node.js. "
                "Enables multi-format document ingestion (PDF, DOCX, TXT, CSV) with binary magic-byte validation, "
                "768-dimensional Google Gemini vector search indexing in PostgreSQL via pgvector, and grounded conversational "
                "assistance with verifiable page-level citations."
            ),
            "preview_image": "/assets/images/documind-preview.svg",
            "live_url": "https://docu-mind-dun.vercel.app",
            "github_url": "https://github.com/shadow190202/DocuMind",
            "highlights": [
                "Architected a full-stack document intelligence platform using Next.js 14 App Router, React, and Node.js, enabling multi-format document ingestion (PDF, DOCX, TXT, CSV) with binary magic-byte validation and physical page attribution.",
                "Implemented an end-to-end vector search pipeline generating 768-dimensional embeddings via Google Gemini (gemini-embedding-001) and indexing chunks in PostgreSQL using pgvector cosine distance search (<=>) with Drizzle ORM.",
                "Engineered a grounded conversational RAG assistant using Google Gemini 2.5 Flash, featuring token-budgeted context assembly, verifiable page-level source citations, and hallucination-resistant fallback responses.",
                "Built automated document summarization (executive summaries, bullet points, key takeaways) with database caching to eliminate redundant AI calls, alongside structured side-by-side document comparison analytics.",
                "Secured application with Clerk authentication, PostgreSQL server-side role-based access control (RBAC), multi-user document permissions (read, write, admin), IDOR protection, admin telemetry dashboard, and 570+ automated tests."
            ],
            "tags": [
                "Next.js 14 (App Router)",
                "React",
                "Node.js",
                "PostgreSQL",
                "pgvector",
                "Google Gemini 2.5 Flash",
                "gemini-embedding-001",
                "Drizzle ORM",
                "Docker",
                "Clerk Auth",
                "Tailwind CSS",
                "Vercel"
            ],
            "architecture_specs": [
                {"label": "Embedding Model", "value": "Google Gemini (gemini-embedding-001, 768-dim)"},
                {"label": "Inference Engine", "value": "Google Gemini 2.5 Flash"},
                {"label": "Vector Database", "value": "PostgreSQL with pgvector extension"},
                {"label": "ORM & Migrations", "value": "Drizzle ORM"},
                {"label": "Ingestion Formats", "value": "PDF, DOCX, TXT, CSV with Magic-Byte validation"},
                {"label": "Security Model", "value": "Clerk Auth + Server-side RBAC & IDOR Guard"},
                {"label": "Test Coverage", "value": "570+ Unit & E2E Automated Tests Passed"}
            ]
        }
    ],
    "skills": [
        {
            "group": "AI & Generative AI",
            "icon": "brain",
            "skills": [
                "Retrieval-Augmented Generation (RAG)",
                "Vector Embeddings (768-dim)",
                "Google Gemini API (2.5 Flash)",
                "Semantic & Cosine Search (<=>)",
                "Document Summarization & Analytics"
            ]
        },
        {
            "group": "Backend & Databases",
            "icon": "server",
            "skills": [
                "Node.js",
                "PostgreSQL & pgvector",
                "Drizzle ORM",
                "Python",
                "RESTful APIs Architecture",
                "Server-Side RBAC & Security"
            ]
        },
        {
            "group": "Frontend Engineering",
            "icon": "layout",
            "skills": [
                "Next.js (App Router)",
                "React.js",
                "Tailwind CSS",
                "JavaScript (ES6+)",
                "HTML5 & CSS3",
                "Responsive Web Design"
            ]
        },
        {
            "group": "Tools, DevOps & Core CS",
            "icon": "cloud",
            "skills": [
                "Docker",
                "Git & GitHub",
                "Clerk Auth",
                "Vercel Deployment",
                "Postman & VS Code",
                "OOP, DBMS & OS Fundamentals",
                "Computer Networks & Web Security"
            ]
        }
    ],
    "experience": [
        {
            "role": "Python Intern",
            "company": "Ypsilon IT Solutions Pvt. Ltd.",
            "location": "Bhopal, India",
            "duration": "May 2025",
            "type": "Internship",
            "bullets": [
                "Completed hands-on Python development training focused on scripting, debugging, and logical problem-solving using clean coding practices.",
                "Developed Python programs to strengthen programming fundamentals while applying modular design and debugging techniques.",
                "Collaborated with mentors during practical development exercises, enhancing analytical thinking and software development skills."
            ],
            "tags": ["Python", "Scripting", "Debugging", "Modular Design", "Problem Solving"]
        }
    ],
    "education": [
        {
            "degree": "Master of Computer Applications (MCA)",
            "institution": "Lakshmi Narain College of Technology, Bhopal",
            "duration": "2024 — Present",
            "score": "CGPA: 7.70",
            "highlights": "Focused on Advanced Web Engineering, Distributed Systems, Database Management, and Artificial Intelligence."
        },
        {
            "degree": "Bachelor of Science (Computer Science)",
            "institution": "Rajeev Gandhi College, Bhopal",
            "duration": "2021 — 2024",
            "score": "CGPA: 7.50",
            "highlights": "Strong grounding in Computer Science fundamentals, Object-Oriented Programming, Data Structures, and Software Development."
        }
    ],
    "certifications": [
        {
            "title": "Python Internship Certification",
            "issuer": "Ypsilon IT Solutions Pvt. Ltd.",
            "description": "Certified completion of hands-on Python programming, debugging, and software development methodologies."
        }
    ]
}
