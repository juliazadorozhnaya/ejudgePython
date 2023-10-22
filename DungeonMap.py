"""
Вводится карта проходимых в обе стороны тоннелей подземлья в виде строк, содержащих разделённые пробелом названия двух
пещер, которые соединяет соответствующий тоннель. Две последние строки не содержат пробелов — это название входа в
подземелье и название выхода. Вывести "YES", если из входа можно попасть в выход, и "NO" в противном случае.
Пары могут повторяться или содержать одинаковые слова.

"""


def PathFind(St, End, Map):
    visited = set()
    stack = [St]

    while stack:
        current = stack[-1]
        if current == End:
            return True

        if current not in visited:
            visited.add(current)
            neighbors = Map.get(current, [])
            stack.extend(neighbor for neighbor in neighbors if neighbor not in visited)
        else:
            stack.pop()

    return False

Map = {}
while True:
    DungLoc = input()
    if len(DungLoc.split()) == 1:
        break
    LocSt, LocFin = DungLoc.split()
    Map.setdefault(LocSt, []).append(LocFin)
    Map.setdefault(LocFin, []).append(LocSt)

FinSt = DungLoc
FinEn = input()

if PathFind(FinSt, FinEn, Map):
    print("YES")
else:
    print("NO")
