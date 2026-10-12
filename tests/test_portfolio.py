"""Automated tests for FastAPI Developer Portfolio."""
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

    def test_home_page_renders(self):
        """Verify home page renders HTML with stylesheet, portrait, and project details."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("text/html", response.headers["content-type"])
        html = response.text
        self.assertIn("/static/css/style.css", html)
        self.assertIn("my-image-hero-section.png", html)
        self.assertIn("DocuMind", html)
        self.assertIn("570+ Verified Tests", html)

    def test_css_references_hero_background_theme(self):
        """Verify style.css embeds hero-background-img.jpg as theme background."""
        response = self.client.get("/static/css/style.css")
        self.assertEqual(response.status_code, 200)
        self.assertIn("hero-background-img.jpg", response.text)

    def test_projects_endpoint(self):
        """Verify /api/projects returns structured project data."""
        response = self.client.get("/api/projects")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertGreater(data["count"], 0)
        self.assertEqual(data["projects"][0]["id"], "documind")

    def test_contact_submission_success(self):
        """Verify contact form submission handles valid input."""
        payload = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "subject": "AI Project Collaboration",
            "message": "We would love to discuss a project with you."
        }
        response = self.client.post("/api/contact", data=payload)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data["success"])
        self.assertIn("Thank you, Jane Doe", data["message"])

    def test_contact_submission_invalid_email(self):
        """Verify contact form rejects invalid email addresses."""
        payload = {
            "name": "Jane Doe",
            "email": "not-an-email",
            "subject": "Hello",
            "message": "Testing invalid email"
        }
        response = self.client.post("/api/contact", data=payload)
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data["success"])

    def test_asset_serving(self):
        """Verify static asset endpoints correctly serve the hero background and images."""
        bg_response = self.client.get("/assets/images/hero-background-img.jpg")
        self.assertEqual(bg_response.status_code, 200)
        self.assertEqual(bg_response.headers["content-type"], "image/jpeg")

        avatar_response = self.client.get("/assets/images/my-image-hero-section.png")
        self.assertEqual(avatar_response.status_code, 200)
        self.assertEqual(avatar_response.headers["content-type"], "image/png")

        documind_response = self.client.get("/assets/images/documind-preview.svg")
        self.assertEqual(documind_response.status_code, 200)
        self.assertIn("image/svg", documind_response.headers["content-type"])


if __name__ == "__main__":
    unittest.main()
