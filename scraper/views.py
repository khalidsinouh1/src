from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json
import numpy as np

# Create your views here.
def h1(request):
	return render(request, 'home.html')


def scrap(request):
	url = request.GET.get('url')
	rq = requests.get(url).text
	soup = BeautifulSoup(rq, 'html.parser')
	iframes = soup.find_all('iframe')
	lst = []
	for x in iframes:
		lst.append([str(x)])

	js = json.dumps(lst)


	return render(request, 'view.html', {'lst':js})