from django.shortcuts import render


def home(request):
    import requests
    import json

    # pk_9838a657f54d4ef0a27147ffd8012c1a
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_9838a657f54d4ef0a27147ffd8012c1a")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
