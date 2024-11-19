import json
import random


# JSON 파일 로드 함수
def load_reviews(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


# 특정 label에 대해 app 값 비율에 맞춰 샘플링하는 함수
def stratified_sample(reviews, target_yanolja, target_abouthere):
    yanolja_reviews = [review for review in reviews if review['app'] == 'yanolja']
    abouthere_reviews = [review for review in reviews if review['app'] == 'abouthere']

    # 목표 개수에 맞게 샘플링 (목표 개수가 리스트 크기보다 클 경우, 가능한 만큼만 샘플링)
    yanolja_sample_size = min(target_yanolja, len(yanolja_reviews))
    abouthere_sample_size = min(target_abouthere, len(abouthere_reviews))

    # 무작위 샘플링
    yanolja_sample = random.sample(yanolja_reviews, yanolja_sample_size)
    abouthere_sample = random.sample(abouthere_reviews, abouthere_sample_size)

    return yanolja_sample + abouthere_sample


# 호텔 리뷰 데이터 로드
reviews = load_reviews("hotelapp_2020_reviews.json")

# label 값에 따른 리뷰 분류
label_1_reviews = [review for review in reviews if review['label'] == 1]
label_0_reviews = [review for review in reviews if review['label'] == 0]

# 목표 개수 설정 (label 1에서 yanolja 1426, abouthere 574)
target_yanolja_1 = 713
target_abouthere_1 = 287

# label 1 샘플링
sample_label_1 = stratified_sample(label_1_reviews, target_yanolja_1, target_abouthere_1)

# label 0에서 yanolja 1426, abouthere 574
target_yanolja_0 = 713
target_abouthere_0 = 287

# label 0 샘플링
sample_label_0 = stratified_sample(label_0_reviews, target_yanolja_0, target_abouthere_0)

# 최종 샘플 합치기
sample_reviews = sample_label_1 + sample_label_0

# 결과 저장
with open("hotelapp_sampled_reviews.json", "w", encoding='utf-8') as file:
    json.dump(sample_reviews, file, ensure_ascii=False, indent=4)

print("샘플링이 완료되었습니다.")

