from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BookModel

@api_view(['GET'])
def BookListApi(request):
    books = BookModel.objects.all()
    books = [{
        'name': book.name,
        'author': book.author
    }for book in books]
    return Response(books)

@api_view(['POST'])
def BookCreateApi(request):
    data = request.expandtabs()
    name = data['name']
    author = data['author']
    
    BookModel(name=name, author=author).save()
    return Response({
        'message': 'Book Created'
    })
