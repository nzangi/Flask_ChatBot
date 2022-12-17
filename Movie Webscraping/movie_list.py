import random
import requests
from bs4 import BeautifulSoup
from csv import writer

url = "https://www.imdb.com/chart/top/"


def main():
    global movie_list
    movie_list = []
    global actors
    global titles
    global years
    global ratings

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    movie_tags = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    rating_tags = soup.select("td.posterColumn span[name = ir]")
    # print(movie_tags)
    global years
    for movie_number in range(10):
        movietag0 = movie_tags[movie_number]
        movie_split = movietag0.text.split()
        movie_list.append(movie_split)

    print(movie_list)

    # def get_year(movie_tags):
    global year

    years = []
    for idx in range(10):
        movie_split = movie_tags[idx].text.split()
        year = movie_split[-1]
        years.append(year)
    print(years)

    # years_1 = [get_year(tag) for tag in years]
    # years_1 = get_year(movie_tags)
    # print(get_year(movie_tags))
    # print(years_1)
    for i in range(10):
        actors = []
        titles = []

        inner_tag = inner_movietags[i]
        print(inner_tag)
        actor = inner_tag['title']
        actors.append(actor)
        title = inner_tag.text
        titles.append(title)
        # print("<----------------------------------------------------------------------------->")
        print(actors)
        # print("<------------------------------------------------------------------------------>")
        print(titles)
    for i in range(10):
        ratings = []
        rating_tag = rating_tags[i]
        ratings.append(rating_tag['data-value'])
        print(ratings)

    with open("movie data", 'w', encoding='utf8', newline='') as file:

        thewritter = writer(file)
        header = ['Movie Title', 'Movie Actors', 'Release Year', 'Movie Rating']
        thewritter.writerow(header)

        for i in range(10):
            # the_movies = movie_list[i]
            the_titles = titles[i].replace("\n",'')
            the_actors = actors[i].replace("\n",'')
            the_years = years[i].replace("\n",'')
            the_ratings = ratings[i].replace("\n",'')
            info =[the_titles,the_actors,the_years,the_ratings]
            thewritter.writerow(info)


if __name__ == "__main__":
    main()
