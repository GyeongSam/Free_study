from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from .serializers.article import ArticleListSerializer, ArticleSerializer
from .serializers.comment import CommentListSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Article, Comment

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def article_list(request):
    print(request.user)
    articles = get_list_or_404(Article)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, article_pk):
    pass