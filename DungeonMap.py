def PathFind(St, End, Map):
    Stack = [St]
    Way = set()
    Pos = 0
    Way.add(St)
    while Stack:
        Arr = Map.get(Stack[-1])
        if Arr:
            if Arr[Pos] == End:
                return True
            if Arr[Pos] not in Way:
                Stack.append(Arr[Pos])
                Way.add(Arr[Pos])
                Pos = 0
            else:
                Pos += 1
            if Pos == len(Arr):
                Stack.pop()
                Pos = 0
        else:
            Stack.pop()
    return False


DungLoc = str(input())
Map = dict()
MapR = dict()
while len(DungLoc.split()) != 1:
    LocSt, LocFin = DungLoc.split()
    Loc1 = Map.get(LocSt)
    Loc2 = Map.get(LocFin)
    if Loc1 == None or LocFin not in Map[LocSt]:
        Map[LocSt] = Loc1 + [LocFin] if Loc1 else [LocFin]
    if Loc2 == None or LocSt not in Map[LocFin]:
        Map[LocFin] = Loc2 + [LocSt] if Loc2 else [LocSt]
    DungLoc = str(input())

FinSt = DungLoc
FinEn = str(input())

Mes = "YES" if PathFind(FinSt, FinEn, Map) else "NO"
print(Mes)
