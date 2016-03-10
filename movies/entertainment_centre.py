# -*- coding: utf-8 -*-
"""
Created on Wed Mar 09 18:22:01 2016

@author: karl.surmacz
"""

import media
import fresh_tomatoes

if __name__ == "__main__":
    toy_story = media.Movie("Toy Story", 
                            "A story of a boy and his toys that come to life",
                            "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    avatar = media.Movie("Avatar", 
                            "A marine on an alien planet",
                            "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                            "https://www.youtube.com/watch?v=5PSNL1qE6VY")
    waltz_with_bashir = media.Movie("Waltz with Bashir", 
                            "An Israeli film director interviews fellow veterans of the 1982 invasion of Lebanon to reconstruct his own memories of his term of service in that conflict.",
                            "https://upload.wikimedia.org/wikipedia/en/9/9f/Waltz_with_Bashir_Poster.jpg",
                            "https://www.youtube.com/watch?v=XbXdwBNkCmk")
    movies = [toy_story, avatar, waltz_with_bashir]
    #fresh_tomatoes.open_movies_page(movies)
    print(media.Movie.__module__)