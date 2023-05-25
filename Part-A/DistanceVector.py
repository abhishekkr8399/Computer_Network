n = int(input("Enter the no of routers: "))
inf=999
class cell:
    def __init__(self):
        self.cost=0
        self.via = -1
routeTable = [[cell() for _ in range(n)] for _ in range(n)]
def build_route_table(node):
    for j in range(n):
        k=0
        while k<n and j!=node:
            if routeTable[node][j].cost!=inf:
                new_cost=routeTable[node][j].cost+routeTable[j][k].cost
                if routeTable[node][k].cost>new_cost:
                    routeTable[node][k].cost=new_cost
                    routeTable[node][k].via=routeTable[node][j].via
            k+=1
def find_path(i,j):
    print(chr(ord('A')+i))
    if i!=j:
        print("--> ")
        find_path(routeTable[i][j].via,j)
def disp_route_table(i):
    print("\nFinal routing table for ", chr(ord('A')+i))
    print("\nDestination\tCost\tOutgoing line")
    print("\n-----------\t----\t-------------\n")
    for j in range(n):
        print("\n",chr(ord('A')+j),"\t",routeTable[i][j].cost,"\t",chr(ord('A')+routeTable[i][j].via))
def read_route_table(nodes):
    print("Enter initial routing table (if no direct node enter 999: ")
    for i in range(nodes):
        print("Routing table for "+chr(ord('A')+i))
        for j in range(nodes):
            if i==j:
                routeTable[i][j].cost = 0
            else:
                routeTable[i][j].cost = int(input("-->"+chr(ord('A')+j))+"")
            if(routeTable[i][j].cost!=inf):
                routeTable[i][j].via = j
            else:
                routeTable[i][j].via = inf
def main():
    read_route_table(n)
    for i in range(n):
        build_route_table(i)
    for i in range(n):
        disp_route_table(i)
    cont=1
    while(cont):
        src = int(input("Enter the src node: "))
        dest = int(input("Enter the destination node:"))
        if src>=n or dest>=n:
            print("Router does not exist")
        else:
            find_path(src,dest)
            print("Cost of shortest route: ",routeTable[src][dest].cost)
        cont=int(input("Continue?(0/1) "))
main()