import os
import google.generativeai as genai
from bing_image_urls import bing_image_urls


def get_description(keyword):
    api_key = os.getenv("API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    prompt = 'give me 1 result (to the point and just the answer) article description 180 characters max with title :' + str(keyword)
    response = model.generate_content(prompt)
    return response.text

def get_article(keyword):
    api_key = os.getenv("API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    prompt = 'give me result (to the point and just the answer) article with title "' + str(keyword) + '". the article consist of at least 300 words. every paragraphs must use <p> tags.',
    response = model.generate_content(prompt)
    return response.text

def get_image(keyword):
    image = bing_image_urls(keyword, limit=2)
    return image[0]