from django.test import TestCase

# Create your tests here.
class TestAuthenticaton(TestCase):
    def setUP(self):
        admin = models.User()
        admin.username = 'admin'
        admin.is_superuser = True
        admin.set_password('password')
        admin.save()

        user = models.User()
        user.username = 'Squock'
        user.set_password('password')
        user.save()
        
