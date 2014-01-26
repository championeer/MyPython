#-*- coding:utf-8 -*-
#计算输入的两个时间点的时间长度，例如1110到1211的时间长度是1小时1分钟
#start_time = int(raw_input("Please input start time: "))
#end_time = int(raw_input("Please input end time: "))
start_time = raw_input("Please input start time: ")
end_time = raw_input("Please input end time: ")

def timeclapse(a,b):
        time_minutes_1 = int(a[:2])*60+int(a[2:4])
        time_minutes_2 = int(b[:2])*60+int(b[2:4])
        time_length = (time_minutes_2 - time_minutes_1)/60.0
        time_hour = time_length//1
        #print time_length
        #print time_hour
        time_minute = (time_length - time_hour)*60
        #print time_minute
        print "You cost %02d hours %02.0f minutes."%(time_hour,time_minute)

timeclapse(start_time,end_time)

