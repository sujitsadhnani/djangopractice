from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from requests import session
from home import models
from django.core.mail import send_mail
import random
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    
    if request.method == 'GET':
        email = None
        is_doctor_verified = None
        is_site_admin = None
        email = request.session.get('email')
        is_doctor_verified = request.session.get('is_doctor_verified')
        is_site_admin = request.session.get('is_site_admin')


        try:
            top_med_posts = models.med_post.objects.order_by('-med_post_score')[0:5]
            med_posts_count = len(top_med_posts)
            all_med_posts_count = models.med_post.objects.all().count()

            med_post_1 = None
            med_post_2 = None
            med_post_3 = None
            med_post_4 = None
            med_post_5 = None

            if med_posts_count == 1:
                med_post_1 = top_med_posts[0]
            elif med_posts_count == 2:
                med_post_1 = top_med_posts[0]
                med_post_2 = top_med_posts[1]
            elif med_posts_count == 3:
                med_post_1 = top_med_posts[0]
                med_post_2 = top_med_posts[1]
                med_post_3 = top_med_posts[2]
            elif med_posts_count == 4:
                med_post_1 = top_med_posts[0]
                med_post_2 = top_med_posts[1]
                med_post_3 = top_med_posts[2]
                med_post_4 = top_med_posts[3]
            else:

                med_post_1 = top_med_posts[0]
                med_post_2 = top_med_posts[1]
                med_post_3 = top_med_posts[2]
                med_post_4 = top_med_posts[3]
                med_post_5 = top_med_posts[4]

            try:
                med_post_1_datetime = med_post_1.med_post_datetime
                med_post_1_user = str(med_post_1.user.first_name)+' '+str(med_post_1.user.middle_name)+' '+str(med_post_1.user.sur_name)
                med_post_1_text = med_post_1.med_post_text
                med_post_1_likes = med_post_1.med_post_likes
                med_post_1_doc_likes = med_post_1.med_post_doc_likes
                med_post_1_id = med_post_1.med_post_id
            except:
                med_post_1_datetime = None
                med_post_1_user = None
                med_post_1_text = None
                med_post_1_likes = None
                med_post_1_doc_likes = None
                med_post_1_id = None

            try:            
                med_post_2_datetime = med_post_2.med_post_datetime
                med_post_2_user = str(med_post_2.user.first_name)+' '+str(med_post_2.user.middle_name)+' '+str(med_post_2.user.sur_name)
                med_post_2_text = med_post_2.med_post_text
                med_post_2_likes = med_post_2.med_post_likes
                med_post_2_doc_likes = med_post_2.med_post_doc_likes
                med_post_2_id = med_post_2.med_post_id

            except:
                med_post_2_datetime = None
                med_post_2_user = None
                med_post_2_text = None
                med_post_2_likes = None
                med_post_2_doc_likes = None
                med_post_2_id = None


            try:
                med_post_3_datetime = med_post_3.med_post_datetime
                med_post_3_user = str(med_post_3.user.first_name)+' '+str(med_post_3.user.middle_name)+' '+str(med_post_3.user.sur_name)
                med_post_3_text = med_post_3.med_post_text
                med_post_3_likes = med_post_3.med_post_likes
                med_post_3_doc_likes = med_post_3.med_post_doc_likes
                med_post_3_id = med_post_3.med_post_id
            
            except:
                med_post_3_datetime = None
                med_post_3_user = None
                med_post_3_text = None
                med_post_3_likes = None
                med_post_3_doc_likes = None
                med_post_1_id = None

            try:
                med_post_4_datetime = med_post_4.med_post_datetime
                med_post_4_user = str(med_post_4.user.first_name)+' '+str(med_post_4.user.middle_name)+' '+str(med_post_4.user.sur_name)
                med_post_4_text = med_post_4.med_post_text
                med_post_4_likes = med_post_4.med_post_likes
                med_post_4_doc_likes = med_post_4.med_post_doc_likes
                med_post_4_id = med_post_4.med_post_id

            except:
                med_post_4_datetime = None
                med_post_4_user = None
                med_post_4_text = None
                med_post_4_likes = None
                med_post_4_doc_likes = None
                med_post_4_id = None

            try:
                med_post_5_datetime = med_post_5.med_post_datetime
                med_post_5_user = str(med_post_5.user.first_name)+' '+str(med_post_5.user.middle_name)+' '+str(med_post_5.user.sur_name)
                med_post_5_text = med_post_5.med_post_text
                med_post_5_likes = med_post_5.med_post_likes
                med_post_5_doc_likes = med_post_5.med_post_doc_likes
                med_post_5_id = med_post_5.med_post_id

            except:
                med_post_5_datetime = None
                med_post_5_user = None
                med_post_5_text = None
                med_post_5_likes = None
                med_post_5_doc_likes = None
                med_post_5_id = None


            return render(request, 'home.html', {'email' : email, 'is_doctor_verified' : is_doctor_verified, 'is_site_admin' : is_site_admin,   'med_post_1_datetime' : med_post_1_datetime , 'med_post_1_doc_likes' : med_post_1_doc_likes , 'med_post_1_likes' : med_post_1_likes , 'med_post_1_text' : med_post_1_text , 'med_post_1_user' : med_post_1_user , 'med_post_2_datetime' : med_post_2_datetime , 'med_post_2_doc_likes' : med_post_2_doc_likes , 'med_post_2_likes' : med_post_2_likes , 'med_post_2_text' : med_post_2_text , 'med_post_2_user' : med_post_2_user , 'med_post_3_datetime' : med_post_3_datetime , 'med_post_3_doc_likes' : med_post_3_doc_likes , 'med_post_3_likes' : med_post_3_likes , 'med_post_3_text' : med_post_3_text , 'med_post_3_user' : med_post_3_user , 'med_post_4_datetime' : med_post_4_datetime , 'med_post_4_doc_likes' : med_post_4_doc_likes , 'med_post_4_likes' : med_post_4_likes , 'med_post_4_text' : med_post_4_text , 'med_post_4_user' : med_post_4_user , 'med_post_5_datetime' : med_post_5_datetime , 'med_post_5_doc_likes' : med_post_5_doc_likes , 'med_post_5_likes' : med_post_5_likes , 'med_post_5_text' : med_post_5_text , 'med_post_5_user' : med_post_5_user, 'med_post_1_id' : med_post_1_id, 'med_post_2_id' : med_post_2_id, 'med_post_3_id' : med_post_3_id, 'med_post_4_id' : med_post_4_id, 'med_post_5_id' : med_post_5_id , 'display_med_posts' : True,
            'med_posts_count' : all_med_posts_count, 'page_number' : 1, 'page_next': 2, 'page_prev' : None })

        except:
            return render(request, 'home.html', {'email' : email, 'is_doctor_verified' : is_doctor_verified, 'is_site_admin' : is_site_admin, 'display_med_posts' : False } )
    
    if request.method == 'POST':
        email = None
        is_doctor_verified = None
        is_site_admin = None
        email = request.session.get('email')
        is_doctor_verified = request.session.get('is_doctor_verified')
        is_site_admin = request.session.get('is_site_admin')
        page_number = int(request.POST['page_number'])
        if page_number > 1:
            page_prev = page_number - 1
        else:
            page_prev = None
        page_next = page_number + 1
        n = (page_number - 1)*5
        try:
            top_med_posts = models.med_post.objects.order_by('-med_post_score')[n:n+5]
            
            med_posts_count = len(top_med_posts)
            all_med_posts_count = models.med_post.objects.all().count()
            
            med_post_1 = None
            med_post_2 = None
            med_post_3 = None
            med_post_4 = None
            med_post_5 = None

            if med_posts_count == 1:
                med_post_1 = top_med_posts[0]
            elif med_posts_count == 2:
                med_post_1 = top_med_posts[0]
                med_post_2 = top_med_posts[1]
            elif med_posts_count == 3:
                med_post_1 = top_med_posts[0]
                med_post_2 = top_med_posts[1]
                med_post_3 = top_med_posts[2]
            elif med_posts_count == 4:
                med_post_1 = top_med_posts[0]
                med_post_2 = top_med_posts[1]
                med_post_3 = top_med_posts[2]
                med_post_4 = top_med_posts[3]
            else:

                med_post_1 = top_med_posts[0]
                med_post_2 = top_med_posts[1]
                med_post_3 = top_med_posts[2]
                med_post_4 = top_med_posts[3]
                med_post_5 = top_med_posts[4]
            
            try:
                med_post_1_datetime = med_post_1.med_post_datetime
                med_post_1_user = str(med_post_1.user.first_name)+' '+str(med_post_1.user.middle_name)+' '+str(med_post_1.user.sur_name)
                med_post_1_text = med_post_1.med_post_text
                med_post_1_likes = med_post_1.med_post_likes
                med_post_1_doc_likes = med_post_1.med_post_doc_likes
                med_post_1_id = med_post_1.med_post_id
            except:
                med_post_1_datetime = None
                med_post_1_user = None
                med_post_1_text = None
                med_post_1_likes = None
                med_post_1_doc_likes = None
                med_post_1_id = None

            try:            
                med_post_2_datetime = med_post_2.med_post_datetime
                med_post_2_user = str(med_post_2.user.first_name)+' '+str(med_post_2.user.middle_name)+' '+str(med_post_2.user.sur_name)
                med_post_2_text = med_post_2.med_post_text
                med_post_2_likes = med_post_2.med_post_likes
                med_post_2_doc_likes = med_post_2.med_post_doc_likes
                med_post_2_id = med_post_2.med_post_id

            except:
                med_post_2_datetime = None
                med_post_2_user = None
                med_post_2_text = None
                med_post_2_likes = None
                med_post_2_doc_likes = None
                med_post_2_id = None


            try:
                med_post_3_datetime = med_post_3.med_post_datetime
                med_post_3_user = str(med_post_3.user.first_name)+' '+str(med_post_3.user.middle_name)+' '+str(med_post_3.user.sur_name)
                med_post_3_text = med_post_3.med_post_text
                med_post_3_likes = med_post_3.med_post_likes
                med_post_3_doc_likes = med_post_3.med_post_doc_likes
                med_post_3_id = med_post_3.med_post_id
            
            except:
                med_post_3_datetime = None
                med_post_3_user = None
                med_post_3_text = None
                med_post_3_likes = None
                med_post_3_doc_likes = None
                med_post_3_id = None

            try:
                med_post_4_datetime = med_post_4.med_post_datetime
                med_post_4_user = str(med_post_4.user.first_name)+' '+str(med_post_4.user.middle_name)+' '+str(med_post_4.user.sur_name)
                med_post_4_text = med_post_4.med_post_text
                med_post_4_likes = med_post_4.med_post_likes
                med_post_4_doc_likes = med_post_4.med_post_doc_likes
                med_post_4_id = med_post_4.med_post_id

            except:
                med_post_4_datetime = None
                med_post_4_user = None
                med_post_4_text = None
                med_post_4_likes = None
                med_post_4_doc_likes = None
                med_post_4_id = med_post_4.med_post_id

            try:
                med_post_5_datetime = med_post_5.med_post_datetime
                med_post_5_user = str(med_post_5.user.first_name)+' '+str(med_post_5.user.middle_name)+' '+str(med_post_5.user.sur_name)
                med_post_5_text = med_post_5.med_post_text
                med_post_5_likes = med_post_5.med_post_likes
                med_post_5_doc_likes = med_post_5.med_post_doc_likes
                med_post_5_id = med_post_5.med_post_id

            except:
                med_post_5_datetime = None
                med_post_5_user = None
                med_post_5_text = None
                med_post_5_likes = None
                med_post_5_doc_likes = None
                med_post_5_id = med_post_5.med_post_id




            if all_med_posts_count <= page_number *5:
                page_next = None
                return render(request, 'home.html', {'email' : email, 'is_doctor_verified' : is_doctor_verified, 'is_site_admin' : is_site_admin,   'med_post_1_datetime' : med_post_1_datetime , 'med_post_1_doc_likes' : med_post_1_doc_likes , 'med_post_1_likes' : med_post_1_likes , 'med_post_1_text' : med_post_1_text , 'med_post_1_user' : med_post_1_user , 'med_post_2_datetime' : med_post_2_datetime , 'med_post_2_doc_likes' : med_post_2_doc_likes , 'med_post_2_likes' : med_post_2_likes , 'med_post_2_text' : med_post_2_text , 'med_post_2_user' : med_post_2_user , 'med_post_3_datetime' : med_post_3_datetime , 'med_post_3_doc_likes' : med_post_3_doc_likes , 'med_post_3_likes' : med_post_3_likes , 'med_post_3_text' : med_post_3_text , 'med_post_3_user' : med_post_3_user , 'med_post_4_datetime' : med_post_4_datetime , 'med_post_4_doc_likes' : med_post_4_doc_likes , 'med_post_4_likes' : med_post_4_likes , 'med_post_4_text' : med_post_4_text , 'med_post_4_user' : med_post_4_user , 'med_post_5_datetime' : med_post_5_datetime , 'med_post_5_doc_likes' : med_post_5_doc_likes , 'med_post_5_likes' : med_post_5_likes , 'med_post_5_text' : med_post_5_text , 'med_post_5_user' : med_post_5_user, 'med_post_1_id' : med_post_1_id, 'med_post_2_id' : med_post_2_id, 'med_post_3_id' : med_post_3_id, 'med_post_4_id' : med_post_4_id, 'med_post_5_id' : med_post_5_id , 'display_med_posts' : True, 'med_posts_count' : all_med_posts_count, 'page_number' : page_number, 'page_next': page_next , 'page_prev' : page_prev})
            else:
                page_next = page_number + 1
                
                return render(request, 'home.html', {'email' : email, 'is_doctor_verified' : is_doctor_verified, 'is_site_admin' : is_site_admin,    'med_post_1_datetime' : med_post_1_datetime , 'med_post_1_doc_likes' : med_post_1_doc_likes , 'med_post_1_likes' : med_post_1_likes , 'med_post_1_text' : med_post_1_text , 'med_post_1_user' : med_post_1_user ,  'med_post_2_datetime' : med_post_2_datetime , 'med_post_2_doc_likes' : med_post_2_doc_likes , 'med_post_2_likes' : med_post_2_likes , 'med_post_2_text' : med_post_2_text , 'med_post_2_user' : med_post_2_user , 'med_post_3_datetime' : med_post_3_datetime , 'med_post_3_doc_likes' : med_post_3_doc_likes , 'med_post_3_likes' : med_post_3_likes , 'med_post_3_text' : med_post_3_text , 'med_post_3_user' : med_post_3_user ,  'med_post_4_datetime' : med_post_4_datetime , 'med_post_4_doc_likes' : med_post_4_doc_likes , 'med_post_4_likes' : med_post_4_likes , 'med_post_4_text' : med_post_4_text , 'med_post_4_user' : med_post_4_user ,  'med_post_5_datetime' : med_post_5_datetime , 'med_post_5_doc_likes' : med_post_5_doc_likes , 'med_post_5_likes' : med_post_5_likes , 'med_post_5_text' : med_post_5_text , 'med_post_5_user' : med_post_5_user, 'med_post_1_id' : med_post_1_id, 'med_post_2_id' : med_post_2_id, 'med_post_3_id' : med_post_3_id, 'med_post_4_id' : med_post_4_id, 'med_post_5_id' : med_post_5_id , 'display_med_posts' : True, 'med_posts_count' : all_med_posts_count, 'page_number' : page_number, 'page_next': page_next , 'page_prev' : page_prev})

        except:
            return render(request, 'home.html', {'email' : email, 'is_doctor_verified' : is_doctor_verified, 'is_site_admin' : is_site_admin, 'display_med_posts' : False  } )

