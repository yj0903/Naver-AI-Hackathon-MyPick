1. naver ai hackathon "Mypick"
>> 얼굴 인식 ai facenet 모델 이용
>> 다수의 사람이 등장하는 동영상에서 특정 인물이 등장하는 장면만 편집하여 짧은 영상을 제공하는 서비스


2. 환경설정
>> conda activate tensor1.2
>> pip install -r requirements.txt

3. 환경변수
/facial-recognition-video-facenet-master/scr 에서 
>> PYTHONPATH=$(pwd)

3-2 윈도우에서는 파워셀 사용.
/facial-recognition-video-facenet-master/src 위치에서
>> env:PYTHONPATH=(pwd)

4. 학습데이터 align
/facial-recognition-video-facenet-master에서
>> python ./src/align/align_dataset_mtcnn.py 

5. classifier 학습(/trained_classifier/newglint_classifier.pkl가 업데이트된다.)
/facial-recognition-video-facenet-master에서
>> python ./scr/classifier_train.py

6. test
<비디오로 test실행>
>> python ./src/newglint.py

+++++++++++++
React Native 사용
ios, android 모두 호환 가능한 크로스 플랫폼으로 ios 기준으로 개발
