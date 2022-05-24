from collections import deque

# поиск в ширину
graph = {
    'Sveta': [
        'Leila',
        'Arshavir',
        'Dima'
    ],
    'Dima': [
        'Liuba',
        'Vadim'
    ],
    'Leila': [
        'Alexander',
        'Galina'
    ]
}

def is_seller(person):
    return len(person) == 9


people_to_search = deque()
people_to_search += graph['Sveta']

def find_sellers(people_to_search):
    searched = set()
    while people_to_search:
        person = people_to_search.popleft()
        if person not in searched:
            if is_seller(person):
                return f'{person} is a seller'
            else:
                if person_neighbours := graph.get(person):
                    people_to_search += person_neighbours
                searched.add(person)
    return 'no sellers'


if __name__ == '__main__':
    print(find_sellers(people_to_search))
