# Concrete-Inspection
콘크리트 구조물 결함 검출
#### 100x100, 130x130 크기의 이미지를 Pytorch에서 제공하는 CNN 기반의 모델로 학습하고 Test 이미지에 해당 클래스에 해당된다고 판단한 픽셀에
#### Opencv 엑텡글을 이용하여 구분하는 코드

# Install
` pip install pytorch ` 

# Datasets
아래 사이트에서 Crack과 Spall 결함 데이터셋을 다운받을 수 있다.
Crack : https://www.dropbox.com/s/m5zg2s0gxu6ygor/crackSubImageForTraining.rar?dl=0
Spall : https://www.dropbox.com/s/r3sxj33mz1gkt2a/spallSubImageForTraining.rar?dl=

# Process
## 1. Dataset path
데이터셋 경로 및 클래스가 포함된 텍스트파일을 만들어 준다.
' cd SPallData '
' python making_list.py '

## 2. Training
' python main.py ' 
실행하기 전 opts.py에서 하이퍼파라미터 및 기타 argument를 설정하고 실행하는 것을 권장한다.

## 3. Test
' python demo_test.py '
