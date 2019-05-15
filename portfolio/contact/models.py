from django.db import models
# from django.utils.timezone import datetime

# Create your models here.
class contact(models.Model):
    # today = datetime.today()
    name = models.CharField(max_length =100, null= False)
    email = models.EmailField(help_text = 'null@mail.com')
    message = models.CharField(max_length = 300, null= True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    
    def __str__(self):
        return self.name + ' ' + str(self.date) 


