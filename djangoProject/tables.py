import django_tables2 as tables
from .models import Threat

class ThreatTable(tables.Table):
		date = tables.DateTimeColumn(format ='Y M d, h:m:s')
		filename = tables.Column()
		action = tables.Column()
		submit_type = tables.Column()
		rating = tables.Column()
		class Meta:
			model = Threat
			template_name = 'django_tables2/bootstrap.html'
