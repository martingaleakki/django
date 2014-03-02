from django.core.management.base import BaseCommand, CommandError
import csv
from datetime import datetime

from hedgefund.models import HedgeFund
class Command(BaseCommand):
    args = '<filename>'
    help = 'test command'

    def handle(self, *args, **options):
        with open('/Users/akhillodha/Sliced/dev/djangoProjects/slicedinvesting/fakedata/hedgefunds.csv', 'rU') as csvfile:
         reader = csv.reader(csvfile,)
        
         j=0
         convert=self.convert
         for row in reader:
             if(row[0]=='Name'):
                 continue
             j=j+1
             i=HedgeFund.objects.create()
             i.name = row[0]
             i.type = row[1]
             i.description=row[2]
             i.percCompleted=convert(row[3])
             i.portfolioManager=row[4]
             i.numYearsActive=convert(row[5])
             i.assetsUnderManagement=int(row[6])
             i.managementFees=convert(row[7]) 
             i.performanceFees=convert(row[8]) #TBD - should point to other investors
             i.lockInPeriod=convert(row[9])
             i.reportingFrequency=int(row[10])
             i.capitalRequested=convert(row[11])
             i.capitalRaised=convert(row[12])
             i.parentSyndicates=row[13]
             i.numLikes=int(row[14])
             i.hotness=int(row[15])
             i.returnMetrics=convert(row[16])
             i.originDate=datetime.strptime(row[17] , '%m/%d/%y')
             i.website=row[18]
             i.riskLevel=int(row[19])
             i.location=row[20]    
             i.save()
        csvfile.close()
    
    @staticmethod
    def convert(s):
        return float(s.replace(',',''))