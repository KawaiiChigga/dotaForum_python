from django.db.models import QuerySet
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics, views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dota.models import User, Categories, Comment, Likes, Dislikes, Post, Message, Reply, Report
from dota.serializer import UserSerializer, CategoriesSerializer, CommentSerializer, LikesSerializer, DislikesSerializer
from dota.serializer import PostSerializer, MessageSerializer, ReplySerializer, ReportSerializer

# Create your views here.

#-----------------------USER---------------------------

# /user/getall/
# @api_view(['GET'])
# def getAllUser(request):
#     if request.method == 'GET':
#         queryset = User.objects.all()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)

# /user/insert/
@api_view(['PUT'])
def insertUser(request):
    if request.method == 'PUT':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /user/checkLogin/
@api_view(['POST'])
def checkLogIn(request):
    if request.method == 'POST':
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        queryset = User.objects.get(username=username, password=password)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

# /user/{uid}/
@api_view(['GET', 'PUT'])
def user(request, pk):
    try:
        queryset = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#----------------------CATEGORIES----------------------------

# /categories/getall/
# @api_view(['GET'])
# def getAllCategories(request):
#     if request.method == 'GET':
#         queryset = Categories.objects.all()
#         serializer = CategoriesSerializer(queryset, many=True)
#         return Response(serializer.data)

# /categories/{category}/
@api_view(['GET'])
def getCategory(request, category):
    if request.method == 'GET':
        queryset = Categories.objects.all().filter(category=category)
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)

#---------------------COMMENT-----------------------------

# /comment/getall
# @api_view(['GET'])
# def getAllComment(request):
#     if request.method == 'GET':
#         queryset = Comment.objects.all()
#         serializer = CommentSerializer(queryset, many=True)
#         return Response(serializer.data)

# /comment/
@api_view(['PUT'])
def insertComment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /comment/{id_comment}/
@api_view(['GET'])
def getCommentById(request,id_post):
    if request.method == 'GET':
        queryset = Comment.objects.all().filter(id_post=id_post)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

# /comment/delete/{id_comment}/
@api_view(['GET'])
def deleteComment(request,id_comment):
    if request.method == 'GET':
        queryset = Comment.objects.get(id_comment=id_comment)
        queryset.delete()
        return Response()

# /comment/udpate/{pk}
# @api_view(['PUT'])
# def updateComment(request, pk):
#     try:
#         queryset = Comment.objects.get(pk=pk)
#     except Comment.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     serializer = CommentSerializer(queryset, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#--------------------LIKEDISLIKES------------------------------

# /likes/getall/
@api_view(['GET'])
def getAllLikes(request,id_post):
    if request.method == 'GET':
        queryset = Likes.objects.all().filter(id_post=id_post)
        serializer = LikesSerializer(queryset, many=True)
        return Response(serializer.data)

# /likes/
@api_view(['PUT'])
def addLike(request):
    if request.method == 'PUT':
        serializer = LikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /likes/delete/{pk}/
@api_view(['GET'])
def deleteLike(request,pk):
    if request.method == 'GET':
        queryset = Likes.objects.get(pk=pk)
        queryset.delete()
        return Response()

# /dislikes/getall/
@api_view(['GET'])
def getAllDislikes(request,id_post):
    if request.method == 'GET':
        queryset = Dislikes.objects.all().filter(id_post=id_post)
        serializer = DislikesSerializer(queryset, many=True)
        return Response(serializer.data)

# /dislikes/
@api_view(['PUT'])
def addDislike(request):
    if request.method == 'PUT':
        serializer = DislikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /dislikes/delete/{pk}
@api_view(['GET'])
def deleteDislike(request,pk):
    if request.method == 'GET':
        queryset = Dislikes.objects.get(pk=pk)
        queryset.delete()
        return Response()

#----------------------POST----------------------------

