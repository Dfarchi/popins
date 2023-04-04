from django.db import models
from django.contrib.auth.models import User

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    address = models.CharField(max_length=256, db_column='address', null=False, blank=False)
    kids = models.CharField(max_length=256, db_column='kids', null=False, blank=False)
    bio = models.CharField(max_length=256, db_column='bio', null=False, blank=False)
    reviews = models.ForeignKey('Review', on_delete=models.RESTRICT, related_name='parent_reviews')
    sessions = models.ForeignKey('Session', on_delete=models.RESTRICT, related_name='parent_sessions')
    # relations = models.ForeignKey('Relations', on_delete=models.RESTRICT, related_name='parent_relations')
    # phone_number = PhoneNumberField
    birth_year = models.IntegerField(db_column='birth_year', null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'parents'


class Nanny(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    address = models.CharField(max_length=256, db_column='address', null=False, blank=False)
    bio = models.CharField(max_length=256, db_column='bio', null=False, blank=False)
    links = models.URLField(max_length=200, blank=True)
    profile_pic = models.ImageField(upload_to='images/')
    reviews = models.ForeignKey('Review', on_delete=models.RESTRICT, related_name='nanny_reviews')
    sessions = models.ForeignKey('Session', on_delete=models.RESTRICT, related_name='nanny_sessions')
    # relations = models.ForeignKey('Relations', on_delete=models.RESTRICT, related_name='nanny_relations')
    # in_app_exp = ???
    # phone_number = PhoneNumberField
    birth_year = models.IntegerField(db_column='birth_year', null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "nanny's"


class Interests(models.Model):
    nanny = models.ForeignKey('Nanny', on_delete=models.RESTRICT)
    session = models.ForeignKey('Session', on_delete=models.RESTRICT)
    note = models.CharField(max_length=256, db_column='note', null=False, blank=False)

    class Meta:
        db_table = "interests"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    review = models.TextField(db_column='review', null=False)
    review_date = models.DateField(db_column='date', null=False, default='1900-01-01')

    class Meta:
        db_table = "reviews"


class Session(models.Model):
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    date = models.DateField(db_column='date', null=False, default='1900-01-01')
    salary = models.IntegerField(null=True, blank=0)
    note = models.CharField(max_length=256, db_column='note', null=False, blank=False)
    has_happened = models.BooleanField(null=True, blank=False)

    # roll = models.TextField(db_column='roll')

    def __str__(self):
        return f"{self.parent.name} on {self.date}"

    class Meta:
        db_table = 'sessions'
