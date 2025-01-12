from collections import deque

rangBuoc = {
    "A": ["B", "C", "D"],
    "B": ["K"],
    "C": ["E"],
    "D": ["F", "G"],
    "E": [],
    "F": [],
    "G": ["H"],
    "H": [],
    "K": []
}

start = "A"
end = "H"
rrrr = [["TTPT", "TTK", "Danh Sach L"]]

def BFS(start, end, queue, rrrr):
    visited = set()
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        ttk_list = rangBuoc[current]  
        for item_ttk in ttk_list:
            queue.append(item_ttk)
        rrrr.append([current, ttk_list, list(queue)])
        if current == end:
            break

queue = deque([start])
BFS(start, end, queue, rrrr)

for row in rrrr:
    print(row[0].ljust(10), " ".join(row[1]).ljust(15), row[2])