#/post/{jenis}/
@api_view(['GET'])
def getAllPost(request,jenis):
    if request.method == 'GET':
        queryset = Post.objects.all().order_by('-like_post')
        if jenis == 'new':
            queryset = Post.objects.all().order_by('-date_time')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

#/post/search/{judul}/
@api_view(['GET'])
def getPostSearch(request, judul):
    if request.method == 'GET':
        queryset = Post.objects.all().filter(judul__icontains=judul).order_by('-like_post')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

# /post/category/{category}/{sort}/
@api_view(['GET'])
def getPostByCategory(request, category, sort):
    id_cat = int(category) - 1
    if request.method == 'GET':
        if sort == 'new':
            queryset = Post.objects.all().filter(id_category=id_cat).order_by('-date_time')
        elif sort == 'top':
            queryset = Post.objects.all().filter(id_category=id_cat).order_by('-like_post')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

# /post/profile/{id_user}/
@api_view(['GET'])
def getProfilePost(request, id_user):
    if request.method == 'GET':
        queryset = Post.objects.all().filter(id_user=id_user)
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

# /post/
@api_view(['PUT'])
def insertPost(request):
    if request.method == 'PUT':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /post/{pk}/
@api_view(['GET'])
def getPostById(request, pk):
    if request.method == 'GET':
        queryset = Post.objects.get(pk=pk)
        serializer = PostSerializer(queryset)
        return Response(serializer.data)

# /post/{pk}/
@api_view(['GET', 'PUT'])
def post(request, pk):
    try:
        queryset = Post.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#---------------------MESSAGE-----------------------------

# @api_view(['GET'])
# def getAllMessage(request):
#     if request.method == 'GET':
#         queryset = Message.objects.all()
#         serializer = MessageSerializer(queryset, many=True)
#         return Response(serializer.data)

# /message/
@api_view(['PUT'])
def insertMessage(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /message/inbox/{id_receiver}/
#harusnya ada -> group by id_sender
@api_view(['GET'])
def getInbox(request, id_receiver):
    if request.method == 'GET':
        query = Message.objects.all().query
        query.group_by = ['id_sender']
        queryset = QuerySet(query=query, model=Message).filter(id_receiver=id_receiver).order_by('date_time')
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

# /message/inbox/{id_sender}/{id_receiver}/
@api_view(['GET'])
def getMsgFromId(request, id_receiver, id_sender):
    if request.method == 'GET':
        queryset = Message.objects.all().filter(id_receiver=id_receiver,id_sender=id_sender).order_by('date_time') | Message.objects.all().filter(id_receiver=id_sender,id_sender=id_receiver).order_by('date_time')
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

# /message/delete/{pk}/
# @api_view(['GET'])
# def deleteMessage(request,id_message):
#     if request.method == 'GET':
#         queryset = Message.objects.get(id_message=id_message)
#         queryset.delete()
#         return Response()


# /message/update/{pk}
# @api_view(['PUT'])
# def updateMessage(request, pk):
#     try:
#         queryset = Message.objects.get(pk=pk)
#     except Message.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     serializer = MessageSerializer(queryset, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#----------------------REPLY----------------------------
# /reply/{id_comment}/
@api_view(['GET'])
def getReplyByCommentId(request,id_comment):
    if request.method == 'GET':
        queryset = Reply.objects.all().filter(id_comment=id_comment)
        serializer = ReplySerializer(queryset, many=True)
        return Response(serializer.data)

# /reply/delete/{pk}/
@api_view(['GET'])
def deleteReply(request, pk):
    if request.method == 'GET':
        queryset = Reply.objects.get(pk=pk)
        queryset.delete()
        return Response()

# /reply/
@api_view(['PUT'])
def insertReply(request):
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#----------------------REPORT----------------------------

# @api_view(['GET'])
# def getAllReport(request):
#     if request.method == 'GET':
#         queryset = Report.objects.all()
#         serializer = ReportSerializer(queryset, many=True)
#         return Response(serializer.data)
