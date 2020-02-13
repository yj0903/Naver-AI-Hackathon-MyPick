from moviepy.editor import VideoFileClip, concatenate
from parse import compile
import datetime
from datetime import timedelta
from datetime import time
import re
import os

#videotrim 으로 이동할 것.
def pick_people(mypick,timelist):
    # mypick! 멤버를 고른다.
    people_list = {'jennie':0, 'jisoo':1, 'lisa':2, 'rose':3}
    pick = people_list[mypick]
    time_data1 = [timelist[pick]]

    return time_data1

# 등장한 프레임만 추출한다.
def appearance_timedata (timedata):
    # 1 등장한 프레임만 찾는다.
    # input : 리스트 하나를 받아온다.
    alltheframe = []

    for i in timedata:
        if i[1] == 1:
            alltheframe.append(i)

    return alltheframe

def band_time(alltheframe):
    # 2 등장 시간을 묶는다.
    # output : [[],[],...]
    whole_time = []
    show_time = []
    # print('alltheframe',alltheframe)

    show_time.append(alltheframe[0][0])

    for i in range(1, len(alltheframe)):
        # print('itr :', i, '\n time', alltheframe[i][0], ' 사람있나? :',alltheframe[i][1])
        pick_time = datetime.datetime.strptime(alltheframe[i][0], "%H:%M:%S.%f")
        pick_time_1 = datetime.datetime.strptime(alltheframe[i - 1][0], "%H:%M:%S.%f")

        if pick_time.second == 0 and pick_time.minute == 0:
            pick_time.second = 1

        if (pick_time - pick_time_1) < datetime.timedelta(seconds=2.5):
            #연속하면
            show_time.append(alltheframe[i][0])
            # print('2초 차이 안 남. show_time',show_time)

            if i == len(alltheframe) - 1:
                show_time.append(alltheframe[i][0])
                whole_time.append(show_time)
                # print('i == len(alltheframe)-1 show_time', show_time)

        else:
            if i == len(alltheframe) - 1:
                whole_time.append(show_time)
                show_time = []
                show_time.append(alltheframe[i][0])
                # print('i == len(alltheframe)-1 show_time', show_time)

            whole_time.append(show_time)
            # print('2초 차이 남. show_time', show_time)
            # print('whole_time', whole_time)
            show_time = []
            show_time.append(alltheframe[i][0])
            # print('show_time', show_time)


    # appearance_timeset.append(whole_time)
    # print('whole_time',whole_time)

    return whole_time

def extract_timedata(timedata):
    people_list = ['jennie','jisoo','lisa','rose']
    appearance_timeset_result = []
    appearance_timeset = []

    #1 등장 프레임을 묶는다.
    for idx, appearance_frame in enumerate(timedata):
        # print('='*18, people_list[idx])
        appearance_time = []
        extend_time = []

        # 1 등장한 프레임만 찾는다. (시간, 1)
        alltheframe = appearance_timedata(appearance_frame)
        # print('alltheframe',alltheframe)

        #2 등장 시간을 묶는다.
        # if
        whole_time = band_time(alltheframe)
        # print(len(alltheframe))
        # print('main whole_time',whole_time)

        appearance_timeset.append(whole_time)
        # print('main appearance_timeset',appearance_timeset)

        for idx, _timeset in enumerate(whole_time):
            st = _timeset[0]; et = _timeset[-1];
            st_tmp = datetime.datetime.strptime(st, "%H:%M:%S.%f")
            et_tmp = datetime.datetime.strptime(et, "%H:%M:%S.%f")

            if len(whole_time) == 1:
                pass

            elif idx == 0:
                et = et_tmp + datetime.timedelta(seconds=1)
                et = et.strftime("%H:%M:%S.%f")

            elif idx == len(whole_time)-1:
                st = st_tmp - datetime.timedelta(seconds=1)
                st = st.strftime("%H:%M:%S.%f")

            else:

                st = st_tmp - datetime.timedelta(seconds=1)
                st = st.strftime("%H:%M:%S.%f")
                et = et_tmp + datetime.timedelta(seconds=1)
                et = et.strftime("%H:%M:%S.%f")

            appearance_time.append([st, et])

        appearance_timeset_result.append(appearance_time)

    return appearance_timeset_result

