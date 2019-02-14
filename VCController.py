# -*- coding: utf-8 -*-
import random
import os
import string
#创建.h文件
def text_createH(fileNmae,msg,msg1,propertyNumber,methodArray,msg3):
    full_path = '/Users/tangmengbo/Desktop/download/' + fileNmae + '.h'
    file = open(full_path, 'w')
    file.write('//\n//  '+fileNmae+'.h\n//  Yemao\n\n//  Created by zhangyu on 2018/7/12.\n//  Copyright ©  2018年  fqsq. All rights reserved.\n//\n\n')
    file.write(msg)
    file.write(msg1)
    propryNameArray = []
    for index in range(1,propertyNumber):
        propryNameArray.append(random.choice(array))
    propryNameArray = list(set(propryNameArray))
    for propertyName in propryNameArray:
        file.write('@property(nonatomic,strong)'+random.choice(classArray)+' * '+propertyName+';\n')
    file.write('\n\n')
    for methodName in methodArray:
        file.write('- (NSArray *)'+methodName+';\n')
    file.write(msg3)
    file.close()
    print('Done')
#创建.m文件
def text_createM(fileNmae,msg,msg1,methodArray,msg3):
    full_path = '/Users/tangmengbo/Desktop/download/' + fileNmae + '.m'
    file = open(full_path, 'w')
    file.write('//\n//  '+fileNmae+'.m\n//  Yemao\n\n//  Created by zhangyu on 2018/7/12.\n//  Copyright ©  2018年 fqsq. All rights reserved.\n//\n\n')
    file.write(msg)
    file.write(msg1)
    for methodName in methodArray:
        file.write('- (NSArray *)'+methodName+'\n{\n\n  NSMutableArray *array = [NSMutableArray array];\n')
        number = random.randint(3, 10)
        for i in range(1,number):
            file.write('  [array addObject:@('+str(random.randint(100,999))+')];\n')
        file.write('  return array;')
        file.write('\n}\n\n')
    file.write(msg3)
    file.close()
    print('Done')

