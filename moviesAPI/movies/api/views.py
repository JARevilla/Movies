from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
import requests
from bs4 import BeautifulSoup
from movies.models import Movie
from movies.serializers import MovieSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def getMovieFunction(request):
    title = request.query_params.get('title', None)
    sitename = request.query_params.get('sitename', None)

    if not title:
        return Response({"error": "Title parameter is required"}, status=400)

    movies = Movie.objects.filter(title__icontains=title)
    
    if sitename:
        movies = movies.filter(sitename__icontains=sitename)

    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([AllowAny])
def SaveMovieFunction(request):
    title = request.data.get('title')
    link = request.data.get('pagelink')
    sitename = request.data.get('sitename')
    image = request.data.get('image')
    
    #query movies table for duplicate title and sitename
    movie = Movie.objects.filter(title=title, sitename=sitename).first()

    if movie:
        # If the movie already exists, update its details
        movie.pagelink = link
        movie.image = image
        movie.save()
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        # If the movie does not exist, create a new one
        movie_data = {
            'title': title,
            'pagelink': link,
            'sitename': sitename,
            'image': image
        }
        serializer = MovieSerializer(data=movie_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def BulkMovie(request):
    movies_data = request.data.get('movies', [])  # Expecting an array under 'movies'
    
    if not movies_data:
        return Response({"error": "No data provided"}, status=status.HTTP_400_BAD_REQUEST)

    movie_instances = []
    errors = []
    for movie_data in movies_data:
        title = movie_data.get('title')
        sitename = movie_data.get('sitename')
        
        # Check if a movie with the same title and sitename already exists
        movie = Movie.objects.filter(title=title, sitename=sitename).first()

        if movie:
            # Update existing movie
            serializer = MovieSerializer(movie, data=movie_data, partial=True)
        else:
            # Create new movie
            serializer = MovieSerializer(data=movie_data)
        
        if serializer.is_valid():
            movie_instance = serializer.save()
            movie_instances.append(movie_instance)
        else:
            errors.append(serializer.errors)

    if errors:
        return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"success": f"{len(movie_instances)} movies processed"}, status=status.HTTP_201_CREATED)

