from django.shortcuts import render
from django_tables2 import RequestConfig

from .models import Threat
from .tables import ThreatTable
from django.contrib import messages
import json
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from datetime import datetime


def Threats(request):
	# read json file 
	json_data = open('djangoProject/fixtures/data.json')   
	data = json.load(json_data)
	json_data.close()
	print("ah");
	for d in data:
		d["submit_type"] = d["submit-type"]
		d["date"] = datetime.strptime(d["date"], '%b %d, %Y %H:%M:%S')

	table = ThreatTable(data)
	RequestConfig(request).configure(table)
	return render(request, 'threats.html', {'table': table})

class ThreatFilter(django_filters.FilterSet):
    class Meta:
        model = Threat
        fields = ['date', 'action']

