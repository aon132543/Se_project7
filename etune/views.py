from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import * 
from .models import *
import datetime
import math
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from datetime import date

# Create your views here.

def index(request):         #หน้าข่าวประชาสัมพันธ์หน้าแรกก่อนเข้า login 
    file_my = None   
    news = Scholar_news.objects.all()
    return render(request, 'index/index2.html',{'files':file_my,'news':news})

def login(request):
    file_my = None
    if request.user.is_authenticated:
        file_my = MyModel.objects.filter(upload_by=request.user.id)
        
    news = Scholar_news.objects.all()
    return render(request, 'index/login.html',{'files':file_my,'news':news})
    



def test2(request):
    return render(request,'t.html',{'test':'<h2>HELLOWORLD</h2><br><h6>this is h 6 </h6>'})

def log_user_out(request):
    logout(request)
    return redirect('/')

@login_required (login_url='index')
def home(request):                  #หน้าหลังจาก login ของทุกคน
    news = Scholar_info.objects.all()
    if request.user.is_staff == False:
        obj2 = add_commit.objects.filter(ac_email=request.user.email).exists() 
        if obj2 == True:
            obj2 = add_commit.objects.filter(ac_email=request.user.email)
            if obj2 != None:
                user_obj = User.objects.filter(email=request.user.email)
                obj2=obj2[0]
                for i in user_obj:
                    i.is_staff = True
                    i.first_name = obj2.ac_firstname
                    i.last_name = obj2.ac_lastname
                    i.save()
                messages.success(request, 'สวัสดีคุณ'+ str(obj2.ac_firstname)+ 'เข้าสู่ระบบ โดยเป็นคณะกรรมการ')
                return redirect('home')
                
                
        
    return render(request,'home-std.html',{'scholars': news})
    
@login_required (login_url='index')
def information(request):           #หน้าสร้างข่าวประชาสัมพันธ์ของ admin
    if request.method == 'POST':  
        head_news = request.POST['head_news']
        detail_news = request.POST['detail_news']
        date_news = request.POST['date_news']

        img = None
        file_to = None
        if request.FILES.get('images_news'):
            img =  request.FILES.get('images_news')
        if request.FILES.get('file_news'):
            file_to = request.FILES.get('file_news')

        
        data = Scholar_news.objects.create(
        sn_header = head_news,
        sn_description = detail_news,
        sn_expire_date = date_news,
        sn_photo_bg = img,
        sn_path_to_pdf = file_to
        )
        data.save()
        messages.success(request, 'สร้างประชาสัมพันธ์แล้ว')
        return render(request,'Create_Admin/information.html')
    return render(request,'Create_Admin/information.html')

def viewpost(request,id_post):              #หน้าดูรายละเอียดเพิ่มเติมของหน้า index
    news = Scholar_news.objects.filter(id=id_post)
    return render(request,'index/view-post.html',{'news':news})

@login_required (login_url='index')
def CreateScholar (request):                #หน้าสร้างประกาศรับทุน admin
    if request.method == 'POST':
        name_scholar = request.POST['name_scholar']
        detail = request.POST['detail']
        amount = request.POST['amount']
        amount_per_person = request.POST['amount_per_person']
        total = math.floor(int(amount)/int(amount_per_person))
        date_e = request.POST['date_news']
        option = request.POST['option']
        namelst = request.POST.getlist('text[]')
        type_scholar=request.POST['type_scholar']
        news = request.POST.get('news',None)  
        keys =[]
        
        for i in range(len(namelst)):
            keys.append(str("ผู้สนับสนุนทุนท่าที่ ")+str(i+1))

        file_to = None
        img =None
        if request.FILES.get('img'):
            img =  request.FILES.get('img')
        if request.FILES.get('file_t'):
            file_to = request.FILES.get('file_t')

        res = {}
        for key in keys:
            for value in namelst:
                res[key] = value
                namelst.remove(value)
                break
        data = Scholar_info.objects.create(
            si_name =name_scholar,
            si_description = detail,
            si_total_amount = amount,
            si_individual_amount =amount_per_person,
            si_max_scholar = total,
            si_remain_scholar = total,
            si_source =type_scholar,
            si_source_name =res,
            si_photo_bg =  img,
            si_path_to_pdf= file_to,
            si_note =option,
            si_expire_time =date_e,
            si_year = datetime.date.today().year,
            si_semester = 2
        ) 
        data.save()


        if news == "1" :
            data = Scholar_news.objects.create(
            sn_header = name_scholar,
            sn_description = detail,
            sn_expire_date = date_e,
            sn_photo_bg = img,
            sn_path_to_pdf = file_to
            )
            data.save()
            messages.success(request, "เพิ่มในข่าวหน้าประชาสัมพัมธ์เรียบร้อยแล้ว")
        messages.success(request, "สร้างทุนเรียบร้อยแล้ว")
        return redirect('home')

    return render(request,'Create_Admin/CreateScholar.html')
    
