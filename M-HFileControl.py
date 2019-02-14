
# -*- coding: utf-8 -*-
import random
import os

def getArray():
    first = "abcdefghijklmnopqrstuvwxyz"
    second = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    third = "1234567890"
    number = "345"
    index = 0
    for i in range(5000):
        final=(random.choice(first))
        index = random.randint(3, 5)
        for i in range(index):
            final+=(random.choice(first))
        final += (random.choice(second))
        for i in range(index):
            final+=(random.choice(third))
        array.append(final)
classArray = ['NSString','UILabel','NSDictionary','NSData','UIScrollView','UIView','UITextView','UITableView','UIImageView']#.h文件里属性的类型从这个数组里随机选
viewArray = ['UILabel','UIScrollView','UIView','UITextView','UITableView','UIImageView']#.m文件里创建的元素的类型从这个数组里随机选
array = []
getArray()#用于生成.h和.m文件中将要用的属性名
array = list(set(array))
#.h文件添加废代码
def HFileAddMj(file_path,old_str1,old_str2,old_str3,old_str4,old_str5,old_str6,old_str7):
    
    file_data = ""
    Ropen=open(file_path,'r')
    for line in Ropen:
        nameStr = random.choice(array)
        className = random.choice(classArray)
        if old_str1 in line:
            line += '\n\n/*********mjfile**********/\n@property(nonatomic,strong)'+className +' * '+nameStr+';\n/*********mjfile**********/\n\n'
            file_data += line
            array.remove(nameStr)#防止创建的属性名重复(创建一个从数组中删除一个)
        elif old_str2 in line:
            line += '\n\n/*********mjfile**********/\n@property(nonatomic,strong)'+className +' * '+nameStr+';\n/*********mjfile**********/\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str3 in line:
            line += '\n\n/*********mjfile**********/\n@property(nonatomic,strong)'+className +' * '+nameStr+';\n/*********mjfile**********/\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str4 in line:
            line += '\n\n/*********mjfile**********/\n@property(nonatomic,strong)'+className +' * '+nameStr+';\n/*********mjfile**********/\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str5 in line:
            line += '\n\n/*********mjfile**********/\n@property(nonatomic,strong)'+className +' * '+nameStr+';\n/*********mjfile**********/\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str5 in line:
            line += '\n\n/*********mjfile**********/\n@property(nonatomic,strong)'+className +' * '+nameStr+';\n/*********mjfile**********/\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str5 in line:
            line += '\n\n/*********mjfile**********/\n@property(nonatomic,strong)'+className +' * '+nameStr+';\n/*********mjfile**********/\n\n'
            file_data += line
            array.remove(nameStr)
        else:
            file_data += line
    Ropen.close()
    Wopen=open(file_path,'w')
    Wopen.write(file_data)
    Wopen.close()
    print(file_data)

