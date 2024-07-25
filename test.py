import pandas as pd
from transformers import pipeline

# 데이터 준비
titles = [
    "[올림픽] 배영 200ｍ 이주호 '목표는 높게…1분55초대 기록으로 결승진출'",
    "전북 5곳 호우주의보 해제…전주 등 6곳 폭염경보 유지",
    "경남 거창에 호우주의보 해제…창원 등 8곳 폭염경보 유지",
    "尹대통령, 한동훈 등 與 신임지도부와 만찬…당정 화합 방점",
    "베트남, 전 환경부 차관 체포…'희토류 채굴 수사 관련'",
    "박영재, 딸 변호사시험 때 관리위원…'관여 안했지만 우려 인정'(종합)",
    "프랑스, 2030 동계올림픽 개최…2034년은 미국 솔트레이크시티",
    "[올림픽] 8년 만에 올림픽 돌아온 북한 다이빙…훈련 때부터 '엄근진'",
    "프로야구 대전구장에 화재…경기 개시 지연",
    "민희진-하이브 또 난타전…'업무방해 등 고소' vs '무고로 대응'(종합)"
]

categories = ["정치", "북한", "경제", "산업", "사회", "전국", "세계", "문화", "건강", "연예", "스포츠"]

# 분류 모델 로드
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# 뉴스 제목 분류 함수
def classify_titles(titles, categories):
    results = []
    for title in titles:
        result = classifier(title, candidate_labels=categories)
        results.append(result['labels'][0])
    return results

# 분류 실행
classified_categories = classify_titles(titles, categories)

# 결과 출력
for title, category in zip(titles, classified_categories):
    print(f"'{title}' -> {category}")

# 데이터프레임으로 결과 보기
df = pd.DataFrame({"Title": titles, "Category": classified_categories})
print(df)