classArray = ['NSString','UILabel','NSDictionary','NSData','UIScrollView','UIView']
array = ['uzmgtQ3275', 'xyszbF5516', 'yjebF442', 'ckddvkO21895', 'mokfyzH75814', 'etuqoW7427', 'loewedI98603', 'stkcnyQ80853', 'mbjgzmI38351', 'pcljzP5565', 'nyfxA194', 'wxulX101', 'beecucS70288', 'llfuI669', 'rtdhetJ93664', 'klcopmO10900', 'xxhicxJ76250', 'arfpfjS79054', 'csarL343', 'ixcyA563', 'yqglI855', 'expfP081', 'ojlzrP5046', 'ntsyrV7910', 'agszbtZ49877', 'aouicN3820', 'witpouR51763', 'ejooP339', 'uxzqnyV83127', 'hrdoeK5601', 'uagviN4009', 'hlfwC484', 'onyiyQ5321', 'jlpkP777', 'kibggJ1307', 'ymexhzE79036', 'plpcqL8787', 'iiqqaJ8686', 'plairR6973', 'crmgzI1810', 'qothtlZ93845', 'ukqwrV4740', 'gvvnpqS24757', 'kbhqX247', 'zvuuuoN95861', 'fxhubjB14434', 'bypeM738', 'nzwgwV6301', 'msyxqgE78844', 'fpbnY655', 'yczoffK07934', 'giwjC105', 'ahcxT619', 'coqrrX2382', 'yzjxraY24245', 'yramraK64058', 'kovhbH2701', 'pexgcaF27314', 'nxejW316', 'ecxyE189', 'ppyubsE04935', 'lvyelU4822', 'bjxqgR3224', 'cuzvsjB95286', 'utihjvJ70227', 'mrdxT277', 'qgaxA107', 'jjekmhU08421', 'rgtvmM6112', 'rhlbjT9911', 'lnlvB182', 'xwmqqK4370', 'mwivY146', 'lilsujF88311', 'zbqmqwS83191', 'tbwsJ228', 'oojdG960', 'hahwesM13609', 'gvxiM779', 'krxblL0610', 'btdzM730', 'adplpR8681', 'qxsiQ962', 'jyotjhP04560', 'xgndaI4225', 'kxenjY6076', 'dtvnteY19851', 'pnvurlP12742', 'rhwbhzJ93213', 'owwbqgK01976', 'zqzwC073', 'fznowH6983', 'htgoqyA15208', 'batyJ783', 'vqumuP9674', 'oeofvlX92923', 'rifiiB3004', 'kqxcxxX42791', 'xmssdyW76846', 'fwyrG324', 'jfpmkrQ67240', 'ftlbfaO37415', 'nnsdQ090', 'pfltvY4879', 'vecdkrA01927', 'zpewY590', 'ycowjE0083', 'yowpF755', 'kyhppqJ04296', 'ajygdR8161', 'nggnouO84547', 'ksfnoF8994', 'potkV767', 'yywzR155', 'zhluoT7963', 'xnxpoaE78839', 'hzeyleP47845', 'jgphuD2595', 'nvbityI36336', 'qjqiH762', 'ldruD533', 'jbfcnwX95509', 'kdzlwhU02067', 'iunckU5094', 'czdzQ237', 'iuasE166', 'xnkbX632', 'nhksrE7654', 'pgwbD158', 'bfphdT7182', 'alercgV19656', 'bhlocB7932', 'cpmdmyX04271', 'hfzxpT4894', 'wqqqwfE42275', 'gvlyJ571', 'uajmhL3901', 'aqdgxnI66605', 'lznhbbM84701', 'tiohaK0774', 'mecpccC35458', 'wpyfttL08075', 'spolrmS16137', 'eljcrnL55365', 'fugnxfP40064', 'ehzpR447', 'srfpE998', 'eofwmP0508', 'mgdxB521', 'ypmwG749', 'pllyzyX78017', 'xklzzeH32566', 'uyshP472', 'cuzmfI5496', 'xuvpsG8182', 'dmivD716', 'qekzjY6059', 'bgldsjG96845', 'juxqaU8158', 'athgjhK27158', 'manjG032', 'awrccS2428', 'dhijN491', 'ttqtS780', 'igmzT913', 'zgnkQ668', 'rsbrtsI67596', 'wuskeeU41737', 'vxtgI098', 'vmppgbC36479', 'xvivE472', 'jbjlfM1631', 'dapzdA7581', 'vkqlyvL34379', 'zvqltW1326', 'ionqY469', 'zjwznY7204', 'rzuxgjJ16889', 'kuqkaC0470', 'sckrV023', 'sujpzdH14399', 'raetpY5199', 'vgivvP4936', 'zdsuP771', 'dnwdbwJ56430', 'nijtgP5053', 'ooiwbT2826', 'amyiU823', 'kzjsP130', 'pyrsmT1068', 'bfnnjyT72603', 'qrtjapG57803', 'zuljI650', 'bvupC326', 'wyylnR5595', 'jniclqS55961', 'zqrxqC1840', 'jijugxQ11891', 'ihlqhjQ02473', 'pllmK483', 'pqccczN86884', 'ujmwA932', 'cjcesgG93664', 'ywmyB042', 'higepmY31118', 'lmsxR830', 'rmfghH3451', 'dxzyP185', 'qvxnksK44620', 'vfjegZ5438', 'avtxW975', 'czbdgD7537', 'smcjjsQ91156', 'cyvlxeB62588', 'moljvzX28764', 'lbbzqB0831', 'gymmhaR47784', 'cdrlzE5615', 'mnfrJ050', 'honizP9831', 'wrdfV007', 'dlfedN3307', 'dragW241', 'jjsbL675', 'udgoB562', 'zjzmJ702', 'dciubnN65536', 'hevnY389', 'odyryV5326', 'gxxbV368', 'dxvhtaF93701', 'vyhxcgB93754', 'oahdvwE49341', 'bixoM951', 'mnykB147', 'dvmswjJ30147', 'vqcfwD0333', 'phozpxO39986', 'kjabpkC25903', 'fuwxxoZ77340', 'vnupgwK42195', 'qihrL997', 'tcjtmY7539', 'uumukI1289', 'ecwcW123', 'splpuN4105', 'uqfhI401', 'ygpsK950', 'ztzompH38195', 'gwaymP8532', 'pguheR9019', 'pfikpZ0809', 'pdxbnpI17334', 'xerxlgI21823', 'qywkO296', 'zstvX966', 'yxcrpnP68043', 'phqfsmJ74519', 'nemguC4319', 'ppviP581', 'eoenoT1847', 'ceuxU599', 'qlixqwS89324', 'lousxrO44966', 'bwjdaeD84783', 'ujzsO239', 'adzwvoV51346', 'xenlK460', 'ouawX710', 'azkuaoU27813', 'bjdnV243', 'adprmzE48270', 'yonmznC58212', 'ixjwP609', 'hpeoC598', 'fidgH879', 'zahmR404', 'lsjcQ957', 'apzwzwD80129', 'ekyhZ643', 'mvgvZ364', 'jufyfU5821', 'nlnrjI1097', 'qrrqS094', 'katwT748', 'saxpV906', 'huhxT286', 'lsnmehT22064', 'wrgwvtB64248', 'pxjbdbX67575', 'vxzoJ671', 'zqmpC835', 'agxhssQ46421', 'ozypqyD02855', 'ctnpQ759', 'nntriuW01473', 'hrekD375', 'tmlbhY8616', 'clanfY1101', 'yljoT539', 'psotlwK30579', 'mbdbO093', 'fppcnU9198', 'nvegH722', 'ybnrV316', 'sxnemxH11730', 'cabcO366', 'mtscO436', 'gnhswgB53209', 'cgphqmN92224', 'qewfpdQ05118', 'mzhcW172', 'sxwrquD71668', 'uoatnL6133', 'afgxW237', 'smikrtB86438', 'awhslV4458', 'jhnphH7017', 'brkluE1980', 'nnkeJ949', 'mqmepcI35265', 'rsucK478', 'fuqeobW72360', 'wynpT876', 'zftaF744', 'qzqwjtT11456', 'ytiinU1159', 'mpjviJ1108', 'xauolJ8572', 'nieaknN40520']
array = list(set(array))

methodFirstArray = ['gsc_','asc_','push_','gpy_','vcs_','gsc_rcs_','wqo_pushTo_']
for name in array:
    number = random.randint(3, 10)
    methodArray = []
    for i in range(1,number):
        methodArray.append(random.choice(methodFirstArray)+random.choice(array)+random.choice(array))
    methodArray = list(set(methodArray))#数组去重
    text_createH(name+'ViewController', '#import <UIKit/UIKit.h>\n','@interface '+name+ 'ViewController:'+ 'UIViewController\n\n',number,methodArray,'\n\n@end')
    text_createM(name+'ViewController', '#import "'+name+'ViewController.h"\n\n' '@interface '+ name+'ViewController()\n\n @end\n\n','@implementation '+name+'ViewController\n\n- (void)viewDidLoad { \n\n [super viewDidLoad];\n\n}\n\n',methodArray,'\n\n@end')




















