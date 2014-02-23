from django.test import TestCase
from investor.models import Investor
from datetime import datetime
# Create your tests here.

class InvestorTestCase(TestCase):
    
    def setUp(self):
        self.__iFirstName="Akhil"
        self.__iLastName="Lodha"
        self.__iBio="I am a rockstar!"
        self.__iPercCompleted=90
        self.__iPic=None
        self.__iAccountValue=30000
        self.__iPortfolioValue=25000
        self.__iFollowers=20
        self.__iFollowing=50
        self.__iSyndicates="A,B"
        self.__iStatusUpdate="I'm going to be rich!"
        self.__iPortfolioReturn=30
        
        self.__investor=Investor.objects.create(firstName=self.__iFirstName,
                                                lastName=self.__iLastName,
                                                bio=self.__iBio,
                                                percCompleted=self.__iPercCompleted,
                                                pic=self.__iPic,
                                                portfolioValue=self.__iPortfolioValue,
                                                accountValue=self.__iAccountValue,
                                                followers=self.__iFollowers,
                                                following=self.__iFollowing,
                                                syndicates=self.__iSyndicates,
                                                statusUpdate=self.__iStatusUpdate,
                                                portfolioReturn=self.__iPortfolioReturn
                                                )
        return
    
    #These are tests to check - null 
    def testInvestorFirstName(self):
        self.assertNotEqual(Investor.objects.get(firstName=self.__iFirstName), second=None)
    
    def testInvestorLastName(self):
        self.assertNotEqual(Investor.objects.get(lastName=self.__iLastName), second=None)
    
    def testInvestorBio(self):
        self.assertNotEqual(Investor.objects.get(bio=self.__iBio), second=None)
    
    def testPercCompleted(self):
        self.assertNotEqual(Investor.objects.get(percCompleted=self.__iPercCompleted), second=None)
    
    def testPic(self):
        self.assertNotEqual(Investor.objects.get(pic=self.__iPic), second=None)
    
    def testPortfolioValue(self):
        self.assertNotEqual(Investor.objects.get(portfolioValue=self.__iPortfolioValue), second=None)
    
    def testAccountValue(self):
        self.assertNotEqual(Investor.objects.get(accountValue=self.__iAccountValue), second=None)
    
    def testFollowers(self):
        self.assertNotEqual(Investor.objects.get(followers=self.__iFollowers), second=None)
    
    def testFollowing(self):
        self.assertNotEqual(Investor.objects.get(following=self.__iFollowing), second=None)
    
    def testSyndicates(self):
        self.assertNotEqual(Investor.objects.get(syndicates=self.__iSyndicates), second=None)
    
    def testStatusUpdate(self):
        self.assertNotEqual(Investor.objects.get(statusUpdate=self.__iStatusUpdate), second=None)
    
    def testPortfolioReturn(self):
        self.assertNotEqual(Investor.objects.get(portfolioReturn=self.__iPortfolioReturn), second=None)
    