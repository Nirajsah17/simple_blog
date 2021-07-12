from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import blog
from .forms import postform
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	post = blog.objects.all()
	context = {'post':post}
	return render(request,'user/index.html',context)
def signup(request):
	if request.method=='POST':
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST['email']
		pass1 = request.POST['password1']
		pass2 = request.POST['password2']
		# validation
		if len(fname) and len(lname) <3:
			msg = "First name or Last name should be greater than 3 character"
			return render(request,'user/Signup.html',{'msg':msg})
		if pass1 != pass2 :
			msg = 'Both passwordd should be same!'
			return render(request,'user/Signup.html',{'msg':msg})
		# usercreation
		myuser = User.objects.create_user(email,email,pass1)
		myuser.first_name = fname
		myuser.last_name = lname
		myuser.save()
		return redirect('login')
		#messages.success(request,"sucessfully created your accounts ")
	else:
		return render(request,'user/Signup.html')
def handlelogin(request):
	if request.method =='POST':
		uemail = request.POST['uemail']
		upassword = request.POST['upassword']
		user = authenticate(username=uemail,password=upassword)
		if user is not None :
			login(request,user)
			return redirect('index')
		else:
			msg = 'Invalid credential '
			return render(request,'user/login.html',{'msg':msg})
	return render(request,'user/login.html')
@login_required
def handlelogout(request):
	a = logout(request)
	msg = ' sucessfully logged out '
	return render(request,'user/index.html',{"msg":msg})
@login_required
def handlepost (request):
	form = postform(request.POST or None or request.FILES)
	if request.method =="POST":
		if form.is_valid():
			form = form.save(commit=False)
			form.users =request.user
			form.save()
			return redirect('index')
	return render(request,'user/post_create.html',{'form':form})