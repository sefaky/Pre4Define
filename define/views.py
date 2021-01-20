from django.shortcuts import render
from word.models import WordsDefining
from django.core.paginator import Paginator

# Create your views here.



def define(request):
    words = WordsDefining.objects.all().order_by('downloads').reverse()
    paginator = Paginator(words , 25)  # Show 25 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {

        'words':page_obj,
    }


    return render(request, 'define.html',context)

def homepage(request):
    return render(request, 'base.html')


def categorize(request, category):

    words = WordsDefining.objects.filter(category = category)
    context = {

        'words': words ,
    }

    return render(request, 'define.html', context)