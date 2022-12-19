from rest_framework.response import Response
from rest_framework.decorators import api_view
from .lib.newscraper import Scrap_Bangla_News
from django.core.cache import cache

# Create your views here.
@api_view(['GET'])
def Scrap(request):
    data = Scrap_Bangla_News()
    return Response({
        'status':200,
        'news':data,
    })
