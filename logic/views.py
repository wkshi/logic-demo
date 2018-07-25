from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from logic.models import Logic
from logic.serializers import LogicSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'logic': reverse('logic-list', request=request, format=format)
    })


class LogicList(APIView):
    """
    List all past logic record, or create new logic record.
    """
    def get(self, request, format=None):
        logic = Logic.objects.all()
        serializer = LogicSerializer(logic, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LogicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogicDetail(APIView):
    """
    Retrieve, update or delete a logic record.
    """
    def get_object(self, pk):
        try:
            return Logic.objects.get(pk=pk)
        except Logic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        logic = self.get_object(pk)
        serializer = LogicSerializer(logic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        logic = self.get_object(pk)
        serializer = LogicSerializer(logic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        logic = self.get_object(pk)
        logic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
