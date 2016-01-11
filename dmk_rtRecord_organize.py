# 从实时接口每周使用记录的json中，按用户维度整理出请求次数、成功次数、成功率数据

# 使用模块re,csv

# 函数：从txt数据文件读入数据
def Get_data_From_file(input_filename):

    import re
    
    DMP_realtime = open(input_filename,'r')
    
    secret,totalcnt,validcnt = [],[],[]

    for line in DMP_realtime:
        if len(re.findall('"secret" : "([^"]*)"',line)):
                secret.append(re.findall('"secret" : "([^"]*)"',line)[0])
        else:
                secret.append('no name')
        
        if len(re.findall('"totalcnt" : ([0-9]*)[,|\s]',line.lower())):
                totalcnt.append(int(re.findall('"totalcnt" : ([0-9]*)[,|\s]',line.lower())[0]))
        else:
                totalcnt.append(0)
                
        if len(re.findall('"validcnt" : ([0-9]*)\s',line.lower())):
                validcnt.append(int(re.findall('"validcnt" : ([0-9]*)\s',line.lower())[0]))
        else:
                validcnt.append(0)
    
    return secret,totalcnt,validcnt

# 函数：按用户维度汇总数据
def sum_by_secret(secret,totalcnt,validcnt):
    
    num = len(secret)

    outcome_secret = list(set(secret))
    outcome_totalcnt,outcome_validcnt,outcome_ratio = [],[],[]

    for i in range(len(outcome_secret)):
        outcome_totalcnt_temp,outcome_validcnt_temp = 0,0
        
        for j in range(num):
            
            if secret[j] == outcome_secret[i]:
                outcome_totalcnt_temp = outcome_totalcnt_temp + totalcnt[j]
                outcome_validcnt_temp = outcome_validcnt_temp + validcnt[j]
            else:
                outcome_totalcnt_temp = outcome_totalcnt_temp + 0
                outcome_validcnt_temp = outcome_validcnt_temp + 0
                
        outcome_totalcnt.append(outcome_totalcnt_temp)
        outcome_validcnt.append(outcome_validcnt_temp)
        outcome_ratio.append(outcome_validcnt_temp/outcome_totalcnt_temp)

    return outcome_secret,outcome_totalcnt,outcome_validcnt,outcome_ratio

# 函数：将汇总数据写入csv文件
def writer_csv(outcome_secret,outcome_totalcnt,outcome_validcnt,outcome_ratio):

    import csv

    DMP_realtime_outcome = open(outcome_filename,'w',newline="")
    writer = csv.writer(DMP_realtime_outcome)

    writer.writerow(['客户标识','总次数','成功次数','成功率'])

    for k in range(len(outcome_secret)):
        writer.writerow([outcome_secret[k],outcome_totalcnt[k],outcome_validcnt[k],outcome_ratio[k]])
        
    DMP_realtime_outcome.close()

    return

# 配置输入输出文件
input_filename = input('txt数据文件路径：')
outcome_filename = input('导出csv文件路径：')

# 增加默认导出路径
if outcome_filename == '':
    outcome_filename = input_filename[:-4] + '.csv'
    print("使用默认导出路径：",outcome_filename)
else:
    pass

# 从txt文件读入数据
secret,totalcnt,validcnt = Get_data_From_file(input_filename)

# 按用户维度汇总数据
outcome_secret,outcome_totalcnt,outcome_validcnt,outcome_ratio = sum_by_secret(secret,totalcnt,validcnt)

# 将汇总数据写入csv文件
writer_csv(outcome_secret,outcome_totalcnt,outcome_validcnt,outcome_ratio)
	    

    

