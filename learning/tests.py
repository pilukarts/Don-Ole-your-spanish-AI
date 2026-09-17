from django.test import TestCase
from django.urls import reverse


class LearningViewsTests(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse("learning:home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Aprende español")

    def test_invalid_profile_falls_back_safely(self):
        response = self.client.get(reverse("learning:lesson"), {"level": "Z9", "audience": "robot"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nivel A1")

    def test_quiz_score(self):
        response = self.client.post(
            reverse("learning:lesson") + "?level=A1&audience=adultos",
            {"question_0": "0", "question_1": "1", "question_2": "1"},
        )
        self.assertContains(response, "3 de 3")

