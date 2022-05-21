# ==============================================================================
# * Graph BFS
# ! Time Complexity - O(V+E) -> V - vertices, E - edges
# ==============================================================================

graph = {
    "tahseen": ["tanshit", "nashit"],
    "nashit": ["areeba", "warisa"],
    "manu": ["azka"],
    "tanshit": [],
    "areeba": ["manu", "tahseen"],
    "numa": ["zehran"],
}


def is_person(person):
    return "m" in person.lower()


def bfs(name):
    queue = graph.get(name, [])
    searched = set()
    while queue:
        person = queue.pop(0)
        print("current person", person)
        if person in searched:
            continue

        if is_person(person):
            print("Person Found")
            return True

        connections = graph.get(person, [])
        if connections:
            queue.extend(connections)
        searched.add(person)
    print("Person not found")
    return False


bfs("tahseen")
