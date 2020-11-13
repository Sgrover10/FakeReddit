from django.db import models
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, postdata):
        errors={}
        if len(postdata['fname'])<2:
            errors['fname']="First name must be at least 2 characters"
        if len(postdata['lname'])<2:
            errors['lname']="Last name must be at least 2 characters"

        if not EMAIL_REGEX.match(postdata['email']):
            errors['email'] = "Invalid email address!"

        email_check = self.filter(email=postdata['email'])
    ##prevent accounts with same email
        if email_check:
            errors['email'] = "Email already in use"
    ##validate passwords
        if len(postdata['pw'])<8:
            errors['pw']="Password must be at least 8 characters"
        if postdata['pw'] != postdata['cpw']:
            errors['pw']="Passwords must match"
        return errors

    def authenticate(self, email, password):
        users_email = self.filter(email=email)
        if not users_email:
            return False
        user = users_email[0]
        return bcrypt.checkpw(password.encode(), user.password.encode())

    def register(self, postdata):
        hash_pw=bcrypt.hashpw(postdata['pw'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name=postdata['fname'],
            last_name=postdata['lname'],
            email=postdata['email'],
            password=hash_pw
            )

class User(models.Model):
    first_name=models.CharField(max_length=55)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=UserManager()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

