movie = {'na': 'Kalia', 'actor': 'Amitabh Bacchan',
         'villain': 'Amjad Khan', 'Year': 1991}
print(movie)

user_actor = input('Enter the name of the actor: ')

if movie['actor'] == user_actor:
    print('\n*********DETAILS OF THE MOVIE ACTOR*********\n')
    print('        MOVIE NAME = {}'.format(movie['na']))
    print('         ACTOR NAME = {}'.format(movie['actor']))
    print('       VILLAIN NAME = {}'.format(movie['villain']))
    print(' MOVIE RELEASE DATE = {}'.format(movie['Year']))
    print('\n********************************************')

elif movie['actor'] != user_actor:
    print('Sorry the entered actor is not available in the given dictionary!')
