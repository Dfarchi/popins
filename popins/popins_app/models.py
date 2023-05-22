from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, db_column="user_id", on_delete=models.CASCADE)
    is_parent = models.BooleanField(db_column="is_parent")
    # is_nanny = models.BooleanField(db_column='is_nanny')
    name = models.CharField(max_length=256, db_column="name", blank=False)
    bio = models.TextField(max_length=256, db_column="bio", null=True, blank=True)
    birth_year = models.IntegerField(db_column="birth_year", null=True)
    address = models.CharField(
        max_length=256, db_column="address", null=True, blank=True
    )
    social = models.URLField(max_length=200, null=True, blank=True)
    profile_pic = models.URLField(max_length=200, null=True, blank=True)

    # relations = models.ForeignKey('Relations', on_delete=models.RESTRICT, related_name='parent_relations')
    # phone_number = PhoneNumberField
    def __str__(self):
        return self.name

    # def _create(
    #     self,
    #     username,
    #     is_parent,
    #     user,
    # ):
    #     profile = self.model(user=user, username=username, is_parent=is_parent)
    #     profile.save(using=self._db)
    #     return profile

    class Meta:
        db_table = "profiles"


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=None)
    date = models.DateField(db_column="date", null=False, auto_now_add=True)
    salary = models.IntegerField(db_column="salary", default=50)
    note = models.TextField(max_length=256, db_column="note", null=False, blank=False)
    has_happened = models.BooleanField(null=False, default=False)
    interested_nannies = models.ManyToManyField(
        User, through="Interest", related_name="sessions"
    )

    def __str__(self):
        return f"{self.user.profile.name} on {self.date}"

    class Meta:
        db_table = "sessions"


class Interest(models.Model):
    nanny = models.ForeignKey(
        User, on_delete=models.RESTRICT, related_name="interests", default=None
    )
    session = models.ForeignKey(Session, on_delete=models.RESTRICT, default=None)
    note = models.TextField(max_length=256, db_column="note", null=False, blank=False)
    talked = models.BooleanField(null=False, blank=False, default=False)
    status = models.BooleanField(null=False, blank=False, default=False)

    class Meta:
        db_table = "interest"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, default=None)
    review = models.TextField(db_column="review", null=False)
    review_date = models.DateField(db_column="date", null=False, auto_now_add=True)

    class Meta:
        db_table = "reviews"
