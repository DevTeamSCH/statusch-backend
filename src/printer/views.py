import requests
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models


class PrintersByUsers(APIView):
    def get(self, request, format=None):
        try:
            url = models.PrinterProxy.objects.get().url
            res = requests.get(url)

            return Response(res.json())
        except requests.exceptions.ConnectionError as e:
            return Response({"details": "Connection Error."})
