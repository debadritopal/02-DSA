class MaxHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,num):
        self.heap.append(num)
        ind=len(self.heap)-1     
        if ind==0:
            return
        while self.heap[ind]>self.heap[(ind-1)//2] and ind>0:
            self.heap[ind],self.heap[(ind-1)//2]=self.heap[(ind-1)//2],self.heap[ind]
            ind=(ind-1)//2
    def extract_max(self):
        if len(self.heap)==0:
            return
        if len(self.heap)==1:
            return self.heap.pop()
        mini=self.heap.pop()
        maxi=self.heap[0]
        self.heap[0]=mini
        ind=0
        while ind*2+1<len(self.heap) and (self.heap[ind]<self.heap[2*ind+1] or self.heap[ind]<self.heap[2*ind+2]):
            if ind*2+2<len(self.heap):
                if self.heap[2*ind+1]>self.heap[2*ind+2]:
                    self.heap[2*ind+1],self.heap[ind]=self.heap[ind],self.heap[2*ind+1]
                    ind=ind*2+1
                else:
                    self.heap[2*ind+2],self.heap[ind]=self.heap[ind],self.heap[2*ind+2]
                    ind=ind*2+2
            else:
                self.heap[2*ind+1],self.heap[ind]=self.heap[ind],self.heap[2*ind+1]
                ind=ind*2+1
        return maxi
    def peek(self):
        if len(self.heap)==0:
            return
        return self.heap[0]
    def display(self):
        print(self.heap)
mh=MaxHeap()
mh.insert(90)
mh.insert(80)
mh.insert(70)
mh.insert(60)
mh.insert(50)
mh.insert(40)
mh.display()
print(mh.peek())
print(mh.extract_max())
mh.display()
print(mh.peek())