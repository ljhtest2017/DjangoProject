from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

# Create your views here.
def display_meta(request):
    values = request.META.items()
    values.sort()
    html =[]
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table> ' %'\n'.join(html))

def search_form(request):
    return render(request, 'search_form.html')

def search(request):
    if 'q' in request.GET:
        message = 'You searched for %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render(request,'search_results.html',
                      {'books': books, 'query': q})