import pandas as pd

# 예시 데이터프레임 생성
f=open("crawling\\titledata\culture.txt","r",encoding="utf-8")
l=[]
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\economy.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\entertainment.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\health.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\industry.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\international.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\local.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\market-plus.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\\north-korea.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\people.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\politics.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\society.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

f=open("crawling\\titledata\sports.txt","r",encoding="utf-8")
for lines in f.readlines():
    l.append(lines.strip("\n"))
f.close()

cat = ["문화"]*500
cat.extend(["경제"]*500)
cat.extend(["연예"]*500)
cat.extend(["건강"]*500)
cat.extend(["산업"]*500)
cat.extend(["세계"]*500)
cat.extend(["전국"]*500)
cat.extend(["마켓플러스"]*500)
cat.extend(["북한"]*500)
cat.extend(["사람들"]*500)
cat.extend(["정치"]*500)
cat.extend(["사회"]*500)
cat.extend(["스포츠"]*500)

data = {
    'title': l,
    'category': cat
}

df = pd.DataFrame(data)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['title'])
y = df['category']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# 데이터셋을 학습용과 테스트용으로 나누기
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 모델 학습
model = LogisticRegression()
model.fit(X_train, y_train)

# 테스트 데이터로 예측
y_pred = model.predict(X_test)

print(f'Accuracy: {accuracy_score(y_test, y_pred)}')

def predict_category(title):
    X_new = vectorizer.transform([title])
    category = model.predict(X_new)[0]
    return category

# 예시 테스트
new_title = '0.07% 돌연변이 세포로도 뇌전증 유발…KAIST 치료제 연구'
predicted_category = predict_category(new_title)
print(f'The predicted category for the title "{new_title}" is "{predicted_category}".')
