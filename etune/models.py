from django.conf import settings
from django.db import models
from private_storage.fields import PrivateFileField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.utils import timezone
from django_resized import ResizedImageField
from django.contrib.auth.models import User


import os



class Scholar_news (models.Model):          #Database สำหรับข่าวประชาสัมพันธืท้งหมด
    sn_header = models.CharField(max_length=256)
    sn_description = models.TextField() #text
    sn_expire_date = models.DateField() #วันที่
    sn_photo_bg = models.ImageField(upload_to='uploads/') #photo
    sn_path_to_pdf = models.FileField(upload_to='documents/') #pdf
    sn_create_time = models.DateField(default=timezone.now)
    
    class Meta:
        ordering = ['-sn_create_time']

    def __str__(self):
        return str(self.sn_header)


class Scholar_info (models.Model):           #Database สำหรับข่าวรับทุนทั้งหมด
    
    si_name	= models.CharField(max_length=256)
    si_description	= models.TextField()
    si_total_amount	= models.IntegerField() #จำนวนเงินทั้งหมด
    si_individual_amount = models.IntegerField() #เงินหารเฉลี่ย
    si_max_scholar	= models.IntegerField() #จำนวนคนที่ได้รับ
    si_remain_scholar = models.IntegerField() #จำนวนเงินทุนที่เหลือปัจจุบัน
    si_source	 = models.CharField(max_length=256) #ภายนอก/ใน
    si_source_name	= models.JSONField() #ผู้ให้ทุน
    si_photo_bg = ResizedImageField(upload_to='uploads/info',size=[1280, 720], crop=['middle', 'center'],quality=100)
    si_path_to_pdf = models.FileField(upload_to='documents/info')
    si_note	= models.TextField()	
    si_grade_require = 	models.FloatField(null=True)
    si_create_time = models.DateField(default=timezone.now)
    si_expire_time = models.DateField()
    si_year = models.CharField(max_length=4)
    si_semester = models.IntegerField()

    class Meta:
        ordering = ['-si_create_time']


    def __str__(self):
        return str(self.si_name)
    

class add_commit(models.Model):     #Database เพิ่มรายชื่อกรรมการ
    ac_email	=  models.CharField(max_length=256)
    ac_firstname =  models.CharField(max_length=256)
    ac_lastname = models.CharField(max_length=256)
    
    def __str__(self):
        return str(self.ac_firstname)

class add_scholar_Commit(models.Model):     #Database เพิ่มทุนให้กรรมการ
    id_commit = models.ForeignKey(User, on_delete=models.CASCADE) #id ของกรรมการ
    Scholar_name = models.ForeignKey(Scholar_info,on_delete=models.CASCADE) #id ของทุน
    def __str__(self):
        return str(str(self.id_commit)+" เข้าถึงทุน"+str(self.Scholar_name))

    
class Scholar_weight_score(models.Model): #สร้างแบบฟอร์มการให้คะแนนสัมภาษณ์
    sws_si_id = models.OneToOneField(Scholar_info,on_delete=models.CASCADE)
    sws_info = models.JSONField()
    sws_date = models.DateField(default=timezone.now)
    status = models.BooleanField(default=False)


    def __str__(self):
        return str(self.sws_si_id)


