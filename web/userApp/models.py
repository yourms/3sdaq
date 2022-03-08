from django.db import models

# Create your models here.
# class - table
# create table webuser ( user_id varchar2(100) )
class WebUser(models.Model) :
    user_id      = models.TextField(max_length=100)
    user_pwd     = models.TextField(max_length=100)
    user_name    = models.TextField(max_length=100)
    user_acct = models.CharField(max_length=100)
    user_amt = models.IntegerField(default=30000000)
    user_regdate = models.DateTimeField(auto_now=True)

class SBS(models.Model):
    title = models.TextField(max_length=100)
    url = models.TextField(max_length=100)

class Comp(models.Model):
    code    = models.IntegerField(primary_key = True)
    name  = models.CharField(max_length=500)
    type  = models.CharField(max_length=100)
    vol   = models.IntegerField(default=100)
    d_1price = models.IntegerField(default=0)
    regdate = models.DateTimeField(auto_now=True)

class Order(models.Model):
    code = models.IntegerField()
    gubun  = models.CharField(max_length=1, default='B')
    price  = models.IntegerField(default=0)
    quan   = models.IntegerField(default=0)
    tquan = models.IntegerField(default=0, null=True)
    buyer  = models.CharField(max_length=50, null=True)
    seller = models.CharField(max_length=50, null=True)
    tradeyn = models.CharField(max_length=1, default='N')
    time1 = models.DateTimeField(auto_now=True)
    time2 = models.DateTimeField(null=True)

class Ballance(models.Model):
    user_id = models.CharField(max_length=50)
    code    = models.IntegerField()
    price  = models.IntegerField(default=0)
    quan   = models.IntegerField(default=0)
    t_price = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user_id","code"],
                name="unique ballance",
            )
        ]