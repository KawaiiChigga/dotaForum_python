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
@api_view(['GET'])
def getAllUser(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

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

# /account/{uid}/
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
@api_view(['GET'])
def getAllCategories(request):
    if request.method == 'GET':
        queryset = Categories.objects.all()
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)

# /categories/{category}/
@api_view(['GET'])
def getCategory(request, category):
    if request.method == 'GET':
        queryset = Categories.objects.all().filter(category=category)
        serializer = CategoriesSerializer(queryset, many=True)
        return Response(serializer.data)

#---------------------COMMENT-----------------------------

# /comment/getall
@api_view(['GET'])
def getAllComment(request):
    if request.method == 'GET':
        queryset = Comment.objects.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

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
def getCommentById(request,id_comment):
    if request.method == 'GET':
        queryset = Comment.objects.all().filter(id_comment=id_comment)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

# /comment/delete/{id_comment}/
@api_view(['GET'])
def deleteComment(request,id_comment):
    if request.method == 'GET':
        queryset = Comment.objects.all().filter(id_comment=id_comment)
        serializer = CommentSerializer(queryset, many=True)
        if (serializer.is_valid()):
            serializer.remove()
            return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /comment/udpate/{pk}
@api_view(['PUT'])
def updateComment(request, pk):
    try:
        queryset = Comment.objects.get(pk=pk)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CommentSerializer(queryset, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#--------------------LIKEDISLIKES------------------------------

# /likes/getall/
@api_view(['GET'])
def getAllLikes(request):
    if request.method == 'GET':
        queryset = Likes.objects.all()
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

# /likes/delete/{id_post}/{id_user}
@api_view(['GET'])
def deleteLike(id_post, id_user):
    queryset = Likes.objects.all().filter(id_post=id_post,id_user=id_user)
    serializer = LikesSerializer(queryset, many=True)
    if(serializer.is_valid()):
        serializer.remove()
        return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /dislikes/getall/
@api_view(['GET'])
def getAllDislikes(request):
    if request.method == 'GET':
        queryset = Dislikes.objects.all()
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

#----------------------POST----------------------------

#/post/getall/{jenis}/
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

# /post/bycategory/{category}/{sort}/
@api_view(['GET'])
def getPostByCategory(request, category, sort):
    category = category - 1
    if request.method == 'GET':
        if sort == 'new':
            queryset = Post.objects.all().filter(id_category=category).order_by('-date_time')
        elif sort == 'top':
            queryset = Post.objects.all().filter(id_category=category).order_by('-like_post')
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

#--------------------------------------------- TRAKHIR -----------------------------------------------------------------

#---------------------MESSAGE-----------------------------

@api_view(['GET'])
def getAllMessage(request):
    if request.method == 'GET':
        queryset = Message.objects.all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

# /message/
@api_view(['PUT'])
def insertMessage(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /message/inbox/{id_receiver}/
#harusnya ada -> group by id_sender order by date_time
# @api_view(['GET'])
# def getInbox(request, id_receiver):
#     if request.method == 'GET':
#         queryset = Message.objects.all().filter(id_receiver=id_receiver)
#         serializer = MessageSerializer(queryset, many=True)
#         return Response(serializer.data)

# /message/inbox/{id_sender}/{id_receiver}/
#harusnya ada -> order by date_time
# @api_view(['GET'])
# def getMsgFromId(request, id_receiver, id_sender):
#     if request.method == 'GET':
#         queryset = Message.objects.all().filter(id_receiver=id_receiver,id_sender=id_sender) | Message.objects.all().filter(id_receiver=id_sender,id_sender=id_receiver)
#         serializer = MessageSerializer(queryset, many=True)
#         return Response(serializer.data)

# /message/delete/{id_message}/
@api_view(['GET'])
def deleteMessage(id_message):
    queryset = Message.objects.all().filter(id_message=id_message)
    serializer = MessageSerializer(queryset, many=True)
    if (serializer.is_valid()):
        serializer.remove()
        return Response(serializer.errors, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# /message/update/{pk}
@api_view(['PUT'])
def updateMessage(request, pk):
    try:
        queryset = Message.objects.get(pk=pk)
    except Message.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MessageSerializer(queryset, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#----------------------REPLY----------------------------
@api_view(['GET'])
def getAllReply(request):
    if request.method == 'GET':
        queryset = Reply.objects.all()
        serializer = ReplySerializer(queryset, many=True)
        return Response(serializer.data)

#----------------------REPORT----------------------------

@api_view(['GET'])
def getAllReport(request):
    if request.method == 'GET':
        queryset = Report.objects.all()
        serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data)

