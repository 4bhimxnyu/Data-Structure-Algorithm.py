my_hash_set = [
    [None],
    ['Jones'],
    [None],
    ['Lisa'],
    [None],
    ['Bob'],
    [None],
    ['Siri'],
    ['Pete'],
    [None]
]

def  my_hash_function(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)

    return sum_of_char%10

def add(value):
    index = my_hash_function(value)
    bucket = my_hash_set[index]
    if value not in bucket:
        bucket.append(value)

def contain(value):
    index = my_hash_function(value)
    bucket = my_hash_set[index]
    return  value in bucket

add('Stuart')
print(my_hash_set)
print("does  'Stuart' exist in the set?", contain('Stuart'))