@csrf_exempt
def logout(request):
    request.session['email'] = None
    request.session['email_already'] = None
    request.session['error_message'] = None
    request.session['is_doctor_verified'] = None
    request.session['is_site_admin'] = None
    return redirect('home')

@csrf_exempt
def medposting(request):
    email = request.session.get('email')
    try:
        user = models.user.objects.get(email=email)
        if user.is_doctor_verified:
            if request.method == 'GET':
                return render(request, 'medposting.html')
            if request.method == 'POST':
                med_post_text = request.POST['med_post_text']
                new_med_post = models.med_post(user=user, med_post_text=med_post_text)
                new_med_post.save()
                return redirect('home')

        else:
            return redirect('home')
    except:
        return redirect('home')


@csrf_exempt
def signup(request):
    if request.method == 'GET':
        return render(request, 'sign_up.html')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        sur_name = request.POST['sur_name']
        date_of_birth = request.POST['date_of_birth']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        is_doctor = request.POST['is_doctor']
        medical_license = request.POST['medical_license']
        doc_speciality = request.POST['doc_speciality']
        password = request.POST['password']
        already_user = None

        try:
            already_user = models.user.objects.get(email=email)
        except:
            already_user = None

        if already_user:
            request.session['email_already'] = email
            return redirect('login')
        else :
            password = make_password(password)

            new_user = models.user(first_name=first_name, middle_name=middle_name, sur_name=sur_name, date_of_birth=date_of_birth, gender=gender, email=email, phone=phone, is_doctor=is_doctor, medical_license=medical_license, doc_speciality=doc_speciality, password=password)

            new_user.save()
            request.session['email'] = email
            request.session['email_already'] = None

            return redirect('home')

