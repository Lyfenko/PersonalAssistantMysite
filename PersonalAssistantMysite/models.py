from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    birthday = models.DateField()

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def days_until_birthday(self):
        from datetime import date
        today = date.today()
        next_birthday = date(today.year, self.birthday.month, self.birthday.day)
        if today > next_birthday:
            next_birthday = date(today.year + 1, self.birthday.month, self.birthday.day)
        days_left = (next_birthday - today).days
        return days_left


class Note(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"Note #{self.id}"
