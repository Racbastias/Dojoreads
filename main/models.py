from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def basicvalidator(self, postData):
        regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        letters = re.compile(r'^[a-zA-Z. ]+$')

        errors = {}

        if len(postData['name']) < 2:
            errors['name'] = "The name must be 2 letters at least";
        if len(postData['nickname']) < 2:
            errors['nickname'] = "The last name must be 2 letters at least";
        if not regex.match(postData['email']):
            errors['email'] = "invalid e-mail"
        if not letters.match(postData['name']):
            errors['solo_letras'] = "Your name must be only Letters"
        if len(postData['password']) < 4:
            errors['password'] = "The password must be 8 characters at least";
        if postData['password'] != postData['password_confirm'] :
            errors['password_confirm'] = "Both Passwords must be equals "
        return errors

class User(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    avatar = models.URLField(default='https://toppng.com/uploads/preview/roger-berry-avatar-placeholder-11562991561rbrfzlng6h.png')
    password = models.CharField(max_length=70)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    def __str__(self):
        return f"{self.nickname}"

    def __repr__(self):
        return f"{self.nickname}"


class Author(models.Model):
    name = models.CharField(max_length=100, unique = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"
    def __repr__(self):
        return f"{self.name}"

class Book(models.Model):
    title = models.CharField(max_length=100, unique = True)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)
    # authors
    # reviews
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}"
    def __repr__(self):
        return f"{self.title}"

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.review} and {self.rating} stars"
    def __repr__(self):
        return f"{self.review} and {self.rating} stars"