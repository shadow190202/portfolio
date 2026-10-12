"""Portfolio content configuration and structured dataset.

Easily update your bio, projects, skills, and experience in this central module.
"""

PORTFOLIO_DATA = {
    "profile": {
        "name": "Sahus",
        "title": "Full-Stack AI & Software Engineer",
        "badge": "Available for High-Impact Roles & Consulting",
        "tagline": "Architecting resilient full-stack systems, modern RAG pipelines, and high-performance cloud applications.",
        "bio": (
            "I design and build production-grade web applications and AI-driven platforms with a focus on "
            "sub-millisecond latency, verified correctness, and intuitive user experiences. Specializing in "
            "modern Python/FastAPI backends, Next.js frontends, and enterprise-scale RAG architectures."
        ),
        "location": "India",
        "email": "contact@portfolio.dev",
        "hero_image": "/assets/images/my-image-hero-section.png",
        "hero_background": "/assets/images/hero-background-img.jpg",
        "social": {
            "github": "https://github.com",
            "linkedin": "https://linkedin.com",
            "twitter": "https://twitter.com",
            "email": "mailto:contact@portfolio.dev"
        },
        "stats": [
            {"value": "570+", "label": "Automated Tests Passed"},
            {"value": "142ms", "label": "P99 RAG Pipeline Latency"},
            {"value": "99.9%", "label": "Production Reliability"},
            {"value": "4+", "label": "Years Building Web & AI Systems"}
        ]
    },
    "projects": [
        {
            "id": "documind",
            "title": "DocuMind — Enterprise RAG Assistant",
            "category": "AI / Full-Stack",
            "featured": True,
            "badge": "Featured Project",
            "summary": (
                "A full-stack RAG assistant featuring semantic retrieval over multi-page PDF documents, "
                "pgvector 768-dim embeddings, server-side RBAC, and grounded Gemini 2.5 Flash synthesis "
                "with verifiable page citations."
            ),
            "preview_image": "/assets/images/documind-preview.svg",
            "live_url": "https://docu-mind-dun.vercel.app/assistant/rag-query",
            "github_url": "https://github.com",
            "highlights": [
                "Grounded context synthesis with hallucination-resistant fallback & page citations",
                "pgvector cosine similarity indexing with sub-150ms query turnaround",
                "Clerk authentication integrated with strict server-side RBAC and magic-byte binary validation",
                "Extensive test suite with over 570 verified end-to-end and unit tests"
            ],
            "tags": ["Next.js 14", "Gemini 2.5 Flash", "PostgreSQL", "pgvector", "Drizzle ORM", "Clerk Auth", "Tailwind CSS"]
        },
        {
            "id": "neural-flow",
            "title": "NeuralFlow — Real-Time Agentic Orchestrator",
            "category": "Cloud & AI",
            "featured": True,
            "badge": "High Performance",
            "summary": (
                "Event-driven workflow orchestration engine coordinating multi-agent LLM systems with "
                "dynamic tool dispatch, state persistence, and distributed Redis event queuing."
            ),
            "preview_image": None,
            "live_url": "#",
            "github_url": "https://github.com",
            "highlights": [
                "Dynamic streaming execution with WebSocket bi-directional updates",
                "Distributed task scheduling backed by Celery and Redis Streams",
                "Automated checkpointing and rollbacks for multi-turn LLM reasoning"
            ],
            "tags": ["Python", "FastAPI", "Redis", "Docker", "WebSockets", "Pydantic"]
        },
        {
            "id": "pulse-metrics",
            "title": "PulseMetrics — Cloud Telemetry Dashboard",
            "category": "Infrastructure",
            "featured": False,
            "badge": "DevOps / Infra",
            "summary": (
                "High-throughput observability pipeline collecting time-series system metrics and log streams, "
                "rendering interactive analytics with millisecond query speeds."
            ),
            "preview_image": None,
            "live_url": "#",
            "github_url": "https://github.com",
            "highlights": [
                "Ingestion rate exceeding 25,000 events/sec via async worker pool",
                "Dynamic anomaly detection alerting via webhooks and Slack integrations",
                "Modular glassmorphism UI with real-time SVG sparkline charts"
            ],
            "tags": ["FastAPI", "TimescaleDB", "Chart.js", "Docker", "Tailwind CSS"]
        }
    ],
    "skills": [
        {
            "group": "AI & Machine Learning",
            "icon": "brain",
            "skills": [
                {"name": "Gemini API & LLMs", "level": "Expert"},
                {"name": "RAG Architecture", "level": "Expert"},
                {"name": "pgvector & Vector Search", "level": "Advanced"},
                {"name": "Embeddings & Semantic Search", "level": "Expert"},
                {"name": "Context Engineering", "level": "Advanced"}
            ]
        },
        {
            "group": "Backend Engineering",
            "icon": "server",
            "skills": [
                {"name": "Python & FastAPI", "level": "Expert"},
                {"name": "PostgreSQL & Drizzle ORM", "level": "Advanced"},
                {"name": "Redis & Caching", "level": "Advanced"},
                {"name": "RESTful & WebSocket APIs", "level": "Expert"},
                {"name": "RBAC & Auth Architecture", "level": "Advanced"}
            ]
        },
        {
            "group": "Frontend & Design",
            "icon": "layout",
            "skills": [
                {"name": "Next.js & React", "level": "Advanced"},
                {"name": "Tailwind CSS & Glassmorphism", "level": "Expert"},
                {"name": "HTML5 & Modern CSS", "level": "Expert"},
                {"name": "JavaScript / TypeScript", "level": "Advanced"},
                {"name": "Responsive & A11y UI", "level": "Expert"}
            ]
        },
        {
            "group": "DevOps & Cloud",
            "icon": "cloud",
            "skills": [
                {"name": "Docker & Containerization", "level": "Advanced"},
                {"name": "Git & CI/CD Pipelines", "level": "Expert"},
                {"name": "Vercel & Cloud Deployments", "level": "Advanced"},
                {"name": "Automated Testing (570+ Suites)", "level": "Expert"},
                {"name": "Linux Environments", "level": "Advanced"}
            ]
        }
    ],
    "timeline": [
        {
            "year": "2024 — Present",
            "role": "Senior AI & Full-Stack Solutions Engineer",
            "company": "Independent Innovations & Enterprise Clients",
            "description": (
                "Leading architectural design for production generative AI systems, modernizing cloud applications, "
                "and implementing robust RAG infrastructure including DocuMind. Engineered end-to-end vector retrieval pipelines "
                "and strict validation test suites."
            ),
            "tags": ["FastAPI", "Next.js", "Gemini 2.5", "pgvector", "PostgreSQL"]
        },
        {
            "year": "2022 — 2024",
            "role": "Full-Stack Web Developer",
            "company": "Technology Studio",
            "description": (
                "Developed scalable client-facing web applications, responsive dashboards, and optimized API layers. "
                "Spearheaded database migrations, auth flow hardening, and microservice integration."
            ),
            "tags": ["Python", "JavaScript", "REST APIs", "Tailwind CSS", "Docker"]
        },
        {
            "year": "2020 — 2022",
            "role": "B.Tech in Computer Science & Engineering",
            "company": "University",
            "description": (
                "Deep grounding in Data Structures, Algorithms, Distributed Computing, Database Management Systems, "
                "and Computer Networks."
            ),
            "tags": ["Algorithms", "Distributed Systems", "DBMS", "Operating Systems"]
        }
    ]
}