@csrf_exempt
def login(request):
    if request.method == 'GET':
        email_already = None
        email_already = request.session.get('email_already')
        return render(request, 'login.html', {'email_already' : email_already})

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = models.user.objects.get(email=email)
        except:
            user = None

        error_message = None
        if user:
            pass_check = check_password(password, user.password)
            if pass_check:
                request.session['email'] = user.email
                request.session['email_already'] = None
                if user.is_doctor_verified:
                    request.session['is_doctor_verified'] = user.is_doctor_verified
                if user.is_site_admin:
                    request.session['is_site_admin'] = user.is_site_admin

                return redirect('home')
            else:
                error_message = 'Password is invalid!'
                email_already = user.email
        else:
            error_message = 'Email is invalid!'

        return render(request, 'login.html', {'error_message': error_message, 'email_already' : email_already})

@csrf_exempt  
def forgot_pass(request):
    if request.method == 'GET':
        email_already = None
        email_already = request.session.get('email_already')
        error_message = None
        error_message = request.session.get('error_message')
        return render(request, 'forgot_pass.html', {'email_already' : email_already, 'error_message' : error_message})

    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = models.user.objects.get(email=email)
        except:
            user = None

        if user:    
            try:
                reset_otp = random.randint(100000,999999)
                mail_message = 'Please use the One Time Password(OTP) provided to reset the password. OTP:'+ str(reset_otp)
                send_mail( 'What does the Doc. say? password reset mail', mail_message, 'whatdoesthedocsayproject@gmail.com', [email], fail_silently=False,)
                user.reset_otp = reset_otp
                user.save()
                request.session['email_already'] = email
                return redirect('reset_pass')

            except:
                error_message = 'we are having some difficulty sending the email'
                request.session['error_message'] = error_message
                return redirect('forgot_pass')

        else:
            error_message = 'no user found for the provided email address, please provide a different email address or consider signing up'
            request.session['error_message'] = error_message
            return redirect('forgot_pass')

