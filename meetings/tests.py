from django.test import TestCase
from meetings.models import Meeting
from datetime import datetime


class MeetingTestCase(TestCase):
    def setUp(self):
        self.date = datetime.now()
        Meeting.objects.create(title="meeting 1", date=self.date)

    def test_meeting_date_is_set(self):
        """"Meeting date is set"""
        meeting = Meeting.objects.get(title="meeting 1")
        self.assertEqual(meeting.date, self.date.date())