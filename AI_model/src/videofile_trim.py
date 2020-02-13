from moviepy.editor import VideoFileClip, concatenate
import os
import time_list

def assemble_cuts(inputfile, cuts, outputfile):
    """ Concatenate cuts and generate a video file. """
    '''
    input :::
    inputfile (str) : 작업할 비디오 파일 dir.
    cuts (list) : 클립할 영상의 시작점과 끝점을 넣는다. [[시작점1, 끝점1],[시작점2,끝점2],...]
    outputfile (str) : 저장할 파일명

    return ::: 편집된 영상파일이 저장된다.
    (None) 
    '''
    video = VideoFileClip(inputfile)
    final = concatenate([video.subclip(start, end)
                         for (start, end) in cuts])
    # 파일 저장 경로를 설정하고 싶으면 사용한다.
    # os.chdir('/home/pirl/PycharmProjects/NAVER_hack/save_video')
    final.to_videofile(outputfile)

    video.reader.close()
    video.audio.reader.close_proc()

##USAGE
# 작업할 비디오 파일을 넣어준다.
inputfile = "C:\\Users\\green\\PycharmProjects\\pj1\\test.mp4"


# 시작점과 끝 점을 pair로 리스트 형식으로 넣어준다.
# # which can be expressed in seconds (15.35), in (min, sec), in (hour, min, sec), or as a string: '01:03:05.35'.
# cuts = [['0:0:0.966','0:0:3.33'], ['0:0:5.100','0:0:9.233']]
#
# assemble_cuts(inputfile, cuts, "dog_1.mp4")

#마이픽! 고르기
people_list = {'jennie':0,'jisoo':1,'lisa':2,'rose':3}
time_data = [[('0:0:0.966', 0), ('0:0:2.0', 1), ('0:0:3.033', 0), ('0:0:4.066', 1), ('0:0:5.1', 1), ('0:0:6.133', 1), ('0:0:9.233', 1), ('0:0:10.266', 0), ('0:0:11.3', 1), ('0:0:12.333', 0), ('0:0:16.466', 1), ('0:0:17.5', 1), ('0:0:18.533', 1), ('0:0:19.566', 1), ('0:0:20.6', 1), ('0:0:21.633', 1), ('0:0:24.733', 1), ('0:0:25.766', 1), ('0:0:26.8', 1), ('0:0:27.833', 1)], [('0:0:0.966', 1), ('0:0:2.0', 1), ('0:0:3.033', 1), ('0:0:4.066', 1), ('0:0:5.1', 1), ('0:0:6.133', 1), ('0:0:7.166', 1), ('0:0:8.2', 1), ('0:0:9.233', 1), ('0:0:10.266', 1), ('0:0:11.3', 1), ('0:0:12.333', 1), ('0:0:13.366', 1), ('0:0:14.4', 1), ('0:0:15.433', 1), ('0:0:17.5', 1), ('0:0:18.533', 1), ('0:0:19.566', 1), ('0:0:20.6', 1), ('0:0:21.633', 1), ('0:0:22.666', 1), ('0:0:23.7', 1), ('0:0:24.733', 1), ('0:0:25.766', 1), ('0:0:26.8', 1), ('0:0:27.833', 1)], [('0:0:0.966', 1), ('0:0:2.0', 1), ('0:0:3.033', 1), ('0:0:25.766', 0), ('0:0:26.8', 1)], [('0:0:0.966', 1), ('0:0:2.0', 1), ('0:0:3.033', 1), ('0:0:4.066', 1), ('0:0:5.1', 1), ('0:0:6.133', 1), ('0:0:7.166', 1), ('0:0:7.166', 0), ('0:0:8.2', 1), ('0:0:8.2', 1), ('0:0:9.233', 1), ('0:0:10.266', 1), ('0:0:11.3', 1), ('0:0:12.333', 1), ('0:0:13.366', 1), ('0:0:14.4', 1), ('0:0:14.4', 1), ('0:0:15.433', 1), ('0:0:18.533', 1), ('0:0:19.566', 1), ('0:0:21.633', 1), ('0:0:22.666', 1), ('0:0:22.666', 1), ('0:0:23.7', 1), ('0:0:23.7', 1), ('0:0:24.733', 1), ('0:0:25.766', 1), ('0:0:26.8', 1), ('0:0:27.833', 1)]]

mypick = input('who is your pick?: jennie/jisoo/lisa/rose')
pickone = people_list[mypick]
pick_time = [time_data[pickone]]
print(pick_time)

#등장 시간 추출
_cut = time_list.extract_timedata(pick_time)
print(mypick,'_cut', _cut[0])

#영상 자르기
assemble_cuts(inputfile, _cut[0], "mypick_2.mp4")
