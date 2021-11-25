from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post
from posts.api.serializers import PostSerializer

class PostApiView(APIView):
    def get(self, request):
        # posts= Post.objects.all()
        # posts = [post.title for post in Post.objects.all()]
        posts = PostSerializer(Post.objects.all(), many=True)
        return Response(status= status.HTTP_200_OK, data= posts.data)

    def post(self, request):
        post = PostSerializer(data=request.POST)
        post.is_valid(raise_exception=True)
        post.save()
        return Response(status= status.HTTP_200_OK, data= post.data)
        
        # title=request.POST.get('title', "otro")
        # description=request.POST.get('description',"sin descripcion")
        # order=request.POST.get('order',"99")
        # Post.objects.create(title=title, description=description, order=order)
        # return self.get(request)