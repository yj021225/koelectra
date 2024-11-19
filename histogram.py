import pandas as pd
import matplotlib.pyplot as plt

# review.json 파일을 읽어와 DataFrame으로 변환
data = pd.read_json('hotelapp_2020_reviews.json')

# score 컬럼이 존재하는지 확인
if 'score' in data.columns:
    # score 값이 1에서 5 사이의 정수인 데이터만 필터링
    filtered_data = data[data['score'].isin([1, 2, 3, 4, 5])]

    # 히스토그램 생성
    plt.figure(figsize=(8, 6))
    plt.hist(filtered_data['score'], bins=5, range=(1, 6), color='skyblue', edgecolor='black', align='left')
    plt.title('Score Distribution (1 to 5)')
    plt.xlabel('Score')
    plt.ylabel('Frequency')

    # 히스토그램을 이미지 파일로 저장
    plt.savefig('score_histogram.png')
    print("히스토그램이 'score_histogram.png' 파일로 저장되었습니다.")
else:
    print("데이터에 'score' 컬럼이 존재하지 않습니다.")
