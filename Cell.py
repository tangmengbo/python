
# -*- coding: utf-8 -*-
import random

import string

def text_createH(fileNmae,msg,msg1,propryNameArray,methodArray,msg3):
    full_path = '/Users/tangmengbo/Desktop/python-H-M/' + fileNmae + '.h'
    file = open(full_path, 'w')
    file.write('//\n//  '+fileNmae+'.h\n//  ZhangYu\n\n//  Created by tmb bo on 2018/7/12.\n//  Copyright ©  2018年 tmb. All rights reserved.\n//')
    file.write('\n\n'+msg)
    file.write(msg1)
    for propertyName in propryNameArray:
        file.write('@property(nonatomic,strong)'+random.choice(classArray)+' * '+propertyName+';\n')
    file.write('\n\n')
    for methodName in methodArray:
        file.write('- (void)initData'+methodName+'VC:(NSDictionary *)info;\n')
    file.write(msg3)
    file.close()
    print('Done')

def text_createM(fileNmae,msg,msg1,methodArray,msg3):
    full_path = '/Users/tangmengbo/Desktop/python-H-M/' + fileNmae + '.m'
    file = open(full_path, 'w')
    file.write('//\n//  '+fileNmae+'.m\n//  ZhangYu\n\n//  Created by  tmb bo on 2018/7/12.\n//  Copyright ©  2018年 tmb. All rights reserved.\n//\n\n')
    file.write(msg)
    file.write(msg1)
    mViewArray = []
    for methodName in methodArray:
        file.write('- (void)initData'+methodName+'VC:(NSDictionary *)info\n{\n\n  NSMutableArray * viewArray = [NSMutableArray array];\n\n')
        number = random.randint(3, 10)
        for i in range(1,number):
            mViewArray.append(random.choice(array))
        mViewArray = list(set(mViewArray))
        for viewName in mViewArray:
            className = random.choice(viewArray)
            file.write(' '+className+' * '+viewName+' = '+'[['+className+' alloc]initWithFrame:CGRectMake('+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+','+str(random.randint(0,100))+')];\n')
            file.write(' '+viewName+'.layer.cornerRadius ='+str(random.randint(5,10))+';\n')
            file.write(' [self addSubview:'+viewName+'];\n')
            file.write(' [viewArray addObject:'+viewName+'];\n\n')
        file.write('\n}\n\n')
    file.write(msg3)
    file.close()
    print('Done')

classArray = ['NSString','UILabel','NSDictionary','NSData','UIScrollView','UIView']
viewArray = ['UIScrollView','UIView','UILabel']
array = ['DthiMdmy', 'VbbzbpBfawsk', 'EtaanUzttv', 'HlbsTrpu', 'IqciddYmvtbu', 'FmdxjZmerz', 'GnmjonYstgoo', 'PlglWhvi', 'VfgpdrPlummr', 'NbssRnuh', 'UdoxajSrehwq', 'IqdtgpCtywyu', 'ZvegCxju', 'VivzioUwlmve', 'KywwunBiqvgl', 'IgowRybt', 'EctvQihk', 'VerdeHbzjl', 'GahsdhLwxkdf', 'SxtwuhNqonkp', 'PszlnZcquh', 'GoecDorh', 'RuilOcjq', 'VicebpSbbkyk', 'JvyccbQozndi', 'AlwcwoBgicoq', 'WpwdOtbu', 'ByrbrCoanm', 'RdyiHkvj', 'TkckuZzztd', 'AptaPohf', 'ZbvnvuCsjfqg', 'NjecHqfg', 'HdylyLylwy', 'HdjixZnzwz', 'VqfvrGunep', 'PxxtvgEpzvja', 'UpvgkhUrefdt', 'PfuusNhare', 'IyevAico', 'CdueKwux', 'SpaiybHofews', 'PysikaXiwbos', 'NthjuVhckc', 'WawlqyWrkflf', 'NjkivKzduk', 'DbheadGfjfkk', 'TwbuExme', 'QqaenTajtc', 'XfgeUmnx', 'GtpjScdb', 'EmaxkrApgyqu', 'WhinslRbjgnd', 'RvhjYpqc', 'OncfhaQpwrzz', 'XaespRlvnz', 'RargUfme', 'EdcggWitvd', 'CzwsJisc', 'AasbwNgvjp', 'EfjlsjOnsxfd', 'JgejOerq', 'UkftNiny', 'EkrtdQtjns', 'QtjrrVokbf', 'WqooeXpvgx', 'CnouaQwhoi', 'RkspPwut', 'XnfjvtAqoein', 'BwolvvUspygc', 'BkvhbpBljwit', 'QblaJsrj', 'MgoashJnjzkc', 'BtlbQojb', 'BalhWzif', 'QgjodNymqd', 'QwnzhmYzbmic', 'KljzoMansq', 'GacjLupr', 'OvykfiDgebsw', 'HluwNerp', 'MglfzzVvknyk', 'CrdredMefqcr', 'CtqdWdvk', 'RbvqiAjwrk', 'WcagiiNerxdg', 'HmpajuXmgael', 'TfwiRigc', 'RqxmwrZrgvtj', 'ApzorkPpgdpz']
array = list(set(array))


for name in array:
    propryNameArray = []
    number = random.randint(3, 10)
    for index in range(1,number):
        propryNameArray.append(random.choice(array))
    propryNameArray = list(set(propryNameArray))

    methodArray = []
    for i in range(1,5):
        methodArray.append(random.choice(array))
    methodArray = list(set(methodArray))
    text_createH(name+'TableViewCell', '#import <UIKit/UIKit.h>\n','@interface '+name+ 'TableViewCell:'+ 'UITableViewCell\n\n',propryNameArray,methodArray,'\n\n@end')
    text_createM(name+'TableViewCell', '#import "'+name+'TableViewCell.h"\n\n','@implementation '+name+'TableViewCell\n\n- (void)awakeFromNib { \n\n [super awakeFromNib];\n\n}\n\n- (id)initWithStyle:(UITableViewCellStyle)style reuseIdentifier:(NSString *)reuseIdentifier\n{\n    self = [super initWithStyle:style reuseIdentifier:reuseIdentifier];\n\n    if (self)\n    {\n    }\n   return self;\n}\n\n',methodArray,'\n\n@end')





















