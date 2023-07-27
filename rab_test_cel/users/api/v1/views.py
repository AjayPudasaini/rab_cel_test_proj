from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rab_test_cel.users.api.v1.serializers import CreateUserSerializer


class UserCreateAPIView(APIView):
    permission_classes = []
    serializer_class = CreateUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data":serializer.data, "message":"User Registred"}, status=status.HTTP_201_CREATED)