from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Show
from .serializers import ShowSerializer


@api_view(["GET"])
def getData(request):
    shows = Show.objects.all()
    serializer = ShowSerializer(shows, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def addShow(request):
    serializer = ShowSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)  # Sending back the item created
