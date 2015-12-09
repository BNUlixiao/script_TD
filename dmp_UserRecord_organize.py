# 从json中整理出DMP用户信息表

# 使用模块re,codecs,csv

# 函数：从txt数据文件读入数据
def Get_data_From_file(input_filename):

    import re,codecs
    
    DMP_realtime = codecs.open(input_filename,'r','utf-8')
    
    org,secret,phone,name = [],[],[],[]

    for line in DMP_realtime:
        
        if len(re.findall('"org" : "([^"]*)"',line)):
                org.append(str(re.findall('"org" : "([^"]*)"',line)[0]))
        else:
                org.append('')
                               
            
        if len(re.findall('"secret" : "([^"]*)"',line)):
                secret.append(str(re.findall('"secret" : "([^"]*)"',line)[0]))
        else:
                secret.append('')
                               
        if len(re.findall('"phone" : "([^"]*)"',line)):
                phone.append(str(re.findall('"phone" : "([^"]*)"',line)[0]))
        else:
                phone.append('')
                               
        if len(re.findall('"name" : "([^"]*)"',line)):
                name.append(str(re.findall('"name" : "([^"]*)"',line)[0]))
        else:
                name.append('')
                
    else:
        pass
    
    return org,secret,phone,name

# 函数：将用户信息写入csv文件
def writer_csv(org,secret,phone,name):

    import csv

    DMP_realtime_outcome = open(outcome_filename,'w',newline="")
    writer = csv.writer(DMP_realtime_outcome)

    writer.writerow(['客户','secret','手机号','联系人'])

    for k in range(len(org)):
        
        if org[k] != '' or secret[k] != '' or phone[k] != '' or name[k] != '':
            writer.writerow([org[k],secret[k],phone[k],name[k]])
        else:
            pass
        
    DMP_realtime_outcome.close()

    return

# 配置输入输出文件
input_filename = input('txt数据文件路径：')
outcome_filename = input('导出csv文件路径：')

# 从txt文件读入数据
org,secret,phone,name = Get_data_From_file(input_filename)

# 将用户信息写入csv文件
writer_csv(org,secret,phone,name)
	    

    

