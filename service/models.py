from django.db import models

class Services(models.Model):
    serviceid = models.IntegerField(db_column='ServiceID', primary_key=True)  # Field name made lowercase.
    name_service = models.CharField(db_column='Name_service', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'services'