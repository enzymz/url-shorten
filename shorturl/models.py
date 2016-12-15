from django.db import models

class UrlShort(models.Model):
    ori_link = models.CharField(max_length=255)
    hash_link = models.CharField(max_length=255)
    short_link = models.CharField(unique=True, db_index=True, max_length=50)

    def __str__(self):
        return self.short_link

class UserAgent(models.Model):
   user_agent = models.CharField(max_length=255)
   short_link = models.ForeignKey(UrlShort)
   user_ip = models.CharField(max_length=50)
   user_national = models.CharField(max_length=50)
   date_create = models.DateField(auto_now=True)
 
   def __str__(self):
       return self.user_ip
