from django.db import models


class Todo(models.Model):
    DONE = 'Done'
    ON_PROCESS = 'On Process'

    STATUS_TODO = [
        (DONE, 'Done'),
        (ON_PROCESS, 'On Process')
    ]

    title = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_TODO, default=ON_PROCESS, max_length=10)

    def __str__(self):
        return self.title