time_data_txt = [[('0:0:0.966', 0), ('0:0:2.0', 1), ('0:0:3.033', 0), ('0:0:4.066', 1), ('0:0:5.1', 1), ('0:0:6.133', 1), ('0:0:9.233', 1), ('0:0:10.266', 0), ('0:0:11.3', 1), ('0:0:12.333', 0), ('0:0:16.466', 1), ('0:0:17.5', 1), ('0:0:18.533', 1), ('0:0:19.566', 1), ('0:0:20.6', 1), ('0:0:21.633', 1), ('0:0:24.733', 1), ('0:0:25.766', 1), ('0:0:26.8', 1), ('0:0:27.833', 1)], [('0:0:0.966', 1), ('0:0:2.0', 1), ('0:0:3.033', 1), ('0:0:4.066', 1), ('0:0:5.1', 1), ('0:0:6.133', 1), ('0:0:7.166', 1), ('0:0:8.2', 1), ('0:0:9.233', 1), ('0:0:10.266', 1), ('0:0:11.3', 1), ('0:0:12.333', 1), ('0:0:13.366', 1), ('0:0:14.4', 1), ('0:0:15.433', 1), ('0:0:17.5', 1), ('0:0:18.533', 1), ('0:0:19.566', 1), ('0:0:20.6', 1), ('0:0:21.633', 1), ('0:0:22.666', 1), ('0:0:23.7', 1), ('0:0:24.733', 1), ('0:0:25.766', 1), ('0:0:26.8', 1), ('0:0:27.833', 1)], [('0:0:0.966', 1), ('0:0:2.0', 1), ('0:0:3.033', 1), ('0:0:25.766', 0), ('0:0:26.8', 1)], [('0:0:0.966', 1), ('0:0:2.0', 1), ('0:0:3.033', 1), ('0:0:4.066', 1), ('0:0:5.1', 1), ('0:0:6.133', 1), ('0:0:7.166', 1), ('0:0:7.166', 0), ('0:0:8.2', 1), ('0:0:8.2', 1), ('0:0:9.233', 1), ('0:0:10.266', 1), ('0:0:11.3', 1), ('0:0:12.333', 1), ('0:0:13.366', 1), ('0:0:14.4', 1), ('0:0:14.4', 1), ('0:0:15.433', 1), ('0:0:18.533', 1), ('0:0:19.566', 1), ('0:0:21.633', 1), ('0:0:22.666', 1), ('0:0:22.666', 1), ('0:0:23.7', 1), ('0:0:23.7', 1), ('0:0:24.733', 1), ('0:0:25.766', 1), ('0:0:26.8', 1), ('0:0:27.833', 1)]]
time_data = [[('0:0:0.966', 0), ('0:0:2.0', 1), ('0:0:3.033', 0), ('0:0:4.066', 1), ('0:0:5.1', 1), ('0:0:6.133', 1), ('0:0:9.233', 1), ('0:0:10.266', 0), ('0:0:11.3', 1), ('0:0:12.333', 0), ('0:0:16.466', 1), ('0:0:17.5', 1), ('0:0:18.533', 1), ('0:0:19.566', 1), ('0:0:20.6', 1), ('0:0:21.633', 1), ('0:0:24.733', 1), ('0:0:25.766', 1), ('0:0:26.8', 1), ('0:0:27.833', 1)], [('0:0:0.966', 1), ('0:0:2.0', 1), ('0:0:3.033', 1), ('0:0:4.066', 1), ('0:0:5.1', 1), ('0:0:6.133', 1), ('0:0:7.166', 1), ('0:0:8.2', 1), ('0:0:9.233', 1), ('0:0:10.266', 1), ('0:0:11.3', 1), ('0:0:12.333', 1), ('0:0:13.366', 1), ('0:0:14.4', 1), ('0:0:15.433', 1), ('0:0:17.5', 1), ('0:0:18.533', 1), ('0:0:19.566', 1), ('0:0:20.6', 1), ('0:0:21.633', 1), ('0:0:22.666', 1), ('0:0:23.7', 1), ('0:0:24.733', 1), ('0:0:25.766', 1), ('0:0:26.8', 1), ('0:0:27.833', 1)], [('0:0:0.966', 1), ('0:0:2.0', 1), ('0:0:3.033', 1), ('0:0:25.766', 0), ('0:0:26.8', 1)], [('0:0:0.966', 1), ('0:0:2.0', 1), ('0:0:3.033', 1), ('0:0:4.066', 1), ('0:0:5.1', 1), ('0:0:6.133', 1), ('0:0:7.166', 1), ('0:0:7.166', 0), ('0:0:8.2', 1), ('0:0:8.2', 1), ('0:0:9.233', 1), ('0:0:10.266', 1), ('0:0:11.3', 1), ('0:0:12.333', 1), ('0:0:13.366', 1), ('0:0:14.4', 1), ('0:0:14.4', 1), ('0:0:15.433', 1), ('0:0:18.533', 1), ('0:0:19.566', 1), ('0:0:21.633', 1), ('0:0:22.666', 1), ('0:0:22.666', 1), ('0:0:23.7', 1), ('0:0:23.7', 1), ('0:0:24.733', 1), ('0:0:25.766', 1), ('0:0:26.8', 1), ('0:0:27.833', 1)]]

time_data1 = [time_data_txt[0]]

allthetime = extract_timedata(time_data1)
print(allthetime)
