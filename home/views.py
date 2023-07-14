from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
import yfinance as yf
import plotly.graph_objects as go

# Create your views here.

def index(request):
    return render(request, 'index.html')

def loginn(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('live_data')
        else:
            return redirect("signup")
    return render(request, 'login.html')

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        myuser=User.objects.create_user(username,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'signup.html')

def live_data(request):
    data = yf.download(tickers='BTC-USD', period='5d', interval='15m')
    latest_price = data.iloc[-1]['Close']
    prices = data['Close']

    # Create a line graph using Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=prices, mode='lines', name='Price'))

    # Customize the graph layout
    fig.update_layout(
        title='Bitcoin Price',
        xaxis_title='Date',
        yaxis_title='Price',
        showlegend=True
    )

    # Convert the graph to HTML and pass it to the template
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    context = {
        'graph_html': graph_html,
    }

    return render(request, 'live_data.html', context)


def my_view(request):
    return render(request, 'my_template.html')