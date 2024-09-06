city = ['jaipur' , 'delhi' , 'rajasthan' , 'mumbai' , 'noida' , 'mirzapur' , 'pune']
sort = sorted (city, key=lambda x: len(x))
print("sorted words by length :", sort)
# answer :-
#sorted words by length : ['pune', 'delhi', 'noida', 'jaipur', 'mumbai', 'mirzapur', 'rajasthan']