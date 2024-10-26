from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
# Create your views here.

class PostView(generics.RetrieveAPIView):
    queryset = Post.objects.all()

    # get is for retrieving the data and sending a response to the client
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostSerializer(queryset, many=True) # many=True for multiple objects
        return Response(serializer.data, status=HTTP_200_OK)