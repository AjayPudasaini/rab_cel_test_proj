from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class OnlineAccount(models.Model):
    """
    This models is created to save the response receive from rabbit mq.
    """

    task_id = models.TextField(
        verbose_name=_("Task ID"),
        help_text=_("The ID generate from rabbit mq."),
    )

    account_detail = models.JSONField(
        verbose_name=_("Account Details"),
        help_text=_("The json that include all the response."),
    )

    status = models.BooleanField(
        verbose_name=_("status"), help_text=_("The account status."), default=False
    )

    class Meta:
        db_table = "online_account"
