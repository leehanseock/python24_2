import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 단일 페이지 URL
url = "https://youth.seoul.go.kr/infoData/sprtInfo/list.do?key=2309130006&sc_ctgry=PDS_04_YC"
base_url = "https://youth.seoul.go.kr"  # 기본 URL
hdr = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

# 페이지 요청 및 HTML 파싱
res = requests.get(url, headers=hdr)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# CSV 파일 생성 및 열기
filename = "청년지원정보_마음건강.csv"

with open(filename, mode="w", encoding="utf-8-sig", newline="") as f:
    writer = csv.writer(f)
    # CSV 헤더 작성
    attributes = ["정책명", "모집상태", "이미지 URL"]
    writer.writerow(attributes)

    # 클래스 이름과 모집 상태 매핑
    status_mapping = {
        "state bg-gray-66": "마감",
        "state bg-blue": "모집중",
        "state bg-gray-e5": "상시"
    }

    # 현재 페이지에서 데이터 수집 (feed-item 기준)
    feed_items = soup.find_all("div", attrs={"class": "feed-item"})
    if not feed_items:
        print("데이터를 찾을 수 없습니다.")

    for feed_item in feed_items:
        try:
            # 하위 클래스 item-overlay에서 정책명 추출
            overlay = feed_item.find("a", class_="item-overlay")
            title = overlay.get_text(strip=True) if overlay else "정책명 없음"

            # 모집 상태 추출 (class 이름에 따라 상태 매핑)
            status_tag = feed_item.find("span", class_=lambda x: x and x.startswith("state"))
            if status_tag:
                class_name = " ".join(status_tag["class"])
                status = status_mapping.get(class_name, "정보 없음")  # 매핑된 상태 가져오기
            else:
                status = "정보 없음"

            # 이미지 URL 추출 (src 속성만 가져오기)
            img_tag = feed_item.find("img")
            imgurl = img_tag['src'] if img_tag else ""  # src 속성을 가져옴
            if imgurl:
                imgurl = urljoin(base_url, imgurl)  # 상대 경로를 절대 경로로 변환

            # 데이터 출력 및 CSV 저장
            print(f"정책명: {title}, 모집상태: {status}, 이미지 URL: {imgurl}")
            writer.writerow([title, status, imgurl])

        except Exception as e:
            print(f"오류 발생: {e}")