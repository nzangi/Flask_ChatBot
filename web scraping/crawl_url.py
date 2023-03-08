import requests
from time import sleep
from bs4 import BeautifulSoup


def get_post_mapping(content):
    post_detail_list = []
    post_soup = BeautifulSoup(content,'lxml')
    h3_content = post_soup.find_all("h3")

    for h3 in h3_content:
        post_detail_list.append(
            {'title': h3.a.get_text(), 'url': h3.a.attrs.get('href')}
        )
    return post_detail_list


def get_post_content(content):
    plain_text = ''
    text_soup = BeautifulSoup(content, 'lxml')
    para_list = text_soup.find_all("div", {'class': 'cms-richtext'})

    for p in para_list:
        plain_text += p.get_text()
    return plain_text

if __name__ =='__main__':
    crawl_url = "http://www.apress.com/in/blog/all-blog-posts"
    post_url_prefix = "http://www.apress.com"

    print('Crawling Apress.com for recent blog posts...\n\n')

    response = requests.get(crawl_url)

    if response.status_code == 200:
        blog_post_details = get_post_mapping(response.content)
    if blog_post_details:
        print(f'Blog post found:{len(blog_post_details)}')

        for post in blog_post_details:
            print("Crawling content for post titled: ",post.get('title'))
            post_response = requests.get(post_url_prefix+post.get('url'))

            if post_response.status_code == 200:
                post['content'] = get_post_content(post_response.content)
            print("waiting for 10 sec before crawling the next text")
            sleep(10)
        print("Content crawled for all posts")

        for post in blog_post_details:
            print(post)
