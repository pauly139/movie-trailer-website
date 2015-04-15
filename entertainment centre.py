import fresh_tomatoes
import media

# Create Movie Objects
toy_story = media.Movie("Toy Story",
                        "Cowboy and Space Guy",
                        "http://1.bp.blogspot.com/_uznC7sISl3A/TOJvSWcg8LI/AAAAAAAAB4k/j6K3OsK3-Qo/s1600/New-Toy-Story-3-Poster.jpg",
                        'https://www.youtube.com/watch?v=y-PWzNjT_pM',
                         103,
                         414984497)

avatar = media.Movie("Avatar",
                     "Cute Blue Aliens",
                     "http://www.leawo.com/blog/wp-content/uploads/2009/12/avatar6.jpg",
                     'https://www.youtube.com/watch?v=uAEFb291hak',
                      162,
                      760505847)

matrix = media.Movie("The Matrix",
                     "Inside the machine...",
                     "http://www.repugnant-conclusion.com/the-matrix.jpg",
                     'https://www.youtube.com/watch?v=7GSgWzmR_-c',
                      136,
                      171479930)

school_of_rock = media.Movie("School of Rock",
                     "A teacher with a difference",
                     "http://www.englishmoviez.com/wp-content/uploads/2012/09/The-School-of-Rock.jpg",
                     'https://www.youtube.com/watch?v=oP7kExN8LFA',
                      108,
                      35000000)

from_paris_with_love = media.Movie("From Paris with Love",
                                   "A little bit of fighting",
                                   "https://tse3.mm.bing.net/th?id=JN.IeGfRZ%2ft5%2f1Bbk1z6legJw&w=79&h=135&c=7&rs=1&qlt=90&o=4&pid=1.7",
                                   'https://www.youtube.com/watch?v=CDR4WLX7V-I',
                                    92,
                                    23979741)

# Create Movie List and pass to fresh_tomatoes
movie_list = [toy_story, avatar, matrix, school_of_rock, from_paris_with_love]
fresh_tomatoes.open_movies_page(movie_list)

# Test Code for inheritance
#from_paris_with_love.show_info()
