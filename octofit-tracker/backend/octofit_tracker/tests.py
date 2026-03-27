from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create(name="Test User", email="test@example.com", team=self.team)

    def test_user_creation(self):
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.team, self.team)

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Alpha Team")
        self.assertEqual(team.name, "Alpha Team")

class ActivityModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Beta Team")
        self.user = User.objects.create(name="Beta User", email="beta@example.com", team=self.team)
        self.activity = Activity.objects.create(user=self.user, type="Run", duration=30)

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, "Run")
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.user, self.user)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups")
        self.assertEqual(workout.name, "Pushups")
        self.assertEqual(workout.description, "Do 20 pushups")

class LeaderboardModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Gamma Team")
        self.user = User.objects.create(name="Gamma User", email="gamma@example.com", team=self.team)
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.user, self.user)
        self.assertEqual(self.leaderboard.score, 100)
