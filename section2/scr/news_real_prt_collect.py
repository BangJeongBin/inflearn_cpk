import feedparser
from openai import OpenAI

def fetch_articles(rss_url: str, limit: int = 10):
    """RSS 피드에서 기사 제목과 설명을 추출"""
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries[:limit]:
        title = entry.title
        description = entry.description
        text = f"{title}. {description}"
        articles.append(text)
    return articles

def summarize_articles(articles, api_key: str):
    """기사들을 GPT API에 요약 요청"""
    client = OpenAI(api_key=api_key)

    # 프롬프트 작성
    prompt = (
        "다음은 부동산 뉴스 기사들입니다.\n"
        "각 기사를 요약하고 오늘의 주요 Top 5 이슈로 정리해주세요.\n\n"
    )
    for i, article in enumerate(articles, 1):
        prompt += f"{i}. {article}\n"

    # GPT API 호출
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "너는 뉴스 요약 전문가야."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    RSS_URL = "https://www.mk.co.kr/rss/50300009/"
    API_KEY = "YOUR_API_KEY"  # 👉 OpenAI API 키 입력

    # 1. 기사 가져오기
    articles = fetch_articles(RSS_URL, limit=10)

    # 2. GPT 요약 요청
    summary = summarize_articles(articles, API_KEY)

    # 3. 결과 출력
    print("오늘의 부동산 Top 5 이슈\n")
    print(summary)