@login_required (login_url='index')
def editScholar(request,order_id):
    if request.method == 'POST':
        name_scholar_text = request.POST['name_scholar']
        detail = request.POST['detail']
        amount = request.POST['amount']
        amount_per_person = request.POST['amount_per_person']
        total = math.floor(int(amount)/int(amount_per_person))
        date_e = request.POST['date_news']
        option = request.POST['option']
        namelst = request.POST.getlist('text[]')
        type_scholar=request.POST['type_scholar']
        news = request.POST.get('news',None)  
        keys =[]
        
        for i in range(len(namelst)):
            keys.append(str("ผู้สนับสนุนทุนท่าที่ ")+str(i+1))

        

        res = {}
        for key in keys:
            for value in namelst:
                res[key] = value
                namelst.remove(value)
                break


        name_scholar = Scholar_info.objects.filter(id=order_id)
        name_scholar = name_scholar[0]
        bool_name_news = Scholar_news.objects.filter(sn_header=name_scholar).exists()

        data = Scholar_info.objects.filter(id=order_id).update(
            si_name =name_scholar_text,
            si_description = detail,
            si_total_amount = amount,
            si_individual_amount =amount_per_person,
            si_max_scholar = total,
            si_remain_scholar = total,
            si_source =type_scholar,
            si_source_name =res,
            si_note =option,
            si_expire_time =date_e,
            si_year = datetime.date.today().year,
            si_semester = 2
        )

        if request.FILES.get('img') != None :
            img =  request.FILES.get('img')
            img_name = request.FILES.get('img').name
            fs = FileSystemStorage(location='static/images/uploads')
            files = fs.save(img.name,img)
            fileurl = fs.path(files)
            Scholar_info.objects.filter(id=order_id).update(si_photo_bg= fileurl)
            
        if request.FILES.get('file_t'):
            pdf= request.FILES.get('file_t')
            fs2 = FileSystemStorage()
            files = fs2.save(pdf.name,pdf)
            fileurl = fs2.path(files)
            
        if bool_name_news :
            data = Scholar_news.objects.filter(sn_header=name_scholar).update(
            sn_header = name_scholar,
            sn_description = detail,
            sn_expire_date = date_e,
            sn_photo_bg = img,
            sn_path_to_pdf = file_to
            )
            messages.success(request, "แก้ไขข่าวหน้าประชาสัมพัมธ์เรียบร้อยแล้ว")
        messages.success(request, "แก้ไขทุนเรียบร้อยแล้ว")
        return redirect('home')
    scholar_info = Scholar_info.objects.filter(id=order_id)  
    scholar_info = scholar_info[0]
    json = scholar_info.si_source_name
    return render(request,'Create_Admin/editScholar.html',{'scholar_info':scholar_info,'json':json})

    



def InformationHome(request):  
    news = Scholar_news.objects.all()
    return render(request,'informationNews_Admin/informationhome.html',{'info':news})

def viewInfomation(request,order_id):       #หน้าดูข่าวสารของ admin
    news = Scholar_news.objects.filter(id=order_id)
    return render(request,'informationNews_Admin/view-Infomation.html',{'news': news})

