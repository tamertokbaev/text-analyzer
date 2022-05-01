from fastapi import FastAPI
from helpers.web_scrapper import extract_text_from_single_web_page
from helpers.sentiment_analyzer import analyze_text
from models.url_query import URLQuery

app = FastAPI()


@app.post("/url/analyze", description="Make sentiment analyze on content scrapped from web URL")
def analyze_url(url: URLQuery):
    url_content = extract_text_from_single_web_page(url.url)
    sentiment = analyze_text(url_content)
    return {
        "message": "success",
        "result": sentiment
    }


@app.post("/url/extract_content", description="Get text content from given URL")
def extract_content_from_url(url: URLQuery):
    url_content = extract_text_from_single_web_page(url.url)
    return {
        "message": "success",
        "content": url_content
    }