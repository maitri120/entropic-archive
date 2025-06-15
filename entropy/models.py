from django.db import models
from django.utils import timezone #for time-stamps
import random #for randomsing characters

class Submission(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def time_since_submission(self):
        return (timezone.now() - self.created_at).total_seconds()

    def fragments(self):
        chars = list(self.content)
        elapsed_time = self.time_since_submission()
        for _ in range(int(elapsed_time//2)):
            if chars:
                i = random.randint(0, len(chars)-1)
                chars[i] = random.choice(['@', '#', '$', '%', '^', '&', '*'])
        return ''.join(chars)
