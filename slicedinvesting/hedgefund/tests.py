from django.test import TestCase
from hedgefund.models import HedgeFund
from datetime import datetime
# Create your tests here.

class HedgeFundTestCase(TestCase):
    
    def setUp(self):
        
        self.__hFName = "AK Capital Management"
        self.__hFType = "Fixed Income"
        self.__hFDescription="Invests in Corporate Bonds"
        self.__hFCompletionPerc= 100
        self.__hFPortfolioManager="Akhil Lodha"
        self.__hFNumYearsActive= 1.5 
        self.__hFAssetsUnderManagement= 50 #In Millions
        self.__hFManagementFees=2
        self.__hFPerformanceFees=20
        self.__hFLockInPeriod=2
        self.__hFReportingFrequency=1 
        self.__hFCapitalRequested=750000
        self.__hFCapitalRaised=500000
        self.__hFParentSyndicates="A, B" 
        self.__hFNumLikes=5000
        self.__hFHotness=75 # On a scale of 100
        self.__hFReturnMetrics=30.5 
        self.__hFOriginDate=datetime.today().date()
        self.__hFWebsite="www.akcapital.com"
        
        
        self.__hedgeFund=HedgeFund.objects.create(name=self.__hFName,
                                                  type=self.__hFType,
                                                  description=self.__hFDescription,
                                                  percCompleted=self.__hFCompletionPerc,
                                                  portfolioManager=self.__hFPortfolioManager,
                                                  numYearsActive=self.__hFNumYearsActive,
                                                  assetsUnderManagement=self.__hFAssetsUnderManagement,
                                                  managementFees=self.__hFManagementFees,
                                                  performanceFees=self.__hFPerformanceFees,
                                                  lockInPeriod=self.__hFLockInPeriod,
                                                  reportingFrequency=self.__hFReportingFrequency,
                                                  capitalRequested=self.__hFCapitalRequested,
                                                  capitalRaised=self.__hFCapitalRaised,
                                                  parentSyndicates=self.__hFParentSyndicates,
                                                  numLikes=self.__hFNumLikes,
                                                  hotness=self.__hFHotness,
                                                  returnMetrics=self.__hFReturnMetrics,
                                                  originDate=self.__hFOriginDate,
                                                  website=self.__hFWebsite)
                                                 
        return
    
    def testHedgeFundName(self):
        self.assertNotEqual(HedgeFund.objects.get(name=self.__hFName), second=None)
        
    def testHedgeFundType(self):
        self.assertNotEqual(HedgeFund.objects.get(type=self.__hFType), second=None)
        
    def testHedgeFundDescription(self):
        self.assertNotEqual(HedgeFund.objects.get(description=self.__hFDescription), second=None)

    def testHedgeFundCompletionPerc(self):
        self.assertNotEqual(HedgeFund.objects.get(completionPerc=self.__hFCompletionPerc), second=None)
    
    def testHedgeFundPortfolioManager(self):
        self.assertNotEqual(HedgeFund.objects.get(portfolioManager=self.__hFPortfolioManager), second=None)
     
    def testHedgeFundNumYearsActive(self):
        self.assertNotEqual(HedgeFund.objects.get(numYearsActive=self.__hFNumYearsActive), second=None)
   
    def testHedgeFundAssetsUnderManagement(self):
        self.assertNotEqual(HedgeFund.objects.get(assetsUnderManagement=self.__hFAssetsUnderManagement), second=None)
   
    def testHedgeFundPerformanceFees(self):
        self.assertNotEqual(HedgeFund.objects.get(performanceFees=self.__hFPerformanceFees), second=None)
   
    def testHedgeFundManagementFees(self):
        self.assertNotEqual(HedgeFund.objects.get(managementFees=self.__hFManagementFees), second=None)
   
    def testHedgeFundLockInPeriod(self):
        self.assertNotEqual(HedgeFund.objects.get(lockInPeriod=self.__hFLockInPeriod), second=None)
   
    def testHedgeFundCapitalRequested(self):
        self.assertNotEqual(HedgeFund.objects.get(capitalRequested=self.__hFCapitalRequested), second=None)
   
    def testHedgeFundCapitalRaised(self):
        self.assertNotEqual(HedgeFund.objects.get(capitalRaised=self.__hFCapitalRaised), second=None)
   
    def testHedgeFundParentSyndicates(self):
        self.assertNotEqual(HedgeFund.objects.get(parentSyndicates=self.__hFParentSyndicates), second=None)
   
    def testHedgeFundNumLikes(self):
        self.assertNotEqual(HedgeFund.objects.get(numLikes=self.__hFNumLikes), second=None)
   
    def testHedgeFundHotness(self):
        self.assertNotEqual(HedgeFund.objects.get(hotness=self.__hFHotness), second=None)
   
    def testHedgeFundReturnMetrics(self):
        self.assertNotEqual(HedgeFund.objects.get(returnMetrics=self.__hFReturnMetrics), second=None)
    
    def testHedgeFundOriginDate(self):
        self.assertNotEqual(HedgeFund.objects.get(originDate=self.__hFOriginDate), second=None)
    
    def testHedgeFundWebsite(self):
        self.assertNotEqual(HedgeFund.objects.get(website=self.__hFWebsite), second=None)
       