@csrf_exempt
def reset_pass(request):
    if request.method == 'GET':
        email_already = None
        email_already = request.session.get('email_already')
        error_message = None
        error_message = request.session.get('error_message')
        return render(request, 'reset_pass.html', {'email_already' : email_already, 'error_message' : error_message})

    if request.method == 'POST':
        email = request.POST['email']
        reset_otp_input = request.POST['reset_otp']
        password = request.POST['password']
        if reset_otp_input == 0:
            error_message = 'Incorrect OTP'
            request.session['error_message'] = error_message
            request.session['email_already'] = email
            return redirect('reset_pass')

        try:
            user = models.user.objects.get(email=email)
        except:
            user = None
        if user:
            print(user.reset_otp)
            print(reset_otp_input)
            if reset_otp_input == str(user.reset_otp):
                password = make_password(password)
                user.password = password
                user.save()
                request.session['email'] = user.email
                return redirect('home')

            else:
                error_message = 'Incorrect OTP'
                request.session['error_message'] = error_message
                request.session['email_already'] = email
                return redirect('reset_pass')

        else:
            error_message = 'no user found for the provided email address, please provide a different email address or consider signing up'
            request.session['error_message'] = error_message
            request.session['email_already'] = email
            return redirect('reset_pass')

@csrf_exempt
def like(request):
    if request.method == 'POST':
        email = request.POST['email']
        med_post_like_id = int(request.POST['med_post_like_id'])

        try:
            user = models.user.objects.get(email=email)
            med_post_liked = models.med_post.objects.get(med_post_id = med_post_like_id)
            new_like = models.like(med_post=med_post_liked, user=user)
            new_like.save()
            if user.is_doctor_verified:
                med_post_liked.med_post_doc_likes = med_post_liked.med_post_doc_likes +1
                med_post_liked.med_post_score = med_post_liked.med_post_score +10
                doc_score_increase =10
            else:
                med_post_liked.med_post_likes = med_post_liked.med_post_likes +1
                med_post_liked.med_post_score = med_post_liked.med_post_score +1
                doc_score_increase =1

            med_post_liked.save()
            poster = med_post_liked.user
            poster.doc_score = poster.doc_score + doc_score_increase
            poster.save()
            return redirect('home')

        except:
            return redirect('home')


