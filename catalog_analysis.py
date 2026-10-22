import math

movies = [
    {
    "title": "The Dune Chronicles",
    "year": 2021,
    "genres": {"sci-fi", "drama"},
    "rating": 8.6,
    "duration_min": 155,
    "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    total_raiting = 0
    for movie in movies:
        total_raiting += movie["rating"]
    mid_raiting = total_raiting / len(movies)
    return round(mid_raiting, 1)

def catalog_age_stats(movies, current_year=2026):
    movies_ages = []
    for movie in movies:
        movies_ages.append(current_year - movie["year"])
    average_age = sum(movies_ages) / len(movies_ages)
    return max(movies_ages), min(movies_ages), math.ceil(average_age)

def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"

def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def movies_genre(movies):
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print (movie["title"])

def first_movie_rating_9(movies):
    i = 0
    while i < len(movies):
        movie = movies[i]
        if movie["rating"] > 9.0:
            print(movie["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")

def count_long_movies(movies, threshold=120):
    counting = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            counting += 1
    return counting

def normalize_title(title):
    new_title = []
    words = title.split()
    for word in words:
        new_word = word[0].upper() + word[1:].lower()
        new_title.append(new_word)
    return " ".join(new_title)

def make_slug(title):
    normalized = normalize_title(title)
    lowercase = normalized.lower()
    slug = lowercase.replace(" ", "-")
    return slug

def format_report_line(movie):
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return (
        f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, '
        f"{duration}, жанры: {genres}"
    )

def titles_sorted_by_rating(movies):
    ordered = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    sorted_movies = []
    for movie in ordered:
        sorted_movies.append(movie["title"])
    return sorted_movies

def top_n_by_rating(movies, n=3):
    ordered = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    sorted_movies = []
    for movie in ordered[:n]:
        sorted_movies.append((movie["title"], movie["rating"]))
    return sorted_movies

def count_by_genre(movies):
    new_dict = {}
    for movie in movies:
        for genre in movie["genres"]:
            new_dict[genre] = new_dict.get(genre, 0) + 1
    return new_dict

def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            filmography[actor] = filmography.get(actor, [])
            filmography[actor].append(movie["title"])
    return filmography

def rating_over_average(movies):
    average = average_rating(movies)
    return {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > average
    }

def all_genres(movies):
    genres_set = set()
    for movie in movies:
        genres_set.update(movie["genres"])
    return genres_set

def common_actors(movie1, movie2):
    actors_1 = set(movie1["actors"])
    actors_2 = set(movie2["actors"])
    return actors_1 & actors_2

def genres_only_in_one(movies_a, movies_b):
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    return genres_a - genres_b

def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie
    
def print_high_rated(movies):
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))

def total_duration_over_seven(movies):
    return sum(movie["duration_min"] for movie in movies if movie["rating"] > 7)

def build_report(movies):
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет")
    print()

    print("Топ-3 фильма:")
    movies_by_title = {movie["title"]: movie for movie in movies}
    for title, _ in top_n_by_rating(movies):
        print(f"  {format_report_line(movies_by_title[title])}")
    print()

    print("Фильмов по жанрам:")
    genre_counts = count_by_genre(movies)
    ordered_genres = sorted(
        genre_counts.items(),
        key=lambda item: (-item[1], item[0]),
    )
    for genre, count in ordered_genres:
        print(f"  {genre} — {count}")
    print()

    print(f"Все жанры каталога: {', '.join(sorted(all_genres(movies)))}")

if __name__ == "__main__":
    build_report(movies)





    