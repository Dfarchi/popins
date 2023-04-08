from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    User_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE)
    is_parent = models.BooleanField(db_column='is_parent', default=False)
    is_nanny = models.BooleanField(db_column='is_nanny', default=False)
    name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
    bio = models.TextField(max_length=256, db_column='bio', null=False, blank=False)
    birth_year = models.IntegerField(db_column='birth_year', null=False)
    address = models.CharField(max_length=256, db_column='address', null=False, blank=False)
    link = models.URLField(max_length=200, blank=True)
    profile_pic = models.ImageField(upload_to='images/')

    # relations = models.ForeignKey('Relations', on_delete=models.RESTRICT, related_name='parent_relations')
    # phone_number = PhoneNumberField
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'profiles'


class Session(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, default=None)
    date = models.DateField(db_column='date', null=False, auto_now_add=True)
    salary = models.IntegerField(db_column='salary', default=50)
    note = models.TextField(max_length=256, db_column='note', null=False, blank=False)
    has_happened = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f"{self.user.name} on {self.date}"

    class Meta:
        db_table = 'sessions'


class Interest(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.RESTRICT)
    session = models.ManyToManyField(Session,db_table='Session_Interest')
    note = models.TextField(max_length=256, db_column='note', null=False, blank=False)
    talked = models.BooleanField(null=False, blank=False)
    status = models.BooleanField(null=False, blank=False)

    class Meta:
        db_table = "interest"


class Review(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.RESTRICT)
    review = models.TextField(db_column='review', null=False)
    review_date = models.DateField(db_column='date', null=False, auto_now_add=True)

    class Meta:
        db_table = "reviews"


"MERGEd TABLES"
# class Parent(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
#     kids = models.CharField(max_length=256, db_column='kids', null=False, blank=False)
#
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'users'
#
#
# class Nanny(models.Model):
#     user = models.ForeignKey(User, on_delete=models.RESTRICT)
#     name = models.CharField(max_length=256, db_column='name', null=False, blank=False)
#     address = models.CharField(max_length=256, db_column='address', null=False, blank=False)
#     bio = models.CharField(max_length=256, db_column='bio', null=False, blank=False)
#
#     """create links table"""
#     sessions = models.ForeignKey('Session', on_delete=models.RESTRICT, related_name='nanny_sessions')
#     # relations = models.ForeignKey('Relations', on_delete=models.RESTRICT, related_name='nanny_relations')
#     # in_app_exp = ???
#     # phone_number = PhoneNumberField
#     birth_year = models.IntegerField(db_column='birth_year', null=False)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "nannys"
#
