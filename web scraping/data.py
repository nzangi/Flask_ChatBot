import re
import requests

def extract_blog_content(content):
    content_pattern = re.compile(r'<div class="cms-richtext">(.*?)</div>')
    result = re.findall(content_pattern,content)
    return  result[0] if result else "None"

if __name__ == '__main__':
    base_url = "http://www.apress.com/in/blog/all-blog-posts"
    blog_suffix = "/wannacry-how-to-prepare/12302194"
    print("Crawling Apress.com for required blog post ...\n\n")

    respose = requests.get(base_url+blog_suffix)
    if respose.status_code == 200:
        content = respose.text.encode('utf-8','ignore').decode('utf-8','ignore')
        content = content.replace("\n",'')
        blog_post_content = extract_blog_content(content)
    for post in blog_post_content:
        print(post)

