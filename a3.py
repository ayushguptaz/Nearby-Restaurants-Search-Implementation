class MaxHeap():
    def __init__(self):
        # Initialise it with empty lists , data 
        self.data = []
        # self.index_list=[]
        # Time complexity of function is  O(1)

    def parent(self, j):
        return (j-1)//2
        # returns position of parent node
        # Time complexity of function is  O(1)

    def left(self, j):
        return 2*j+1
        # returns position of left child node
        # Time complexity of function is  O(1)

    def right(self, j):
        return 2*j+2
        # returns position of right child node
        # Time complexity of function is  O(1)

    def has_left(self, j):
        return self.left(j) < len(self.data)
        # Time complexity of function is  O(1)

    def has_right(self, j):
        return self.right(j) < len(self.data)
        # Time complexity of function is  O(1)
    def insert_in_data(self, element):
        self.data.append(element)
        # Time complexity of function is  O(1)
    def max_child(self, i):
        if self.has_left(i):
            left = self.left(i)
            child = self.left(i)
            if self.has_right(i):
                right = self.right(i)
                if self.data[left] <= self.data[right]:
                    child = right
        else:
            child = i
        return child
        # Time complexity of function is  O(1)

  
    def heapUp(self, i):
        while ((i-1) // 2 >= 0):
            if self.data[i] >= self.data[(i-1) // 2]:
                self.data[i], self.data[(
                    i-1) // 2] = self.data[(i-1) // 2], self.data[i]
            i = (i-1) // 2
        # Time complexity of function is  O(log(n))
    def heapDown(self, i):
        if i+1 == len(self.data):
            return                
        while (i * 2) < len(self.data):
            max_c = self.max_child(i)
            if max_c == i:
                break
            if self.data[i] < self.data[max_c]:
                self.data[i], self.data[max_c] = self.data[max_c], self.data[i]
            i = max_c 
    def insert(self, element):
        self.data.append(element)
        self.heapUp(len(self.data)-1)
        # Time complexity of function is  O(log(n))
    def extract_max(self):

        self.data[0],self.data[-1]=self.data[-1],self.data[0]
        yyy=self.data.pop()
        self.heapDown(0)
        return yyy 


    def FastHeap(self):
        start = (len(self.data)-1)
        for j in range(start, -1, -1):
            self.heapUp(j) 
        hheaap = self.data
        return hheaap
def find_Max_nbr(L):
    max=L[0]
    for i in range (len(L)):
        if L[i]>max:
            max=L[i] 
    return max 


def findMaxCapacity(n,links,s,t):                                                                               
    wt_each_indx=[0 for i in range (n)]
    links = sorted(links, key=lambda item: item[2],reverse = True)
    

    # 0 for unvisited and 1 for visited 
    visited_=[0 for i in range (n)] 
    
    # adj_mat = [[0 for i in range(n)] for j in range(n)]
    adj_list= [ [] for j in range(n)]

    for i in range (len(links)):
        adj_list[links[i][0]]=adj_list[links[i][0]]+[(links[i][1],links[i][2])]
        adj_list[links[i][1]]=(adj_list[links[i][1]])+[(links[i][0],links[i][2])]
    Heap=MaxHeap()
    print(adj_list)
    # Buliding Heap of s nbrs first 

    for i in range (len(adj_list[s])):
        if visited_[adj_list[s][i][0]]!=1:
            Heap.insert_in_data((adj_list[s][i][1],adj_list[s][i][0]))
            wt_each_indx[adj_list[s][i][0]]=adj_list[s][i][1]
            #
            visited_[adj_list[s][i][0]]=1 

    Heap.FastHeap()
    # print(Heap.data)


    # Maximum nbr
    # A function that adds unvisited nbrs of vertex
    def add_uv_nbr(vertex,visited_):
        for i in range (len(adj_list[vertex])):
            if visited_[adj_list[vertex][i][0]]!=1:
                Heap.insert((adj_list[vertex][i][1],adj_list[vertex][i][0]))
                visited_[adj_list[vertex][i][0]]=1

 
    current_node=s
    # wt_each_indx[MaxHeap.data[0][1]]=MaxHeap.data[0][0]        
    # wt_each_indx[MaxHeap.data[0][1]]=MaxHeap.data[0][0]    
    # for i in     

    while current_node!=t:  
        # print(wt_each_indx)
        max_nbr_s=Heap.extract_max()
        

    # Previous node of max_nbr_s[1] 
        x1= wt_each_indx[max_nbr_s[1]]
        v1=wt_each_indx[current_node]
        v2=max_nbr_s[0] 

        if v1<v2 : 
            wt_each_indx[max_nbr_s[1]]=v1 
        else:
            wt_each_indx[current_node]= v2 
        if x1>wt_each_indx[max_nbr_s[1]]:
            wt_each_indx[max_nbr_s[1]]=x1

        current_node = max_nbr_s[1]                  
        add_uv_nbr(current_node,visited_)  
    print(wt_each_indx)      
    return wt_each_indx[s]
print(findMaxCapacity(4,[(0,1,30),(0,3,10),(1,2,40),(2,3,50),(0,1,60),(1,3,50)],0,3))
    