import sys

class MinHeap:

	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.size = 0
		self.Heap = [0]*(self.maxsize + 1)
		self.Heap[0] = -1 * sys.maxsize
		self.FRONT = 1

	def heap_parent(self, pos) :
		return pos // 2

	def heap_left_child(self, pos) :
		return (2 * pos)

	def heap_right_child(self, pos) :
		return (2 * pos) + 1

	def is_Heap_Leaf(self, pos) :
		if pos >= (self.size // 2 ) and pos <=self.size:
			return True
		return False
	
	def swap(self, first_pos, second_pos):
		self.Heap[first_pos], self.Heap[second_pos] = self.Heap[second_pos], self.Heap[first_pos]

	def heapify(self,pos):
		smallest = pos
		left_child = 2 * pos
		right_child =  2 * pos + 1
		if self.Heap[pos] > self.Heap[left_child] and left_child <= self.size :
			smallest = left_child
		if self.Heap[pos] > self.Heap[right_child] and right_child <= self.size :
			smallest = right_child
		if smallest != pos :
			self.Heap[pos] , self.Heap[smallest] = self.Heap[smallest] , self.Heap[pos]
			self.heapify(pos)

	def insert(self, element):
		self.size+= 1
		self.Heap[self.size] = element
		pos = self.size
		while self.Heap[pos] < self.Heap[self.heap_parent(pos)] :
			self.swap(pos,self.heap_parent(pos))
			pos = self.heap_parent(pos)

	def Print(self):
		for i in range(1, (self.size + 1)):
			print(self.Heap[i])
	
	def remove(self):
		popped = self.Heap[self.FRONT]
		self.Heap[self.FRONT] = self.Heap[self.size]
		self.size = self.size -  1
		for pos in range(self.size//2, 0, -1):
			self.heapify(pos)
		return popped

#heap = MinHeap(100)
#ar = [2,6931,556,9,10,11,6014,1,22,8,88,40,24,36,75,888,14]
#heap_ar= []

#for i in ar :
#	heap.insert(i)
	
#for i in range(len(ar)):
#	heap_ar.append(heap.remove())

#print(heap_ar)
