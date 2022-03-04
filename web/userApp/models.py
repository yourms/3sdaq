from django.db import models

# Create your models here.
# class - table
# create table webuser ( user_id varchar2(100) )
class WebUser(models.Model) :
    user_id      = models.TextField(max_length=100)
    user_pwd     = models.TextField(max_length=100)
    user_name    = models.TextField(max_length=100)
    user_point   = models.IntegerField(default=1000)
    user_regdate = models.DateTimeField(auto_now=True)

class SBS(models.Model):
    title = models.TextField(max_length=100)
    url = models.TextField(max_length=100)

