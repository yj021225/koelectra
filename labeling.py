import json

# 파일 읽기
with open('yanolja_reviews.txt', 'r', encoding='utf-8') as file:
    reviews = json.load(file)

# 리뷰별로 라벨 추가
for review in reviews:
    if review['score'] >= 4:
        review['label'] = 1  # 긍정
    else:
        review['label'] = 0  # 부정

# 파일에 저장하기
with open('yanolja_labeled_reviews.json', 'w', encoding='utf-8') as file:
    json.dump(reviews, file, ensure_ascii=False, indent=4)

print("라벨링 완료, 'yanolja_labeled_reviews.json' 파일에 저장되었습니다.")
