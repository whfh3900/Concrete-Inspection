# Concrete-Inspection
콘크리트 구조물 결함 검출. 100x100, 130x130 크기의 이미지를 Pytorch에서 제공하는 CNN 기반의 모델로 학습하고 Test 이미지에 해당 클래스에 해당된다고 판단한 픽셀에 Opencv 엑텡글을 이용하여 구분하는 코드이다.
- 원본코드 : https://github.com/liting111/pytorch_Concrete_Inspection
#### VGG모델을 사용하여 결과를 만들어 냈고, 정보통신산업진흥원(NIPA)에서 주관한 AI기반 교량 안전점검 자동화 과제의 중간결과물로 제출하였다. 우리는 Crack과 Spall 대신 실제 터널이 누수가 굉장히 많기 때문에 누수와 그 외 결함을 Class_1, Class_2로 설정하였다. 아쉽게도 중간결과 이후 투자자측에서 더 많은 종류의 결함검출을 원하기 때문에 개발에 더 나아가진 못했다.

# Install
` pip install pytorch ` 

# Datasets
아래 사이트에서 Crack과 Spall 결함 데이터셋을 다운받을 수 있다.

- Crack : https://www.dropbox.com/s/m5zg2s0gxu6ygor/crackSubImageForTraining.rar?dl=0
- Spall : https://www.dropbox.com/s/r3sxj33mz1gkt2a/spallSubImageForTraining.rar?dl=

# Process
## 1. Dataset path
데이터셋 경로 및 클래스가 포함된 텍스트파일을 만들어 준다.

` cd SPallData `

` python making_list.py `

## 2. Training
` python main.py ` 
실행하기 전 opts.py에서 하이퍼파라미터 및 기타 argument를 설정하고 실행하는 것을 권장한다.

## 3. Test
` python demo_test.py `

## 4. Result
- Defalt Test
![175](https://user-images.githubusercontent.com/48546917/72126500-afcd9280-33af-11ea-95d4-22bf5dac3478.png)
![392](https://user-images.githubusercontent.com/48546917/72126539-ce338e00-33af-11ea-997a-e09cf19f0650.png)

- 중간과제 결과물
![당인교_거더_결과파일1](https://user-images.githubusercontent.com/48546917/72126730-911bcb80-33b0-11ea-9296-677d31c0100a.jpg)
![당인교_거더_결과파일2](https://user-images.githubusercontent.com/48546917/72126731-92e58f00-33b0-11ea-979c-526bbee3188d.jpg)

