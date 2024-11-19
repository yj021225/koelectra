import json

# 파일 로드 함수
def load_reviews(file_path, app_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        reviews = json.load(file)
        # 각 리뷰에 'app' 필드 추가
        for review in reviews:
            review['app'] = app_name
    return reviews

# abouthere와 yanolja 파일 불러오기
abouthere_reviews = load_reviews("abouthere_2020_labeled_reviews.json", "abouthere")
yanolja_reviews = load_reviews("yanolja_2020_labeled_reviews.json", "yanolja")

# 두 리뷰 리스트 합치기
merged_reviews = abouthere_reviews + yanolja_reviews

# 합친 파일 저장
with open("hotelapp_2020_reviews.json", "w", encoding='utf-8') as file:
    json.dump(merged_reviews, file, ensure_ascii=False, indent=4)

print("파일이 성공적으로 병합되었습니다.")

