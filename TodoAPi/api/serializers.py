from rest_framework import serializers

from .models import CheckList, ListItem

class ListItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())   
    class Meta:
        model = ListItem
        fields = '__all__'

class CheckListSerializer(serializers.ModelSerializer):
    items = ListItemSerializer(source='listitem_set', many=True, read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CheckList
        fields = '__all__'