def editInfomation(request,edit_id):       #หน้าแก้ไขข่าวประชาสัมพันธ์ของ admin
    if request.method == 'POST':  
        
        head_news = request.POST['head_news']
        detail_news = request.POST['detail_news']
        date_news = request.POST['date_news']
        news_obj = Scholar_news.objects.filter(id=edit_id).update(
            sn_header = head_news,
            sn_description = detail_news,
            sn_expire_date = date_news,
        )
        if request.FILES.get('images_news') != None:
            img = request.FILES.get('images_news')
            img_name = request.FILES.get('images_news').name

            fs = FileSystemStorage(location='static/images/uploads')
            files  = fs.save(img.name,img)

            fileurl = fs.path(files)
           
            Scholar_news.objects.filter(id=edit_id).update(sn_photo_bg =  fileurl )

        if request.FILES.get('file_news') != None:
            pdf = request.FILES.get('file_news')
            
            fs2 = FileSystemStorage()
            files  = fs2.save(pdf.name,pdf)

            fileurl = fs2.path(files)
            

            Scholar_news.objects.filter(id=edit_id).update(sn_path_to_pdf =fileurl)
        return redirect('InformationHome')
        
    news = Scholar_news.objects.filter(id=edit_id)
    return render(request,'Create_Admin/editinformation.html',{'news': news})

def addEditInfomation(request):
    redirect('InformationHome')

def viewHome(request,home_id):
    scholar = Scholar_info.objects.filter(id=home_id)
    datajson  = Scholar_info.objects.get(id=home_id)
    datajson = datajson.si_source_name
    
    return render(request,'view-home.html',{'scholars': scholar,'datajson':datajson})

def manageCommitteeHome(request):   #หน้าแสดงรายชื่อคณะกรรมการทั้งหมด
    news = User.objects.filter(is_staff=True) #ดึงฐานdatabase
    return render(request,'manageCommittee_Admin/manageCommitteeHome.html',{'scholars':news})

def delmanageCommitteeHome(request,user_id):
    user_obj = User.objects.get(id=user_id)
    user_obj.delete()
    messages.success(request, "ลบบัญชี Admin แล้ว")
    news = User.objects.filter(is_staff=True) #ดึงฐานdatabase
    return redirect('manageCommitteeHome')

def viewManageCommitteeHome(request,home_id): #หน้ารายชื่อทุนที่คณะกรรมการท่านนั้นทำการสอบสัมภาษณ์
    scholar = Scholar_info.objects.all()
    users = User.objects.filter(id=home_id)
    return render(request,'manageCommittee_Admin/view-manageCommitteeHome.html',{'scholars': scholar ,'users':users})

def addCommittee(request):
    if request.method == 'POST':
        firstname = request.POST['firstName']
        lastname = request.POST['lastName']
        email = request.POST['email']
        print(firstname,lastname,email)

        #สิ่งที่ต้องแก้ คือ email ยังไม่รู้ว่าจะเช็คยังไงว่าเขาเป็นกรรมการไหม
        news_obj = add_commit.objects.create(
            ac_email = email,
            ac_firstname = firstname,
            ac_lastname = lastname,
        )
        news_obj.save()
        messages.success(request, "เพิ่มบัญชีกรรมการแล้ว")
    return render(request,'manageCommittee_Admin/addCommittee.html')
    
def viewScore(request):
    infoes = Scholar_info.objects.all() #ดึงฐานdatabase
    return render(request,'score/scholar_score.html',{'infoes':infoes}) 

def viewWightScore(request,id_info):
    info = Scholar_info.objects.filter(id=id_info)
    info2 = info[0]
    info2 = info2.id

    json = Scholar_weight_score.objects.filter(id=id_info)
    json = json[0]
    json = json.sws_info
    if request.method == 'POST':
        name_lst = request.POST.getlist('name[]')
        weight_lst = request.POST.getlist('weight[]')
        res = {}
        for key in name_lst:
            for value in weight_lst:
                res[key] = value
                weight_lst.remove(value)
                break  
        now = timezone.now()
        data = Scholar_weight_score.objects.filter(id=id_info).update(
                sws_info = res,
                sws_date = now
        )
        infoes = Scholar_info.objects.all()
        return redirect('scholarScore')
    
    return render(request,'score/weight_score.html',{'info':info,'info2':info2,'json':json})

