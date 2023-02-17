from django.test import TestCase
from .models import Project

class ProjectTest(TestCase):
    def setUp(self):
        Project.objects.create(title="CharField", description="CharField")

    def test_project(self):
        self.assertEqual(Project.objects.count(), 1)
        obj = Project.objects.get(title="CharField")
        self.assertEqual(obj.title, "CharField")