#.m文件添加废代码
def MFileAddMj(file_path,old_str1,old_str2,old_str3,old_str4,old_str5,old_str6,old_str7):
    
    file_data = ""
    Ropen=open(file_path,'r')#读取文件
    for line in Ropen:
        nameStr = random.choice(array)
        className = random.choice(viewArray)
        if old_str1 in line:#如果.h文件中的某一行里包含old_str,则往这一行添加一下语句
            line += '\n\n//*********mjfile**********\nif (![@"FQSQStatus" isEqualToString:FQSQSHSTATUS])\n{\n  '+className +' * '+nameStr+' = '+'[['+className+' alloc]initWithFrame:CGRectMake('+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+')];\n'+'  '+nameStr+'.layer.cornerRadius ='+str(random.randint(5,10))+';\n  '+nameStr+'.userInteractionEnabled = YES;\n  '+nameStr+'.layer.masksToBounds = YES;\n}'+'\n//*********mjfile**********\n\n'
            file_data += line
            array.remove(nameStr)#防止创建的元素名重复(创建一个从数组中删除一个)
        elif old_str2 in line:
            line += '\n\n//*********mjfile**********\nif (![@"FQSQStatus" isEqualToString:FQSQSHSTATUS])\n{\n  '+className +' * '+nameStr+' = '+'[['+className+' alloc]initWithFrame:CGRectMake('+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+')];\n  '+nameStr+'.layer.borderWidth = 1;\n  '+nameStr+'.clipsToBounds = YES;\n'+'  '+nameStr+'.layer.cornerRadius ='+str(random.randint(5,10))+';\n}'+'\n//*********mjfile**********\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str3 in line:
            line += '\n\n//*********mjfile**********\nif (![@"FQSQStatus" isEqualToString:FQSQSHSTATUS])\n{\n  '+className +' * '+nameStr+' = '+'[['+className+' alloc]initWithFrame:CGRectMake('+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+')];\n  '+nameStr+'.backgroundColor = [UIColor whiteColor];\n  '+nameStr+'.layer.borderColor = [[UIColor greenColor] CGColor];\n'+'  '+nameStr+'.layer.cornerRadius ='+str(random.randint(5,10))+';\n}'+'\n//*********mjfile**********\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str4 in line:
            line += '\n\n//*********mjfile**********\nif (![@"FQSQStatus" isEqualToString:FQSQSHSTATUS])\n{\n  '+className +' * '+nameStr+' = '+'[['+className+' alloc]initWithFrame:CGRectMake('+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+')];\n  '+nameStr+'.backgroundColor = [UIColor whiteColor];\n  '+nameStr+'.layer.borderColor = [[UIColor greenColor] CGColor];\n'+' '+nameStr+'.layer.cornerRadius ='+str(random.randint(5,10))+';\n}'+'\n  //*********mjfile**********\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str5 in line:
            line += '\n\n//*********mjfile**********\nif (![@"FQSQStatus" isEqualToString:FQSQSHSTATUS])\n{\n  '+className +' * '+nameStr+' = '+'[['+className+' alloc]initWithFrame:CGRectMake('+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+')];\n  '+nameStr+'.backgroundColor = [UIColor whiteColor];\n  '+nameStr+'.layer.borderColor = [[UIColor greenColor] CGColor];\n  '+' '+nameStr+'.layer.cornerRadius ='+str(random.randint(5,10))+';\n}'+'\n  //*********mjfile**********\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str6 in line:
            line += '\n\n//*********mjfile**********\nif (![@"FQSQStatus" isEqualToString:FQSQSHSTATUS])\n{\n  '+className +' * '+nameStr+' = '+'[['+className+' alloc]initWithFrame:CGRectMake('+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+')];\n  '+nameStr+'.backgroundColor = [UIColor whiteColor];\n  '+nameStr+'.layer.borderColor = [[UIColor greenColor] CGColor];\n'+' '+nameStr+'.layer.cornerRadius ='+str(random.randint(5,10))+';\n}'+'\n  //*********mjfile**********\n\n'
            file_data += line
            array.remove(nameStr)
        elif old_str7 in line:
            line += '\n\n//*********mjfile**********\nif (![@"FQSQStatus" isEqualToString:FQSQSHSTATUS])\n{\n  '+className +' * '+nameStr+' = '+'[['+className+' alloc]initWithFrame:CGRectMake('+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+')];\n  '+nameStr+'.backgroundColor = [UIColor whiteColor];\n  '+nameStr+'.layer.borderColor = [[UIColor greenColor] CGColor];\n  '+nameStr+'.layer.cornerRadius ='+str(random.randint(5,10))+';\n}'+'\n  //*********mjfile**********\n\n'
            file_data += line
            array.remove(nameStr)
        
        else:
            file_data += line
    Ropen.close()
    Wopen=open(file_path,'w')
    Wopen.write(file_data)
    Wopen.close()
    print(file_data)

