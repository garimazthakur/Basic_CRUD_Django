from email import message
# from rest_framework import generics, permissions
from .models import Snippet
from .serializers import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
# from .permissions import IsOwnerOrReadOnly
# from doc.snippets import serializers 

# class SnippetList(generics.ListCreateAPIView):
#     #Allow: GET, POST, HEAD, OPTIONS(create a read-write endpoint that lists all available Snippet instances)
#     queryset= Snippet.objects.all()
#     serializer_class = SnippetSerializer
    
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     Retrieve, update or delete a snippet instance.
#     for a read-write-delete endpoint for each individual Snippet.
#     queryset = Snippet.objects.all()
#     serializer_class= SnippetSerializer

class SnippetList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    def get(self, request, format=None):
        snippets=Snippet.objects.all()
        serializer=SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

class CreateSnippet(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request,format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)




class SnippetDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]
    def get_object(self,request,  pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    # def get(self, request, pk, format=None):
    #     snippet=self.get_object(pk)
    #     serializer=SnippetSerializer(snippet)
    #     return Response(serializer.data)
class GetSnippetDetails(APIView):
    def get(self, request, pk):
        try:
            snippet=Snippet.objects.get(pk=pk)
            serializer=SnippetSerializer(snippet)
            print(serializer.data)
            print("****************************************************************")

            return Response(serializer.data)
        except:
            raise Http404

class UpdateSnippetDetail(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]      
    def put(self, request, pk,format=None):
        try:
            snippet=Snippet.objects.get(pk=pk)
            serializer= SnippetSerializer(snippet, data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Snippet.DoesNotExist:
            return Response({"message": "Snippet does not exist"})
        


            # snippet=self.get_object(pk)
            # serializer= SnippetSerializer(snippet, data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response(serializer.data)
            # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteSnippetDetail(APIView):
    def delete(self, request, pk):
        try:
            snippet=Snippet.objects.get(pk=pk)
            snippet.delete()
            return Response({"message":f"The data with the id {pk} is deleted"})
        except Snippet.DoesNotExist:
            return Response({"message":"Snippet does not exist"})
           
        
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly] 
    #   
    # def get_object(self,request,  pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class UserList(generics.ListAPIView):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer

# class UserDetail(generics.RetrieveAPIView):
#     queryset=User.objects.all()
#     serializer_class= UserSerializer

from affinda import AffindaAPI, TokenCredential
class Affinda(APIView):
    def affinda(self,request ):
        if request.method == 'POST':
            if 'file' not in request.files:
                return Response({"message": 'No file provided/Check the key, spelling or any space after or in the key.'})
            file = request.files['file']
            if file.filename == '':
                return Response({"message": 'No file selected.'})
            
        token = "882cef4ed52c12069650b808d49bde924b5252c4"
        credential = TokenCredential(token=token)
        client = AffindaAPI(credential=credential)
        print(file.filename)
        # folder= os.path.join(UPLOAD_FOLDER, file.filename)
        # print(folder)
        with open(file.filename, "rb") as f:
            resume = client.create_resume(file=f)
            data = resume.as_dict()
        

     
        return Response({"data": data})








    