@login_required (login_url='index')
def profileHistoryNisit(request):
    user_obj = User.objects.filter(id=request.user.id)
    user_obj = user_obj[0]
    if Scholar_profile.objects.filter(sp_userid =user_obj).exists()==False:
        data = Scholar_profile.objects.create(sp_userid = user_obj )
        data.save()
        return render(request,'Form_Nisit/history_nisit.html') 


    if request.method == 'POST':
            #ของนิสิต
            advisor_professor = request.POST['advisor_professor'] ##อาจารย์ที่ปรึกษา
            title_thai = request.POST['title-thai']
            firstname_th = request.POST['firstname-th']
            middlename_th = request.POST['middlename-th']
            lastname_th = request.POST['lastname-th']
            std = request.POST['std']  
            title_eng = request.POST['title-eng']
            firstname_eng = request.POST['firstname-eng']
            middlename_eng = request.POST['middlename-eng']
            lastname_eng = request.POST['lastname-eng']
            ## email = request.POST['email']
            birthday = request.POST['birthday']
            if birthday == "":
                birthday = date.today()
            # pdf = request.POST['pdf']
            ## factor = request.POST['factor']
            major = request.POST['major']
            grade = request.POST['grade']
            address = request.POST['address']
            phone = request.POST['phone']
            
            #ของบิดา
            title_dad = request.POST['title-dadthai'] ##title_dad
            firstname_dad = request.POST['firstname-dad']
            middle_dad = request.POST['middlename-dad']
            lastname_dad = request.POST['lastname-dad']
            statuslife_dad = request.POST['statuslife-dad']
            address_dad = request.POST['address-dad']
            Tel_dad = request.POST['Tel-dad']
            birthday_dad =  request.POST['birthday-dad']
            if birthday_dad == "":
                birthday_dad = date.today()
            age_dad =  request.POST['age-dad']
            if age_dad=="":
                age_dad=0
            status_married_dad =  request.POST['status-married-dad']
            Income_dad =  request.POST['Income-dad']
            if Income_dad=="":
                Income_dad=0
            career_dad =  request.POST['career-dad']
            workplace_dad = request.POST['workplace-dad'] 
            
            # ของมารดา
            title_mom = request.POST['title-momthai'] ##title_mom
            firstname_mom = request.POST['firstname-mom']
            middle_mom = request.POST['middlename-mom']
            lastname_mom = request.POST['lastname-mom']
            statuslife_mom = request.POST['statuslife-mom']
            address_mom = request.POST['address-mom']
            Tel_mom = request.POST['Tel-mom']
            birthday_mom = request.POST['birthday-mom']
            if birthday_mom == "":
                birthday_mom = date.today()
            age_mom = request.POST['age-mom']
            if age_mom=="":
                age_mom=0
            status_married_mom = request.POST['status-married-mom']
            Income_mom = request.POST['Income-mom']
            if Income_mom=="":
                Income_mom=0
            career_mom = request.POST['career-mom']
            workplace_mom = request.POST['workplace-mom']

            #ของพี่น้อง
            title_sibling = request.POST['title-siblingthai']  ##title คำนำหน้า
            firstname_sibling = request.POST['firstname-sibling']
            middle_sibling = request.POST['middlename-sibling'] ##ชื่อกลาง
            lastname_sibling= request.POST['lastname-sibling']
            Tel_sibling = request.POST['Tel-sibling']
            birthday_sibling = request.POST['birthday-sibling']
            if birthday_sibling == "":
                birthday_sibling = date.today()
            age_sibling = request.POST['age-sibling']
            if age_sibling=="":
                age_sibling=0
            education_sibling = request.POST['education-sibling']
            career_sibling = request.POST['career-sibling']
            workplace_sibling = request.POST['workplace-sibling']
            
            #รายละเอียดราบได้ของผู้สมัครทุน
            moneyPerMonth = request.POST['moneyPerMonth']   #รายได้ต่อเดือน
            if moneyPerMonth=="":
                moneyPerMonth=0
            workplace_patron = request.POST['workplace-patron'] #ผู้ปกครองทำงานที่ไหน
            patron = request.POST['patron'] #ได้รับค่าใช้จ่ายจากใคร
            NumOfChild_patron = request.POST['NumOfChild-patron']   #ผู้ปกครองมีบุตรในอุปการะกี่คน
            if NumOfChild_patron=="":
                NumOfChild_patron=0
            studenloan = request.POST['studenloan'] #กู้ทุนมาไหม
            pastime = request.POST['pastime']   #เคยทำงานพิเศษไหม
            status_patron = request.POST['status-patron']   #ผู้ปกครองเกี่ยวข้องเป็นอะไร
            # #ไม่เอาแล้ว เอาเป็นเดือนไปเลยทีเดียว wages_pasttime = request.POST['wages-pasttime'] #นิสิตได้เงินต่อเดือนหรือสัปดาห์
            career_income = request.POST['career-income'] #รายได้จากงานนิสิต
            if career_income=="":
                career_income=0
            Type_address_pastime = request.POST['Type-pasttime']    #ประเภทงานที่ทำและสถานที่ที่นิสิตทำงานพาร์ททาม
            career = request.POST['career-patron']   #อาชีพของผู้ปกครอง
            Tel_patron = request.POST['Tel-patron'] #เบอร์มือถือของผู้ปกครอง
            
            #ทุนการศึกษาของนิสิต
            received_scholar = request.POST['received-scholar'] #ชื่อทุนที่เคยได้รับ
            received_year_scholar = request.POST['received-year-scholar']   #ปีที่ได้รับทุน
            prize = request.POST['prize']   #จำนวนเงินที่ได้รับ
            if prize=="":
                prize=0

            #รายละเอียดเพิ่มเติม
            # details = request.POST['details']   #เขียนรายละเอียดต่างๆ

            picture = request.FILES.get('resume')
            
            data = Scholar_profile.objects.filter(sp_userid= user_obj).update(
                #ของนิสิต
                sp_advisor_professor = advisor_professor,
                sp_status = 1,
                sp_title_en =title_eng, 
                sp_firstname_en = firstname_eng,
                sp_middlename_en = middlename_eng,
                sp_lastname_en = lastname_eng,
                sp_std_code	= std,
                sp_title_th	= title_thai,
                sp_firstname_th	= firstname_th,
                sp_middlename_th = middlename_th,
                sp_lastname_th = lastname_th,
                ## sp_path_to_avatar = 	
                sp_date_of_birth = birthday,	
                sp_major = major,
                sp_grade = grade,
                sp_path_to_pdf_json	= {"key": "value"}, ##json --> pdf,
                sp_std_address = {"address": "Saraburi"}, ##json --> address,
                sp_std_tel_no = phone,
                #ของบิดา
                sp_father_title = title_dad,
                sp_father_firstname	= firstname_dad,
                sp_father_middlename = middle_dad,
                sp_father_lastname = lastname_dad,
                sp_father_date_of_birth = birthday_dad,
                sp_father_age = age_dad,
                sp_father_status_married = status_married_dad,
                sp_father_statuslife = statuslife_dad,
                sp_father_income = Income_dad,
                sp_father_career = career_dad,
                sp_father_workplace = workplace_dad,
                sp_father_address = {"address": "Saraburi"}, ##json --> address_dad,
                sp_father_tel_no = Tel_dad,
                #ของมารดา
                sp_mother_title = title_mom,
                sp_mother_firstname	= firstname_mom,
                sp_mother_middlename = middle_mom,
                sp_mother_lastname = lastname_mom,
                sp_mother_date_of_birth = birthday_mom,
                sp_mother_age = age_mom,
                sp_mother_status_married = status_married_mom,
                sp_mother_statuslife = statuslife_mom,
                sp_mother_income = Income_mom,
                sp_mother_career = career_mom,
                sp_mother_workplace = workplace_mom,
                sp_mother_address = {"address": "Saraburi"}, ##json --> address_mom,
                sp_mother_tel_no = Tel_mom,
                #ของพี่น้อง
                sp_bro_n_sis = {"address": "Saraburi"}, ##json name,educate level,career,workplace
                #รายละเอียดราบได้ของผู้สมัครทุน
                sp_loan = studenloan,
                sp_income = moneyPerMonth,
                sp_income_source = patron,
                sp_patron_relation = status_patron,
                sp_patron_career = career,
                sp_patron_tel_no = Tel_patron,
                sp_patron_workplace = workplace_patron,
                sp_child_in_the_patron = NumOfChild_patron,
                sp_parttime	= pastime,
                sp_parttime_income = career_income,
                sp_parttime_type = Type_address_pastime,

                sp_received_scholar = received_scholar,
                sp_year_received_scholar = received_year_scholar,
                sp_money_received_scholar = prize,
                # sp_report = details,
                sp_path_to_avatar = picture
            )
            data_user = User.objects.filter(id = request.user.id).update(first_name =firstname_th,last_name=lastname_th)
    
    return redirect('home')
    
@login_required (login_url='index')
def editHistoryNisit(request):
    edit = Scholar_profile.objects.filter(sp_userid = 13)
    edit = edit[0]
    return render(request,'Form_Nisit/edit_historyNisit.html',{'edit':edit})    
    