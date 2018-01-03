from django.db import models


class FizzBuzz(models.Model):
    """
    FizzBuzz Model 
    """

    fizzbuzz_id = models.AutoField(primary_key=True)
    useragent = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now=True)
    message = models.TextField()

    def __str__(self):
        return "This FizzBuzz says: {}".format(self.message)
