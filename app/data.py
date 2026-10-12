"""Portfolio content configuration for Shreyansh Sahu.

Centralized dataset with personal details, projects (DocuMind & Expenses Tracker), skills, and education.
"""

PORTFOLIO_DATA = {
    "profile": {
        "name": "Shreyansh Sahu",
        "initials": "SS",
        "title": "Full-Stack Web Developer & AI Engineer",
        "subtitle": "MCA Student • Specialized in Next.js, PostgreSQL & AI Solutions",
        "badge": "Available for Full-Stack & AI Roles",
        "tagline": "Building intelligent, scalable web applications, financial dashboards, and modern architectures.",
        "bio": (
            "Motivated Full-Stack Web Developer and MCA student with hands-on experience building scalable web applications "
            "and AI-powered solutions using Next.js, React, Node.js, PostgreSQL (pgvector), and modern AI architectures. "
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
        "quick_highlights": [
            {
                "tag": "Featured Live App",
                "title": "DocuMind",
                "short_desc": "AI Document Intelligence & RAG platform with multi-format ingestion and citations.",
                "link": "https://docu-mind-dun.vercel.app",
                "link_text": "Launch Live Demo",
                "is_external": True,
                "badge_color": "amber"
            },
            {
                "tag": "Full-Stack Project",
                "title": "Expenses Tracker",
                "short_desc": "Personal budget management with Next.js 14, Drizzle ORM, Clerk, and Recharts.",
                "link": "https://github.com/shadow190202/Expenses-Tracker",
                "link_text": "View on GitHub",
                "is_external": True,
                "badge_color": "silver"
            },
            {
                "tag": "Academic Qualifications",
                "title": "MCA • LNCT Bhopal (7.70 CGPA)",
                "short_desc": "B.Sc Computer Science (7.50 CGPA) • Rajeev Gandhi College • Python Certified.",
                "link": "#experience",
                "link_text": "View Education Details",
                "is_external": False,
                "badge_color": "amber"
            }
        ]
    },
    "projects": [
        {
            "id": "documind",
            "title": "DocuMind — AI Document Intelligence & Knowledge Assistant",
            "category": "AI / Full-Stack Enterprise Platform",
            "featured": True,
            "badge": "Featured AI System",
            "summary": (
                "An end-to-end AI document intelligence platform built with Next.js 14 App Router, React, and Node.js. "
                "Enables multi-format document ingestion (PDF, DOCX, TXT, CSV) with binary magic-byte validation, "
                "vector search indexing in PostgreSQL via pgvector, and grounded conversational "
                "assistance with verifiable page-level citations."
            ),
            "preview_image": "/assets/images/documind-preview.svg",
            "live_url": "https://docu-mind-dun.vercel.app",
            "github_url": "https://github.com/shadow190202/DocuMind",
            "highlights": [
                "Architected a full-stack document intelligence platform using Next.js 14 App Router, React, and Node.js, enabling multi-format document ingestion (PDF, DOCX, TXT, CSV) with binary magic-byte validation and physical page attribution.",
                "Implemented an end-to-end vector search pipeline and indexed chunks in PostgreSQL using pgvector cosine distance search (<=>) with Drizzle ORM.",
                "Engineered a grounded conversational RAG assistant featuring token-budgeted context assembly, verifiable page-level source citations, and hallucination-resistant fallback responses.",
                "Built automated document summarization (executive summaries, bullet points, key takeaways) with database caching to eliminate redundant AI calls, alongside structured side-by-side document comparison analytics.",
                "Secured application with Clerk authentication, PostgreSQL server-side role-based access control (RBAC), multi-user document permissions (read, write, admin), IDOR protection, admin telemetry dashboard, and 570+ automated tests."
            ],
            "tags": [
                "Next.js 14 (App Router)",
                "React",
                "Node.js",
                "PostgreSQL",
                "pgvector",
                "Drizzle ORM",
                "Docker",
                "Clerk Auth",
                "Tailwind CSS",
                "Vercel"
            ],
            "architecture_specs": [
                {"label": "Architecture Type", "value": "Full-Stack Retrieval-Augmented Generation (RAG)"},
                {"label": "Vector Database", "value": "PostgreSQL with pgvector cosine distance indexing"},
                {"label": "ORM & Migrations", "value": "Drizzle ORM"},
                {"label": "Ingestion Formats", "value": "PDF, DOCX, TXT, CSV with Magic-Byte validation"},
                {"label": "Security Model", "value": "Clerk Auth + Server-side RBAC & IDOR Guard"},
                {"label": "Testing & Reliability", "value": "570+ Unit & E2E Automated Tests Passed"}
            ]
        },
        {
            "id": "expenses-tracker",
            "title": "Expenses Tracker — Personal Budgeting & Financial Analytics",
            "category": "Full-Stack Web Application / Financial Tech",
            "featured": True,
            "badge": "Full-Stack Dashboard",
            "summary": (
                "A modern, full-stack personal budgeting & expense management platform built with Next.js 14 App Router, "
                "PostgreSQL, Drizzle ORM, Clerk Auth, and Recharts. Empowers users to set category budgets, record expenses in real-time, "
                "and visualize spending trends through interactive analytics."
            ),
            "preview_image": "/assets/images/expenses-tracker-preview.svg",
            "live_url": "https://github.com/shadow190202/Expenses-Tracker",
            "github_url": "https://github.com/shadow190202/Expenses-Tracker",
            "highlights": [
                "Built an end-to-end personal finance management platform using Next.js 14 App Router, React, and Tailwind CSS with a clean, responsive dashboard layout.",
                "Designed relational database models in PostgreSQL with Drizzle ORM, orchestrating automatic schema migrations with drizzle-kit.",
                "Implemented secure user authentication and multi-tenant session isolation using Clerk Auth to ensure individual budget and transaction privacy.",
                "Integrated Recharts interactive visual analytics, generating dynamic bar charts comparing Budget Allocated vs. Total Actual Spend.",
                "Engineered complete CRUD workflows for budget caps and dynamic expense tracking with real-time UI state updates and deletion refreshes."
            ],
            "tags": [
                "Next.js 14 (App Router)",
                "React",
                "PostgreSQL",
                "Drizzle ORM",
                "drizzle-kit",
                "Clerk Auth",
                "Tailwind CSS",
                "Recharts",
                "Vercel"
            ],
            "architecture_specs": [
                {"label": "Frontend Framework", "value": "Next.js 14 App Router (React)"},
                {"label": "Authentication", "value": "Clerk Multi-Tenant User Sessions"},
                {"label": "Database", "value": "PostgreSQL (Neon / Cloud SQL)"},
                {"label": "Data Access Layer", "value": "Drizzle ORM + Schema Migrations"},
                {"label": "Analytics Visuals", "value": "Recharts Dynamic Spending Charts"},
                {"label": "Component Library", "value": "Modular Tailwind CSS Architecture"}
            ]
        }
    ],
    "skills": [
        {
            "group": "AI & Machine Learning",
            "icon": "brain",
            "skills": [
                "Retrieval-Augmented Generation (RAG)",
                "Semantic & Cosine Search (<=>)",
                "Document Summarization & Analytics",
                "Full-Stack AI Architecture"
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
