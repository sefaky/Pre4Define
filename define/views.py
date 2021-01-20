from django.shortcuts import render
from word.models import WordsDefining
from django.core.paginator import Paginator
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px
from word.models import WordsDefining

"""def index(request):
    x_data = ['Action' , 'Adventure' , 'Music' , 'Casual']
    y_data = df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
    plot_div = plot([Scatter(x=x_data , y=y_data ,
                             mode='lines' , name='test' ,
                             opacity=0.8 , marker_color='green')] ,
                    output_type='div')
    return render(request , "plot.html" , context={'plot_div': plot_div})


def index(request):
    df = px.data.gapminder().query("category == 'Action'")
    fig = px.bar(df , y='downloads' , x='word')
    fig.update_traces(texttemplate='%{text:.2s}' , textposition='outside')
    fig.update_layout(uniformtext_minsize=8 , uniformtext_mode='hide')
    fig.show()
    return render(request , "plot.html")"""


def define(request):
    words = WordsDefining.objects.all().order_by('downloads').reverse()
    paginator = Paginator(words , 25)  # Show 25 contacts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {

        'words': page_obj ,
    }

    return render(request , 'define.html' , context)


def homepage(request):
    return render(request , 'base.html')


def plot(request):
    return render(request, 'plot.html')



"""def plot2(request):
    return render(request, 'plot2.html')"""


"""def categorize(request , category):
    words = WordsDefining.objects.filter(category=category)
    context = {

        'words': words ,
    }

    return render(request , 'define.html' , context)"""
