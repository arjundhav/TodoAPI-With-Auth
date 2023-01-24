from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import CheckList, ListItem
from .permissions import IsOwner

from .serializers import CheckListSerializer, ListItemSerializer

#Listing ,Creation
class ListCreateAPIView(ListCreateAPIView): 
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset

    #We can achieve the same thing above by just overriding these method commented below and instead of inherting ListCreateAPIView, we could have used GenericAPIView.
    # def get(self, request, format=None):
    #     data = CheckList.objects.filter(user=request.user)

    #     serializer = self.serializer_class(data, many=True)
    #     serialized_data = serializer.data

    #     return Response(serialized_data, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     # Code for creation
    #     serializer = self.serializer_class(data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

#Read, Update, Delete    
class CheckListAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CheckListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = CheckList.objects.filter(user=self.request.user)
        return queryset



#Creation
class ItemCreateAPIView(CreateAPIView):
    serializer_class = ListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]  


# Retrieve, Update, Delete
class ListItemAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class =ListItemSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = ListItem.objects.filter(user=self.request.user)
        return queryset         

 #We can achieve the same thing above by just overriding these method commented below and instead of inherting RetrieveUpdateDestroyAPIView, we could have used GenericAPIView.

    # def get_object(self, pk):
    #     try:
    #         obj = ListItem.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, obj)
    #         return obj
    #     except ListItem.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk, format=None):
    #     checklist_item = self.get_object(pk)
    #     serializer = self.serializer_class(checklist_item)
    #     serialized_data = serializer.data
    #     return Response(serialized_data, status=status.HTTP_200_OK)

    # def put(self, request, pk, format=None):
    #     checklist_item = self.get_object(pk)
    #     serializer = self.serializer_class(checklist_item, data=request.data, context={'request': request})
    #     if serializer.is_valid():
    #         serializer.save()
    #         serialized_data = serializer.data
    #         return Response(serialized_data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     checklist_item = self.get_object(pk)
    #     checklist_item.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)