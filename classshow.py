#编写一个Restaurant类
class Restaurant():
    """
    饭店类
    """
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print("饭店名称为："+ self.restaurant_name+",类型为："+self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name+" 正在营业")

    def set_number_served(self,diner):
        self.number_served=diner

    def increment_number_served(self,number):
        self.number_served+=number

    def read_information(self):
        print("有 "+str(rst1.number_served)+" 个人正在就餐")

"""
rst1=Restaurant("西安往事饭店","中餐")
rst1.describe_restaurant()
rst1.open_restaurant()

rst1.set_number_served(3)
rst1.read_information()

rst1.increment_number_served(7)
rst1.read_information()
"""

#编写IceCreamStand类
class IceCreamStand(Restaurant):
    """
    继承Restaurant类
    """

    def __init__(self,restaurant_name,cuisine_type):
        super(IceCreamStand, self).__init__(restaurant_name,cuisine_type)
        self.flavors=["芒果","草莓","菠萝","香蕉"]

    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)


#ice1=IceCreamStand("冰雪之城","冷饮")
#ice1.print_flavors()




#编写一个User类
class User():
    """
    一个User类
    """

    def __init__(self,first_name,last_name,age,sex):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.sex=sex
        self.login_attempts=0

    def describe_user(self):
        name=self.first_name+self.last_name
        print("此人姓名叫做："+name+".性别："+ self.sex+".年龄："+str(self.age))

    def greet(self):
        print("欢迎"+self.first_name+self.last_name+"光临")

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_logon_attempts(self):
        self.login_attempts=0

"""
people1=User("仵","文强",29,"男")
people1.describe_user()
people1.greet()
people1.increment_login_attempts()
print(people1.login_attempts)
people1.increment_login_attempts()
people1.increment_login_attempts()
people1.increment_login_attempts()
print(people1.login_attempts)
people1.reset_logon_attempts()
print(people1.login_attempts)
"""
#编写Privileges类
class Privileges():
    """
    为Admin类的实例属性
    """

    def __init__(self):
        self.privileges_showlist=["添加","删除","禁用"]

    def show_privileges(self):
        print("管理员拥有以下权限：")
        for privilege in self.privileges_showlist:
            print(privilege)




class Admin(User):
    """
    继承User类
    """

    def __init__(self,first_name,last_name,age,sex):
        super().__init__(first_name,last_name,age,sex)
        self.privileges=Privileges()


#u1=Admin("王","萌",28,"女")
#u1.privileges.show_privileges()
from random import randint
class Die():
    """
    创建随机数
    """

    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        x=randint(1,self.sides)
        print(x)

    def update_sides(self,number):
        self.sides=number

"""        
a=Die()
a.update_sides(20)
for i in range(10):
    a.roll_die()
"""

class FileName():
    """
    文件读取
    """
    def read_file(self,filename):
        with open(filename,encoding='utf-8') as filelists:
            lines=filelists.readlines()
            print(lines)
        for i in range(3):
            for line in lines:
                print(line.rstrip())

    def update_file(self,filenamel):
        with open(filenamel,encoding='utf-8') as filelists:
            lines=filelists.readlines()
            for line in lines:
                print(line.replace('Python','C'))
                #print(line.rstrip())

    def write_file(self):
        while True:
            name=input("请输入小狗的名字,退出请按q!")
            if name=='q':
                break
            print("欢迎"+name+"光临！")
            with open('dogs.txt','a',encoding='utf-8') as filenames:
                filenames.write(name+'\n')

#f1=FileName().read_file(r'D:/soft/development/python/code/goodstudy/study/learning_python.txt')
#f2=FileName().update_file(r'D:/soft/development/python/code/goodstudy/study/learning_python.txt')
#f3=FileName().write_file()


class FileException():
    """
    异常处理
    """
    def add(self):
        while True:
            try:
                a=input("请输入整数：")
                b=input("请输入整数：")
                num=int(a)+int(b)
            except ValueError:
                print("输入不是整数，请重新输入")
            else:
                print(a+"+"+b+"="+str(num))
                break

#eg=FileException().add()


    def fileread(self,namefile,word_a):
        try:
            with open(namefile,encoding="utf-8") as file_eg:
                strl=file_eg.read()
        except FileNotFoundError:

            print(namefile+"不存在")
        else:
            words=strl.split()
            num=len(words)
            print("本书共有"+str(num)+"个单词")
            num1=strl.lower().count(word_a)
            print(word_a+"总共出现了"+str(num1)+"次")




#eg1=FileException().fileread("Ascanio.txt","goethe")
"""
#
txtlists=["cats.txt","dogs.txt"]
for txtlist in txtlists:
    eg1=FileException().fileread(txtlist)
"""
import json
def stonum_write(jsonfile):
    number=input("请输入一个您喜欢的数字：")
    with open(jsonfile,'w') as json_eg:
        json.dump(number,json_eg)

def stonum_read(jsonfile):
    try:
        with open(jsonfile) as json_eg1:
            num1=json.load(json_eg1)
    except FileNotFoundError:
        stonum_write(jsonfile)
    else:
        print("您最喜欢的数字是："+str(num1))
#s1=Storage().stonum_write('numberfile.json')
stonum_read('numberfile.json')









