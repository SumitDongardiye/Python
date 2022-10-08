# As soon as split method sees space it will convert it into item.
# Helps to convert string to list

some_words="PrepInsta Python course is a good way for us to learn python"

word=some_words.split()
print(word)

numbers="9,123,571,718,819,182"
print(numbers.split(","))

ind_list=[
    '9','1','2','',
    '3','5','7','',
    '1','7','1','',
]

values=" ".join(ind_list)
print(values)

final=values.split()
print(final)