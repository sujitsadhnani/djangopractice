from pickle import TRUE
from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True, default=' ')
    middle_name = models.CharField(max_length=100, null=True, blank=True, default=' ')
    sur_name = models.CharField(max_length=100, null=True, blank=True,default=' ')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    user_since_datetime = models.DateTimeField(auto_now_add=True)
    is_doctor = models.BooleanField(default=False)
    is_doctor_verified = models.BooleanField(default=False)
    is_site_admin = models.BooleanField(default=False)
    reset_otp = models.IntegerField(null=True, blank=True)
    medical_license = models.CharField(max_length=100, null=True, blank=True)
    doc_speciality = models.CharField(max_length=200, null=True, blank=True)
    doc_score = models.BigIntegerField(null=True, blank=True)


class med_post(models.Model):
    med_post_id = models.BigAutoField(primary_key=True)
    med_post_datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    med_post_text = models.TextField(null=True, blank=True)
    med_post_likes = models.BigIntegerField(default=0, null=True, blank=True)
    med_post_doc_likes = models.BigIntegerField(default=0, null=True, blank=True)
    med_post_score = models.BigIntegerField(default=0, null=True, blank=True)
  

class like(models.Model):
    med_post = models.ForeignKey(med_post, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    like_datetime = models.DateTimeField(auto_now_add=True)

