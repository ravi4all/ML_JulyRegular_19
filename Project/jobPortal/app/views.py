from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import pandas as pd

connection = pymysql.connect(host='localhost',port=3306,database='jobPortal',user='root',autocommit = True)
cursor = connection.cursor()

# skills = pd.read_csv("updateSkill.csv")
s = [["html","css","html5","css3","javascript","jquery","angular","react","angular 8","PWA"],
["php","wordpress","joomla","cms","magento","cake"],["java","jsp","servlets","jdbc","jfs","ejb","struts","spring","hibernate"],["c",'c++','c#','.net','asp.net','.net framework'],['html','python','django','flask','css','bootstrap','jquery','bootstrap','machine learning','data science','data analysis']]
skills = pd.DataFrame({"skills":s})

# skill = ["html","css"]
# print(skills)


# Create your views here.
# def index(req):
#     return HttpResponse("<h1>Welcome to Job Portal</h1>")

def index(req):
    return render(req, 'index.html')

def register(req):
    return render(req, 'register.html')

def registerUser(req):
    username = req.POST['username']
    useremail = req.POST['usermail']
    userpwd = req.POST['userpwd']
    usermobile = req.POST['usernum']

    query = "insert into users values (%s,%s,%s,%s)"
    cursor.execute(query, (username,useremail,userpwd,usermobile))

    return render(req, 'editProfile.html')

def editProfile(req):
    return render(req, 'editProfile.html')

def viewProfile(req):
    return render(req, 'viewProfile.html')

def submitProfile(req):
    email = req.POST['email']
    qualification = req.POST['qualification']
    college = req.POST['clg']
    obj = req.POST['obj']
    skills = req.POST['skills']
    cat = req.POST['cat']
    exp = req.POST['exp']

    query = "insert into userprofile values (%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(email,qualification,college,obj,cat,exp,skills))
    return render(req, 'viewProfile.html')

def loginUser(req):
    email = req.POST['email']
    pwd = req.POST['pwd']

    query = "select * from users where email = %s and pwd = %s"
    cursor.execute(query, (email,pwd))
    data = cursor.fetchall()

    query = "select skills from userProfile where email = %s"
    cursor.execute(query,(email))
    userSkills = cursor.fetchall()
    skill = userSkills[0]
    # skill = ['php']
    # print(skill[0])
    similarity = []
    for i in range(len(skills)):
        sim = len(set(skills["skills"][i]).intersection(skill)) / len(set(skills["skills"][i]).union(skill))
        similarity.append([i,sim])
    sortedSim = sorted(similarity, key=lambda x : x[1],reverse=True)
    print(sortedSim[:2])
    recommended = skills["skills"][sortedSim[0][0]]
    # print(recommended)

    return render(req, 'login.html', context={"data":data,"email":email,"recommended":recommended})