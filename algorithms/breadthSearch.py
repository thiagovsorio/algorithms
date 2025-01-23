from collections import deque

graph = {}
graph['you'] = ['ali', 'bob', 'charles']
graph['bob'] = ['anuj', 'peggy']
graph['ali'] = ['peggy']
graph['anuj'] = []
graph['charles'] = ['thom', 'johny']
graph['peggy'] = []
graph['thom'] = []
graph['johny'] = []

search_queue = deque()
searched_people = deque()
search_queue += graph['you']

def person_is_johny(name):
    return name == 'johny'
    
while search_queue:
    person = search_queue.popleft()
    if not person in searched_people:
        if person_is_johny(person):
            print (person + ' is johny')
            break
        else:
            search_queue += graph[person]
            searched_people.append(person)
