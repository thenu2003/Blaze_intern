from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Create your views here.

def index(request):
    return render(request, 'index.html')

def cards(request):
    return render(request, "cards.html")

def loginn(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('cards')
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
    if request.method == "POST":
        selected_option = request.POST.get('select', None)
        ticker = None
        if selected_option == 'Bitcoin':
            ticker = 'BTC-USD'
        elif selected_option == 'Etherum':  # Updated to 'Etherum'
            ticker = 'ETH-USD'
        elif selected_option == 'Tether':   # Updated to 'Tether'
            ticker = 'USDT-USD'
        elif selected_option == 'BNB':      # Updated to 'BNB'
            ticker = 'BNB-USD'
        elif selected_option == 'XRP':      # Updated to 'XRP'
            ticker = 'XRP-USD'
        elif selected_option == 'DOGE':     # Updated to 'DOGE'
            ticker = 'DOGE-USD'
        if ticker:
            data = yf.download(tickers=ticker, period='5d', interval='15m')
            latest_price = data.iloc[-1]['Close']
            prices = data[['Open', 'High', 'Low', 'Close']]
            average = data['Close'].mean()
            average_price = round(average, 2)

            # Create a candlestick graph using Plotly
            fig = go.Figure(data=[go.Candlestick(x=data.index,
                                                open=prices['Open'],
                                                high=prices['High'],
                                                low=prices['Low'],
                                                close=prices['Close'])])

            # Customize the graph layout
            fig.update_layout(
                title=f'{selected_option} Price',
                xaxis_title='Date',
                yaxis_title='Price',
                showlegend=True
            )

            # Convert the graph to HTML and pass it to the template
            graph_html= fig.to_html(full_html=False, include_plotlyjs='cdn')

            # Fetch current close price (last available price)
            data = yf.download(tickers=ticker, period="1d", interval="1m")
            close_price = data['Close'][0]
            close = round(close_price, 2)

            # Fetch current real-time price
            datas = yf.download(tickers=ticker, period="1d", interval="1m")
            current_price = datas['Close'][-1]
            current = round(current_price, 2)

            context = {
                'graph_html': graph_html,
                'average': average_price,
                'close_price': close,
                'Current_price': current
            }

            return render(request, 'live_data.html', context)

   # For GET requests or when no option is selected 
    return render(request, 'live_data.html')

def live_data1(request):
    if request.method == "POST":
        selected_option = request.POST.get('select', None)
        ticker = None
        if selected_option == 'NIFTY 50':    # Added Nifty ticker
            ticker = '^NSEI'  # Nifty 50 index
        elif selected_option == 'NIFTY Bank':
            ticker = '^NSEBANK'
        if ticker:
            data = yf.download(tickers=ticker, period='5d', interval='15m')
            latest_price = data.iloc[-1]['Close']
            prices = data[['Open', 'High', 'Low', 'Close']]
            average = data['Close'].mean()
            average_price = round(average, 2)

            # Create a candlestick graph using Plotly
            fig = go.Figure(data=[go.Candlestick(x=data.index,
                                                open=prices['Open'],
                                                high=prices['High'],
                                                low=prices['Low'],
                                                close=prices['Close'])])

            # Customize the graph layout
            fig.update_layout(
                title=f'{selected_option} Price',
                xaxis_title='Date',
                yaxis_title='Price',
                showlegend=True
            )

            # Convert the graph to HTML and pass it to the template
            graph_html= fig.to_html(full_html=False, include_plotlyjs='cdn')

            # Fetch current close price (last available price)
            data = yf.download(tickers=ticker, period="1d", interval="1m")
            close_price = data['Close'][0]
            close = round(close_price, 2)

            # Fetch current real-time price
            datas = yf.download(tickers=ticker, period="1d", interval="1m")
            current_price = datas['Close'][-1]
            current = round(current_price, 2)

            context = {
                'graph_html': graph_html,
                'average': average_price,
                'close_price': close,
                'Current_price': current
            }

            return render(request, 'live_data1.html', context)

   # For GET requests or when no option is selected 
    return render(request, 'live_data1.html')

def live_data2(request):
    if request.method == "POST":
        selected_option = request.POST.get('select', None)
        ticker = None
        if selected_option == 'Google':    # Added Nifty ticker
            ticker = 'GOOG'  # Nifty 50 index
        elif selected_option == 'Apple':
            ticker = 'AAPL'
        if ticker:
            data = yf.download(tickers=ticker, period='5d', interval='15m')
            latest_price = data.iloc[-1]['Close']
            prices = data[['Open', 'High', 'Low', 'Close']]
            average = data['Close'].mean()
            average_price = round(average, 2)

            # Create a candlestick graph using Plotly
            fig = go.Figure(data=[go.Candlestick(x=data.index,
                                                open=prices['Open'],
                                                high=prices['High'],
                                                low=prices['Low'],
                                                close=prices['Close'])])

            # Customize the graph layout
            fig.update_layout(
                title=f'{selected_option} Price',
                xaxis_title='Date',
                yaxis_title='Price',
                showlegend=True
            )

            # Convert the graph to HTML and pass it to the template
            graph_html= fig.to_html(full_html=False, include_plotlyjs='cdn')

            # Fetch current close price (last available price)
            data = yf.download(tickers=ticker, period="1d", interval="1m")
            close_price = data['Close'][0]
            close = round(close_price, 2)

            # Fetch current real-time price
            datas = yf.download(tickers=ticker, period="1d", interval="1m")
            current_price = datas['Close'][-1]
            current = round(current_price, 2)

            context = {
                'graph_html': graph_html,
                'average': average_price,
                'close_price': close,
                'Current_price': current
            }

            return render(request, 'live_data2.html', context)

   # For GET requests or when no option is selected 
    return render(request, 'live_data2.html')

def my_view(request):
    return render(request, 'my_template.html')