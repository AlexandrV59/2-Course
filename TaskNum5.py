dictionary = {'Iron Man': 'Robert Downey Jr.',
              'Captain America': 'Chris Evans',
              'Thor': 'Chris Hemsworth',
              'Black Widow': 'Scarlett Johansson',
              'Pepper Potts': 'Gwyneth Paltrow'}
main_list = []
for key in dictionary.items():
    main_list.append(key)
first_pos = main_list[0]
last_pos = main_list[-1]
main_list[0] = last_pos
main_list[-1] = first_pos
main_list.remove(main_list[1]) # i can use function dell, if u want u can ...
dictionary = dict(main_list) #convert list to dictionary
dictionary.update(new_key='new_value')
print(dictionary)
