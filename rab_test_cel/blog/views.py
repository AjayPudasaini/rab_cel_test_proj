from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from rab_test_cel.online_account.publisher import RabbitMQServer
from rest_framework.response import Response


class PublishMessage(APIView):
    permission_classes = []

    @extend_schema(
        operation_id="Publish Message API",
        description="""Publish message to create online account""",
        methods=["post"],
    )

    def post(self, request, *args, **kwargs):
        account_data = request.GET.get("account_data")
        print("l38", account_data)
        server = RabbitMQServer(queue="datum_taml_broker")
        acc_data = {"data1": "test 1", "data2": "test 2"}
        server.publish(payload=acc_data)
        return Response({"message": "Message Published"})