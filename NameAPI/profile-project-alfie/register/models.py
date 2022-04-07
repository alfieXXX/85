from django.db import models
from bo.common import MReference

# class MReference(models.Model):
#     reference_id = models.BigIntegerField(primary_key=True)
#     reference_group = models.CharField(max_length=100)
#     reference_code = models.CharField(max_length=20)
#     reference_shortdesc = models.CharField(max_length=100)
#     reference_longdesc = models.CharField(
#                             max_length=200,
#                             null=True,
#                             blank=True,
#                             default=None  
#                             )
#     reference_desc = models.CharField(max_length=500)
#     reference_groupcode = models.CharField(
#                             max_length=20,
#                             null=True,
#                             blank=True,
#                             default=None                            
#                             )
#     reference_tablestatus_id = models.BigIntegerField()
#     date_added = models.DateTimeField(auto_now_add=True)
#     addedby_user_id = models.BigIntegerField()
#     updatedby_user_id = models.BigIntegerField(
#         null=True,
#         blank=True
#     )
#     date_updated = models.DateTimeField(
#         null=True,
#         blank=True,
#         default=None
#     )

class MUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=10, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    username = models.CharField(max_length=500, null=True, blank=True)
    momo = models.CharField(max_length=500, null=True, blank=True)
    password = models.CharField(max_length=500, null=True, blank=True)
    reference_tablestatus_fk = models.ForeignKey(MReference, on_delete=models.PROTECT, related_name="muser_tablestatus", default=1)
    date_added = models.DateTimeField(auto_now_add=True)
    addedby_user_id = models.BigIntegerField(default=1)
    updatedby_user_id = models.BigIntegerField(
        null=True,
        blank=True
    )
    date_updated = models.DateTimeField(
        null=True,
        blank=True,
        default=None
    )    