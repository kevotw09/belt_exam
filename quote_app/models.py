from django.db import models
import re
# Create your models here.


class UserManager(models.Manager):
    def basic_validation(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['name']) < 2:
            errors['name'] = 'Name should be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters'
        if postData['password'] != postData['confirm_pw']:
            errors['pw'] = 'Password and Confirm Password do not match'
        return errors


class QuoteManager(models.Manager):
    def basic_validation(self, postData):
        errors = {}
        if len(postData['quote']) < 10:
            errors['quote'] = 'Message should be at least 10 characters'
        if len(postData['quoted_by']) < 2:
            errors['quoted_by'] = 'Quoted by should be at least 2 characters'
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Quote(models.Model):
    quote = models.TextField()
    quoted_by = models.CharField(max_length=255)
    quote_owner = models.ForeignKey(
        User, related_name="quote_by_user", on_delete=models.CASCADE)
    user_like = models.ManyToManyField(User, related_name='liked_quote')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()
