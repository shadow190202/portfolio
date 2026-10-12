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

    def test_home_page_renders_shreyansh_details(self):
        """Verify home page renders HTML with Shreyansh Sahu's exact details and projects."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])
        html = response.text
        self.assertIn("Shreyansh Sahu", html)
        self.assertIn("shreyanshsahu1319@gmail.com", html)
        self.assertIn("+91-9752387516", html)
        self.assertIn("Indore, Madhya Pradesh", html)
        self.assertIn("DocuMind", html)
        self.assertIn("Expenses Tracker", html)
        self.assertIn("Ypsilon IT Solutions", html)
        self.assertIn("Lakshmi Narain College of Technology", html)
        self.assertIn("7.70", html)
        self.assertIn("570+ Automated Tests Passed", html)

    def test_css_references_hero_background_theme(self):
        """Verify style.css embeds hero-background-img.jpg as theme background."""
        response = self.client.get("/static/css/style.css")
        self.assertEqual(response.status_code, 200)
        self.assertIn("hero-background-img.jpg", response.text)

    def test_projects_endpoint_both_repositories(self):
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
            "name": "Hiring Manager",
            "email": "hiring@innovatech.com",
            "subject": "Full-Stack Web Developer Opportunity",
            "message": "We reviewed your DocuMind and Expenses Tracker projects and would like to invite you for an interview."
        }
        response = self.client.post("/api/contact", data=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertIn("Thank you, Hiring Manager", data["message"])

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


if __name__ == "__main__":
    unittest.main()
