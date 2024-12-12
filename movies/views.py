from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework import filters
from rest_framework.viewsets import ReadOnlyModelViewSet
from movies.models import Actor, Movie, Comment
from movies.serializers import MovieSerializer, ActorSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['imdb', '-imdb']
    search_fields = ['name']
    # @action(detail=True, methods=["GET"])
    # def actors(self, request, *args, **kwargs):
    #     movie = self.get_object()
    #     serializer = ActorSerializer(movie.actors.all(), many=True)
    #     return Response(serializer.data)
    
    
    @action(detail=True, methods=["POST"])
    def add_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_data = request.data
        actor = Actor.objects.create(
                name=actor_data.get('name', ''),
                birthdate=actor_data.get('birthdate', ''),
                gender=actor_data.get('gender', '')
            )

        movie.actors.add(actor)
        movie.save()

        return Response(status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=["POST"])
    def remove_actor(self, request, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data.get('actor_id')
        movie.actors.remove(actor_id)

        return Response(status=status.HTTP_202_ACCEPTED)



class ActorViewSet(ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



class CommentVIewSet(ReadOnlyModelViewSet):
    
    serializer_class = CommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.all()
    
    def perform_create(self, serializer):
        serializer.validated_data["user"] = self.request.user
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        try:
            comment = self.get_object()
            if comment.user != request.user:
                return Response({"error": "You do not have permission to delete this comment."}, status=status.HTTP_403_FORBIDDEN)
            self.perform_destroy(comment)
            return Response({"message": "Comment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({"error": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)