#.m文件添加废方法代码
def MFileAddMethod(file_path,old_str1,old_str2,old_str3,old_str4,old_str5):
    
    file_data = ""
    Ropen=open(file_path,'r')#读取文件
    for line in Ropen:
        nameStr = random.choice(array)
        className = random.choice(viewArray)
        if old_str1 in line:#如果.h文件中的某一行里包含old_str,则往这一行添加一下语句
            
            strNew = '\n//*********mjfile**********\n'+('- (NSArray *)'+nameStr+'\n{\n  NSMutableArray *array = [NSMutableArray array];\n')
            number = random.randint(3, 10)
            for i in range(1,number):
                strNew+='  [array addObject:@('+str(random.randint(100,999))+')];\n'

            strNew+='  return array;'
            strNew+= ('\n}\n')+'//*********mjfile**********\n\n'
            line = strNew+line
            file_data += line
            array.remove(nameStr)#防止创建的元素名重复(创建一个从数组中删除一个)
    
        elif old_str2 in line:#如果.h文件中的某一行里包含old_str,则往这一行添加一下语句
            
            strNew = '\n//*********mjfile**********\n'+('- (NSArray *)'+nameStr+'\n{\n  NSMutableArray *array = [NSMutableArray array];\n')
            number = random.randint(3, 10)
            for i in range(1,number):
                strNew+='  [array addObject:@('+str(random.randint(100,999))+')];\n'
            
            strNew+='  return array;'
            strNew+= ('\n}\n')+'//*********mjfile**********\n\n'
            line = strNew+line
            file_data += line
            array.remove(nameStr)#防止创建的元素名重复(创建一个从数组中删除一个)

        elif old_str3 in line:#如果.h文件中的某一行里包含old_str,则往这一行添加一下语句
            
            strNew = '\n//*********mjfile**********\n'+('- (NSArray *)'+nameStr+'\n{\n  NSMutableArray *array = [NSMutableArray array];\n')
            number = random.randint(3, 10)
            for i in range(1,number):
                strNew+='  [array addObject:@('+str(random.randint(100,999))+')];\n'
            
            strNew+='  return array;'
            strNew+= ('\n}\n')+'//*********mjfile**********\n\n'
            line = strNew+line
            file_data += line
            array.remove(nameStr)#防止创建的元素名重复(创建一个从数组中删除一个)

        elif old_str4 in line:#如果.h文件中的某一行里包含old_str,则往这一行添加一下语句
            
            strNew = '\n//*********mjfile**********\n'+('- (NSArray *)'+nameStr+'\n{\n  NSMutableArray *array = [NSMutableArray array];\n')
            number = random.randint(3, 10)
            for i in range(1,number):
                strNew+='  [array addObject:@('+str(random.randint(100,999))+')];\n'
            
            strNew+='  return array;'
            strNew+= ('\n}\n')+'//*********mjfile**********\n\n'
            line = strNew+line
            file_data += line
            array.remove(nameStr)#防止创建的元素名重复(创建一个从数组中删除一个)
    
        elif old_str5 in line:#如果.h文件中的某一行里包含old_str,则往这一行添加一下语句
            
            strNew = '\n//*********mjfile**********\n'+('- (NSArray *)'+nameStr+'\n{\n  NSMutableArray *array = [NSMutableArray array];\n')
            number = random.randint(3, 10)
            for i in range(1,number):
                strNew+='  [array addObject:@('+str(random.randint(100,999))+')];\n'
            
            strNew+='  return array;'
            strNew+= ('\n}\n')+'//*********mjfile**********\n\n'
            line = strNew+line
            file_data += line
            array.remove(nameStr)#防止创建的元素名重复(创建一个从数组中删除一个)
        else:
            file_data += line
    Ropen.close()
    Wopen=open(file_path,'w')
    Wopen.write(file_data)
    Wopen.close()
    print(file_data)




def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        #print(root) #当前目录路径
        #print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件
        fileNameArray = files
        #遍历文件夹下的.h和.m文件并添加废代码
        for file in files:
            if '.h' in file:#file_dir+'/'+file含义是file_dir文件夹下的file文件
                HFileAddMj(file_dir+'/'+file, "h;","o;","w;", "y;","n;","e;","t;")#往凡是以"l;", "m;","n;","q;","y;"这些中的某一个结尾的oc语句后添加费代码
            if '.m' in file:
                MFileAddMethod(file_dir+'/'+file,"- (void)v","-(void)g","-(void)i","-(void)s","-(void)t")
                MFileAddMj(file_dir+'/'+file, "e];", "w];","t];","c];","s];","r];","k];")#往凡是以"n];", "w];","m];","c];","p];","q];","l];"这些中的某一个结尾的oc语句后添加费代码
                #往凡是以"-(void)g","- (void)v","-(void)t","-(void)i"这些开始的方法前添加费的方法
#要修改的文件所在的文件夹路径
file_floadPath = '/Users/tangmengbo/Desktop/FanQieSQ/FanQieSheQu/FQSQ_ViewController/FQSQ_OwnerViewController'

file_name(file_floadPath)










