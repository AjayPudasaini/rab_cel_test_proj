from django.apps import AppConfig

class OnlineAccountAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "rab_test_cel.online_account"

    # def ready(self):
    #     from rab_test_cel.online_account.tasks import listen_to_rabbitmq
    #     listen_to_rabbitmq.delay()