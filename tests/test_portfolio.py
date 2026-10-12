"""Automated tests for Shreyansh Sahu Developer Portfolio."""
import sys
from pathlib import Path
import unittest

# Ensure project root is in sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from fastapi.testclient import TestClient
from app.main import app


class TestPortfolioApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_health_endpoint(self):
        """Verify the health check endpoint returns 200 and healthy status."""
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["status"], "healthy")
        self.assertIn("timestamp", data)

    def test_home_page_renders_compact_projects_and_links(self):
        """Verify home page renders HTML with compact project cards and link to /projects."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])
        html = response.text
        self.assertIn("Shreyansh Sahu", html)
        self.assertIn("DocuMind", html)
        self.assertIn("Expenses Tracker", html)
        self.assertIn("/projects", html)
        self.assertIn("View All in Full Detail", html)

    def test_detailed_projects_page_renders(self):
        """Verify /projects and /project routes render full case studies and architectures."""
        for route in ("/projects", "/project"):
            response = self.client.get(route)
            self.assertEqual(response.status_code, 200)
            self.assertIn("text/html", response.headers["content-type"])
            html = response.text
            self.assertIn("Engineering Projects", html)
            self.assertIn("Deep Dive", html)
            self.assertIn("DocuMind", html)
            self.assertIn("Expenses Tracker", html)
            self.assertIn("Comprehensive Implementation Highlights", html)
            self.assertIn("System Specifications &amp; Architectural Matrix", html)
            self.assertIn("documind-preview.svg", html)
            self.assertIn("expenses-tracker-preview.svg", html)

    def test_css_references_hero_background_theme(self):
        """Verify style.css embeds hero-background-img.jpg as theme background."""
        response = self.client.get("/static/css/style.css")
        self.assertEqual(response.status_code, 200)
        self.assertIn("hero-background-img.jpg", response.text)

    def test_projects_api_endpoint(self):
        """Verify /api/projects returns both DocuMind and Expenses Tracker projects."""
        response = self.client.get("/api/projects")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertEqual(data["count"], 2)

        # DocuMind checks
        self.assertEqual(data["projects"][0]["id"], "documind")
        self.assertEqual(data["projects"][0]["github_url"], "https://github.com/shadow190202/DocuMind")
        self.assertEqual(data["projects"][0]["live_url"], "https://docu-mind-dun.vercel.app")

        # Expenses-Tracker checks
        self.assertEqual(data["projects"][1]["id"], "expenses-tracker")
        self.assertEqual(data["projects"][1]["github_url"], "https://github.com/shadow190202/Expenses-Tracker")
        self.assertIn("Next.js 14 (App Router)", data["projects"][1]["tags"])
        self.assertIn("Recharts", data["projects"][1]["tags"])

    def test_contact_submission_success(self):
        """Verify contact form submission handles valid input."""
        payload = {
            "name": "Engineering Lead",
            "email": "lead@company.com",
            "subject": "Full-Stack Web Developer Opportunity",
            "message": "We reviewed your DocuMind and Expenses Tracker detailed case studies."
        }
        response = self.client.post("/api/contact", data=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertIn("Thank you, Engineering Lead", data["message"])

    def test_contact_submission_invalid_email(self):
        """Verify contact form rejects invalid email addresses."""
        payload = {
            "name": "Test User",
            "email": "invalid-email-address",
            "subject": "Inquiry",
            "message": "Testing validation"
        }
        response = self.client.post("/api/contact", data=payload)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data["success"])

    def test_asset_serving(self):
        """Verify static asset endpoints correctly serve images and SVG mockups."""
        bg_response = self.client.get("/assets/images/hero-background-img.jpg")
        self.assertEqual(bg_response.status_code, 200)
        self.assertEqual(bg_response.headers["content-type"], "image/jpeg")

        avatar_response = self.client.get("/assets/images/my-image-hero-section.png")
        self.assertEqual(avatar_response.status_code, 200)
        self.assertEqual(avatar_response.headers["content-type"], "image/png")

        documind_response = self.client.get("/assets/images/documind-preview.svg")
        self.assertEqual(documind_response.status_code, 200)
        self.assertIn("image/svg", documind_response.headers["content-type"])

        expenses_response = self.client.get("/assets/images/expenses-tracker-preview.svg")
        self.assertEqual(expenses_response.status_code, 200)
        self.assertIn("image/svg", expenses_response.headers["content-type"])

    def test_user_theme_and_content_customizations(self):
        """Verify the user's custom requirements:
        1. 'Powered by' badge replaced with Shreyansh Sahu.
        2. 'Quality Assurance' badge removed.
        3. 3 hero boxes contain DocuMind, Expenses Tracker, and Education details in short.
        4. Vector Embeddings (768-dim) and Google Gemini API (2.5 Flash) removed from skills.
        5. Titanium platinum theme and reveal-on-scroll animations applied.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        html = response.text

        # 1. Badge replaced to Shreyansh Sahu
        self.assertIn("Full-Stack Engineer", html)
        self.assertIn("Shreyansh Sahu", html)

        # 2. Quality Assurance removed
        self.assertNotIn("Quality Assurance", html)

        # 3. 3 hero boxes
        self.assertIn("Featured Live App", html)
        self.assertIn("DocuMind", html)
        self.assertIn("Expenses Tracker", html)
        self.assertIn("Academic Qualifications", html)
        self.assertIn("MCA • LNCT Bhopal", html)

        # 4. Removed skills
        self.assertNotIn("Vector Embeddings (768-dim)", html)
        self.assertNotIn("Google Gemini API (2.5 Flash)", html)

        # 5. Scroll reveal and Titanium theme classes
        self.assertIn("reveal-on-scroll", html)
        self.assertIn("gradient-text-titanium", html)


if __name__ == "__main__":
    unittest.main()
