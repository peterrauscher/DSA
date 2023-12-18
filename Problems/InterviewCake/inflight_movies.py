def has_two_movies(flight_length, movie_lengths):
    for movie1 in range(len(movie_lengths)):
        movie1_length = movie_lengths[movie1]
        for movie2 in range(movie1, len(movie_lengths)):
            movie2_length = movie_lengths[movie2]
            if movie1_length + movie2_length == flight_length:
                return True
    return False

def has_two_movies_fast(flight_length, movie_lengths):
    seen = []
    for movie_length in movie_lengths:
        if flight_length - movie_length in seen:
            return True
        seen.append(movie_length)
    return False

print(has_two_movies_fast(120, [80, 100, 130, 190, 30, 60, 50]))