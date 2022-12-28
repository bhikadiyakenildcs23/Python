Q.10. Consider the following list of movies. For each movie it also shows list of ratings. 
Write a  Python program to convert it in such a way that it stores all this data in one dictionary, 
then use  the dictionary to print the average rating for each movie, rounded to one decimal.  
movies = ["Where Eagle’s Dare", "Enter the Dragon", "Iron Fist", "Fist of Fury"]  
dare_ratings = [ 9, 10, 9.5, 8.5, 3, 7.5, 8] for the movie “Where Eagle’s Dare”  
dragon_ratings = [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ] for the movie “Enter the Dragon”  fist_ratings = [ 7, 6, 5 ] for the movie “Iron Fist”  
fury_ratings = [ 6, 5, 6, 6 ] for the movie “Fist of Fury”  
 Output:  
 Average ratings of the movie “Where Eagle’s Dare” is 7.9  
 Average ratings of the movie “Enter the Dragon” is 6.9  
 Average ratings of the movie “Iron Fist” is 6  
 Average ratings of the movie “Fist of Fury” is 5.8  


movies = ["Where Eagleâ€™s Dare", "Enter the Dragon", "Iron Fist", "Fist of Fury"]
dare_ratings = [ 9, 10, 9.5, 8.5, 3, 7.5,8 ]
dragon_ratings = [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ]
fist_ratings = [ 7, 6, 5 ]
fury_ratings = [ 6, 5, 6, 6 ]
rating =[]
rating.extend([dare_ratings,dragon_ratings,fist_ratings,fury_ratings])
dir=dict()
print("="*80)
print("MOVIES :-",movies)
print("Where Eagleâ€™s Dare :-",dare_ratings)
print("Enter the Dragon",dragon_ratings)
print("Iron Fist :- ",fist_ratings)
print("Fist of Fury :- ",fury_ratings)
print("="*80)
for i in range(len(movies)):
    dir[movies[i]]=sum(rating[i])/len(rating[i])
print("|------------------|-------------------------")
print("| Average Rating   |       MOVIES NAME")
print("|------------------|-------------------------")
for key in dir:
     print("| %.2f             |       %s"%(dir[key],key))
print("|------------------|-------------------------")