class Scholar_profile(models.Model): #กรอกแบบฟอร์มนิสิต
    sp_userid = models.OneToOneField(User,on_delete=models.CASCADE)
    sp_advisor_professor =  models.CharField(max_length=64,null=True) #อาจารย์ที่ปรึกษา
    sp_status = models.IntegerField(null=True) #status
    sp_title_en	= models.CharField(max_length=10,null=True) #Title English
    sp_firstname_en	= models.CharField(max_length=64,null=True) #	Firstname English
    sp_middlename_en = models.CharField(max_length=64,null=True)	#Middlename English
    sp_lastname_en = models.CharField(max_length=64,null=True) #lastname English
    sp_std_code	= models.CharField(max_length=10,null=True) #Student ID
    sp_title_th	= models.CharField(max_length=10,null=True) #Title Thai
    sp_firstname_th	= models.CharField(max_length=64,null=True) #	Firstname Thai
    sp_middlename_th = models.CharField(max_length=64,null=True)	#Middlename Thai
    sp_lastname_th = models.CharField(max_length=64,null=True)	#Lastname Thai
    sp_path_to_avatar = ResizedImageField(upload_to='uploads/avatar',size=[300, 300], crop=['middle', 'center'],quality=100)	#	path to avatar
    sp_date_of_birth = 	models.DateField(default=timezone.now) #date of birth
    sp_major = models.CharField(max_length=4,null=True) #major
    sp_grade = models.CharField(max_length=4,null=True) #grade
    sp_path_to_pdf_json	= models.JSONField(null=True) #path to pdf file in json 
    sp_std_address = models.JSONField(null=True) #address
    sp_std_tel_no = models.CharField(max_length=10,null=True) #tel

    #บิดา
    sp_father_title = models.CharField(max_length=10,null=True)    #คำนำหน้า
    sp_father_firstname	= models.CharField(max_length=64,null=True) #firstname dad
    sp_father_middlename = models.CharField(max_length=64,null=True) #middlename dad 
    sp_father_lastname = models.CharField(max_length=64,null=True) #lastname dad
    sp_father_date_of_birth = models.DateField(default=timezone.now)    #วันเกิด
    sp_father_age = models.IntegerField(blank=True,null=True)   #อายุ
    sp_father_status_married = models.CharField(max_length=64,null=True)  #สถานะสมรส
    sp_father_statuslife = models.CharField(max_length=64,null=True)  #สถานะการมีชีวิตอยู่
    sp_father_income = models.IntegerField(blank=True,null=True) #รายได้ต่อเดือน
    sp_father_career = models.CharField(max_length=64,null=True)#อาชีพ
    sp_father_workplace = models.CharField(max_length=128,null=True)#สถานที่ประกอบการ
    sp_father_address = models.JSONField(null=True) #address dad
    sp_father_tel_no = models.CharField(max_length=10,null=True) #Tel dad

    #มารดา
    sp_mother_title = models.CharField(max_length=10,null=True)    #คำนำหน้า
    sp_mother_firstname	= models.CharField(max_length=64,null=True) #firstname mom
    sp_mother_middlename = models.CharField(max_length=64,null=True) #middlename mom
    sp_mother_lastname = models.CharField(max_length=64,null=True) #lastname mom
    sp_mother_address = models.JSONField(null=True) #address mom
    sp_mother_date_of_birth = models.DateField(default=timezone.now)#วันเกิด
    sp_mother_age = models.IntegerField(blank=True,null=True)   #อายุ
    sp_mother_status_married = models.CharField(max_length=64,null=True) #สถานะสมรส
    sp_mother_statuslife = models.CharField(max_length=64,null=True)  #สถานะการมีชีวิตอยู่
    sp_mother_income = models.IntegerField(blank=True,null=True) #รายได้ต่อเดือน
    sp_mother_career = models.CharField(max_length=64,null=True) #อาชีพ
    sp_mother_workplace = models.CharField(max_length=128,null=True)  #สถานที่ประกอบการ
    sp_mother_tel_no = models.CharField(max_length=10,null=True) #Tel mom
    sp_bro_n_sis = models.JSONField(null=True) #ชื่อพี่น้องการศึกษาอาชีพสถานที่ประกอบการ

    #เกี่ยวกับนิสิตและผู้ปกครอง
    sp_loan = models.CharField(max_length=32,null=True) #which are you loan?(กรอ,กยศ,ไม่เคยกู้)
    sp_income = models.IntegerField(blank=True,null=True) #moneyPerMonth 
    sp_income_source = models.CharField(max_length=32,null=True) #income source
    sp_patron_relation = models.CharField(max_length=32,null=True) #patron relation
    sp_patron_career = models.CharField(max_length=64,null=True) #patron career
    sp_patron_tel_no = models.CharField(max_length=64,null=True) #patron tel
    sp_patron_workplace = models.JSONField(null=True) #patron workplace
    sp_child_in_the_patron = models.IntegerField(blank=True,null=True) #child in the patron
    sp_parttime	= models.CharField(max_length=10,null=True) #Have you ever worked part time?
    sp_parttime_income = models.IntegerField(blank=True,null=True) #parttime income
    sp_parttime_type = models.CharField(max_length=128,null=True)	#parttime type

    #ทุนที่เคยได้รับ
    sp_received_scholar = models.CharField(max_length=128,null=True) #ทุนการศึกษา
    sp_year_received_scholar = models.CharField(max_length=4,null=True) #ปีการศึกษา
    sp_money_received_scholar = models.IntegerField(blank=True,null=True) #มูลค่าของทุนที่ได้รับ

    #เขียนรายละเอียดเพิ่มเติม
    sp_report = models.TextField(null=True) #detail
    

    def __str__(self):
        return str(self.sp_userid)

class File_Models(models.Model):
    fm_upload_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    fm_Scholar = models.ForeignKey(Scholar_info,on_delete=models.CASCADE,null=True)
    fm_file = PrivateFileField("File")

class Scholar_app(models.Model):
    sa_userid = models.OneToOneField(User,on_delete=models.CASCADE) 
    sa_si_id = models.OneToOneField(Scholar_info,on_delete=models.CASCADE) #id ทุน
    sa_sp_id =	models.ForeignKey(Scholar_profile,on_delete=models.CASCADE) #id นิสิต
    sa_status =	models.IntegerField()	#สถานะการยื่นทุน
    sa_score = models.IntegerField(blank=True) #คะแนนเฉลี่ยรวม(คะเเนนสอบสัมภาษณ์)
    sa_score_info =	models.JSONField()  #คะแนนรายข้อ(คะเเนนสอบสัมภาษณ์)
    sa_path_to_pdf = PrivateFileField("File") #ไฟล์ข้อมูลเพิ่มเติม