@csrf_exempt        
def best_docs(request):    
    if request.method == 'GET':
        try:    
            top_docs = models.user.objects.filter(is_doctor_verified = True).order_by('-doc_score')[:10]
            top_docs_length = len(top_docs)
            

            top_doc_1 = None
            top_doc_2 = None
            top_doc_3 = None
            top_doc_4 = None
            top_doc_5 = None
            top_doc_6 = None
            top_doc_7 = None
            top_doc_8 = None
            top_doc_9 = None
            top_doc_10 = None

            if top_docs_length == 0:
                return HttpResponse('Sorry, no doctors were found')
            elif top_docs_length == 1:
                top_doc_1 = top_docs[0]
            elif top_docs_length == 2:
                top_doc_1 = top_docs[0]
                top_doc_2 = top_docs[1]

            elif top_docs_length == 3:
                top_doc_1 = top_docs[0]
                top_doc_2 = top_docs[1]
                top_doc_3 = top_docs[2]

            elif top_docs_length == 4:
                top_doc_1 = top_docs[0]
                top_doc_2 = top_docs[1]
                top_doc_3 = top_docs[2]
                top_doc_4 = top_docs[3]

            elif top_docs_length == 5:
                top_doc_1 = top_docs[0]
                top_doc_2 = top_docs[1]
                top_doc_3 = top_docs[2]
                top_doc_4 = top_docs[3]
                top_doc_5 = top_docs[4]

            elif top_docs_length == 6:
                top_doc_1 = top_docs[0]
                top_doc_2 = top_docs[1]
                top_doc_3 = top_docs[2]
                top_doc_4 = top_docs[3]
                top_doc_5 = top_docs[4]
                top_doc_6 = top_docs[5]

            elif top_docs_length == 7:
                top_doc_1 = top_docs[0]
                top_doc_2 = top_docs[1]
                top_doc_3 = top_docs[2]
                top_doc_4 = top_docs[3]
                top_doc_5 = top_docs[4]
                top_doc_6 = top_docs[5]
                top_doc_7 = top_docs[6]

            elif top_docs_length == 8:
                top_doc_1 = top_docs[0]
                top_doc_2 = top_docs[1]
                top_doc_3 = top_docs[2]
                top_doc_4 = top_docs[3]
                top_doc_5 = top_docs[4]
                top_doc_6 = top_docs[5]
                top_doc_7 = top_docs[6]
                top_doc_8 = top_docs[7]

            elif top_docs_length == 9:
                top_doc_1 = top_docs[0]
                top_doc_2 = top_docs[1]
                top_doc_3 = top_docs[2]
                top_doc_4 = top_docs[3]
                top_doc_5 = top_docs[4]
                top_doc_6 = top_docs[5]
                top_doc_7 = top_docs[6]
                top_doc_8 = top_docs[7]
                top_doc_9 = top_docs[8]

            else:
                top_doc_1 = top_docs[0]
                top_doc_2 = top_docs[1]
                top_doc_3 = top_docs[2]
                top_doc_4 = top_docs[3]
                top_doc_5 = top_docs[4]
                top_doc_6 = top_docs[5]
                top_doc_7 = top_docs[6]
                top_doc_8 = top_docs[7]
                top_doc_9 = top_docs[8]
                top_doc_10 = top_docs[9]

            try:
                top_doc_1_name = str(top_doc_1.first_name)+' '+str(top_doc_1.middle_name)+' '+str(top_doc_1.sur_name)
                top_doc_1_speciality = top_doc_1.doc_speciality
                top_doc_1_email = top_doc_1.email
                top_doc_1_phone = top_doc_1.phone
            except:
                top_doc_1_name = None
                top_doc_1_speciality = None
                top_doc_1_email = None
                top_doc_1_phone = None
                

            try:
                top_doc_2_name = str(top_doc_2.first_name)+' '+str(top_doc_2.middle_name)+' '+str(top_doc_2.sur_name)
                top_doc_2_speciality = top_doc_2.doc_speciality
                top_doc_2_email = top_doc_2.email
                top_doc_2_phone = top_doc_2.phone
            except:
                top_doc_2_name = None
                top_doc_2_speciality = None
                top_doc_2_email = None
                top_doc_2_phone = None

            try:
                top_doc_3_name = str(top_doc_3.first_name)+' '+str(top_doc_3.middle_name)+' '+str(top_doc_3.sur_name)
                top_doc_3_speciality = top_doc_3.doc_speciality
                top_doc_3_email = top_doc_3.email
                top_doc_3_phone = top_doc_3.phone

            except:
                top_doc_3_name = None
                top_doc_3_speciality = None
                top_doc_3_email = None
                top_doc_3_phone = None

            try:
                top_doc_4_name = str(top_doc_4.first_name)+' '+str(top_doc_4.middle_name)+' '+str(top_doc_4.sur_name)
                top_doc_4_speciality = top_doc_4.doc_speciality
                top_doc_4_email = top_doc_4.email
                top_doc_4_phone = top_doc_4.phone
            except:
                top_doc_4_name = None
                top_doc_4_speciality = None
                top_doc_4_email = None
                top_doc_4_phone = None

            try:
                top_doc_5_name = str(top_doc_5.first_name)+' '+str(top_doc_5.middle_name)+' '+str(top_doc_5.sur_name)
                top_doc_5_speciality = top_doc_5.doc_speciality
                top_doc_5_email = top_doc_5.email
                top_doc_5_phone = top_doc_5.phone

            except:
                top_doc_5_name = None
                top_doc_5_speciality = None
                top_doc_5_email = None
                top_doc_5_phone = None

            try:
                top_doc_6_name = str(top_doc_6.first_name)+' '+str(top_doc_6.middle_name)+' '+str(top_doc_6.sur_name)
                top_doc_6_speciality = top_doc_6.doc_speciality
                top_doc_6_email = top_doc_6.email
                top_doc_6_phone = top_doc_6.phone
            except:
                top_doc_6_name = None
                top_doc_6_speciality = None
                top_doc_6_email = None
                top_doc_6_phone = None

            try:
                top_doc_7_name = str(top_doc_7.first_name)+' '+str(top_doc_7.middle_name)+' '+str(top_doc_7.sur_name)
                top_doc_7_speciality = top_doc_7.doc_speciality
                top_doc_7_email = top_doc_7.email
                top_doc_7_phone = top_doc_7.phone

            except:
                top_doc_7_name = None
                top_doc_7_speciality = None
                top_doc_7_email = None
                top_doc_7_phone = None

            try:
                top_doc_8_name = str(top_doc_8.first_name)+' '+str(top_doc_8.middle_name)+' '+str(top_doc_8.sur_name)
                top_doc_8_speciality = top_doc_8.doc_speciality
                top_doc_8_email = top_doc_8.email
                top_doc_8_phone = top_doc_8.phone

            except:
                top_doc_8_name = None
                top_doc_8_speciality = None
                top_doc_8_email = None
                top_doc_8_phone = None

            try:
                top_doc_9_name = str(top_doc_9.first_name)+' '+str(top_doc_9.middle_name)+' '+str(top_doc_9.sur_name)
                top_doc_9_speciality = top_doc_9.doc_speciality
                top_doc_9_email = top_doc_9.email
                top_doc_9_phone = top_doc_9.phone

            except:
                top_doc_9_name = None
                top_doc_9_speciality = None
                top_doc_9_email = None
                top_doc_9_phone = None

            try:
                top_doc_10_name = str(top_doc_10.first_name)+' '+str(top_doc_10.middle_name)+' '+str(top_doc_10.sur_name)
                top_doc_10_speciality = top_doc_10.doc_speciality
                top_doc_10_email = top_doc_10.email
                top_doc_10_phone = top_doc_10.phone
            except:
                top_doc_10_name = None
                top_doc_10_speciality = None
                top_doc_10_email = None
                top_doc_10_phone = None

            return render(request, 'best_docs.html', {'top_doc_1_name' : top_doc_1_name,'top_doc_2_name' : top_doc_2_name,'top_doc_3_name' : top_doc_3_name,'top_doc_4_name' : top_doc_4_name,'top_doc_5_name' : top_doc_5_name,'top_doc_6_name' :top_doc_6_name ,'top_doc_7_name' : top_doc_7_name,'top_doc_8_name' :top_doc_8_name ,'top_doc_9_name' :top_doc_9_name ,'top_doc_10_name' : top_doc_10_name,'top_doc_1_speciality' : top_doc_1_speciality,'top_doc_2_speciality' : top_doc_2_speciality,'top_doc_3_speciality' : top_doc_3_speciality,'top_doc_4_speciality' : top_doc_4_speciality,'top_doc_5_speciality' : top_doc_5_speciality,'top_doc_6_speciality' :top_doc_6_speciality ,'top_doc_7_speciality' :top_doc_7_speciality ,'top_doc_8_speciality' :top_doc_8_speciality ,'top_doc_9_speciality' :top_doc_9_speciality ,'top_doc_10_speciality' :top_doc_10_speciality ,'top_doc_1_email' :top_doc_1_email ,'top_doc_2_email' :top_doc_2_email ,'top_doc_3_email' :top_doc_3_email ,'top_doc_4_email' :top_doc_4_email ,'top_doc_5_email' :top_doc_5_email ,'top_doc_6_email' :top_doc_6_email ,'top_doc_7_email' :top_doc_7_email ,'top_doc_8_email' :top_doc_8_email ,'top_doc_9_email' :top_doc_9_email ,'top_doc_10_email' :top_doc_10_email ,'top_doc_1_phone' :top_doc_1_phone ,'top_doc_2_phone' :top_doc_2_phone ,'top_doc_3_phone' : top_doc_3_phone,'top_doc_4_phone' :top_doc_4_phone ,'top_doc_5_phone' :top_doc_5_phone ,'top_doc_6_phone' :top_doc_6_phone ,'top_doc_7_phone' : top_doc_7_phone ,'top_doc_8_phone' :top_doc_8_phone ,'top_doc_9_phone' :top_doc_9_phone ,'top_doc_10_phone' :top_doc_10_phone })

        except:
            return render(request, 'best_docs.html')










