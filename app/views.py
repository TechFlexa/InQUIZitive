from django.shortcuts import render, redirect , render_to_response
from django.conf import settings
import urllib,urllib2,json
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib import messages
import hashlib
import requests
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import DeleteView
from .forms import UserForm
from .models import UserProfile,Topic,Subtopic,Question,Answer,Quiz,Quiz_Question,Attempt

def homepage(request):
	return render(request,'app/homepage.html')

def signup(request):
    context=RequestContext(request)
    registered=False
    if request.method=='POST':         
        form=UserForm(data=request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=form.save()
            user.set_password(user.password)
            user.save()
            # ob=UserProfile.objects.create(user_id=request.user.id)
            # ob.save()
            # authkey = "210112APJgCTharC5ad321b5" # Your authentication key.

            # mobiles = "9340114842" # Multiple mobiles numbers separated by comma.

            # message = "Test message" # Your message to send.

            # sender = "112233" # Sender ID,While using route4 sender id should be 6 characters long.

            # route = "default" # Define route

            # # Prepare you post parameters
            # values = {
            #           'authkey' : authkey,
            #           'mobiles' : mobiles,
            #           'message' : message,
            #           'sender' : sender,
            #           'route' : route
            #           }


            # url = "http://api.msg91.com/api/sendhttp.php" # API URL

            # postdata = urllib.urlencode(values) # URL encoding the data here.

            # req = urllib2.Request(url, postdata)

            # response = urllib2.urlopen(req)

            # output = response.read() # Get Response

            # print output # Print Response


            registered=True
            return redirect('/app/')
            print "clear"   
        else:
            print form.errors
    else:
        form=UserForm()

    return render_to_response('app/signup.html',{'form':form,'registered':registered},context)

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print password
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                response=False
                login(request,user)
                return HttpResponseRedirect('/app/profile/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            response=True
            return render(request,'app/login.html',{'response':response})
           
    else:
        return render_to_response('app/login.html', {}, context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/app/login/')

def profile(request):
    args={'user':request.user}
    return render(request,'app/profile.html',args)


from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StockSerializer1,StockSerializer2,StockSerializer3,StockSerializer4,StockSerializer5,StockSerializer6,StockSerializer7,StockSerializer8,StockSerializer9

 
class Users_List(APIView):

      def get(self,request):
          stocks = User.objects.all()
          serializer=StockSerializer1(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass


class UserProfile_List(APIView):

      def get(self,request):
          stocks = UserProfile.objects.all()
          serializer=StockSerializer2(stocks,many=True)
          return Response(serializer.data)


      def post(self):
          pass

class Topic_List(APIView):

      def get(self,request):
          stocks = Topic.objects.all()
          serializer=StockSerializer3(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass

class Subtopic_List(APIView):

      def get(self,request):
          stocks = Subtopic.objects.all()
          serializer=StockSerializer4(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass

class Question_List(APIView):

      def get(self,request):
          stocks = Question.objects.all()
          serializer=StockSerializer5(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass


class Answer_List(APIView):

      def get(self,request):
          stocks = Answer.objects.all()
          serializer=StockSerializer6(stocks,many=True)
          return Response(serializer.data)


      def post(self):
          pass

class Attempt_List(APIView):

      def get(self,request):
          stocks = Attempt.objects.all()
          serializer=StockSerializer7(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass

class Quiz_List(APIView):

      def get(self,request):
          stocks = Quiz.objects.all()
          serializer=StockSerializer8(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass

class Quiz_Question_List(APIView):

      def get(self,request):
          stocks = Quiz_Question.objects.all()
          serializer=StockSerializer9(stocks,many=True)
          return Response(serializer.data)

      def post(self):
          pass