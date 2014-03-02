from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
# Create your views here.


def loginInvestor(request):
    #if request.method == 'POST':
    
    
    username = request.POST['username']
    password = request.POST['password']
    print "username" + username
    print "password" + password
    user = authenticate(username=username, password=password)
    print user
    data = request.POST
    print data
    if user is not None:
        if user.is_active:
            login(request, user)
            print "Authenticated User" +username
            return HttpResponseRedirect('/profiles/'+username)
        else:
            return HttpResponseRedirect('/landing/')
    #print data['email']
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return HttpResponseRedirect('/landing/')
    #return render_to_response('slicedinvesting/landing/base.html', context_dict, context)



    