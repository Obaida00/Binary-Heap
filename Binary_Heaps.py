class Node(object):
    def __init__(self, data=None, parent=None):
        self.data = data
        self.parent = parent
        self.left_child = None
        self.right_child = None


class Min_heap(object):
    # TODO ->insert ->remove ->heapify ->length ->into_array
    def __init__(self, capacity):
        self.root = Node()
        self.capacity = capacity

    def length(self):
        l = 1
        curr = self.root
        while curr.left_child != None:
            curr = curr.left_child
            l += 1
        return l

    def insert(self, data):
        if self.root.data == None:
            self.root.data = data
            print('root', self.root.data)
        else:
            self.search()

    def search(self):
        print('search..L31')
        queue = [self.root]

        while queue:
            curr = queue.pop(0)
            print(curr.data)
            if curr.right_child == None:
                print('made it')
                return
            else:
                queue.append(curr.left_child)
                queue.append(curr.right_child)



h = Min_heap(10)
h.insert(2)
h.root.left_child = Node(3)
h.root.right_child = Node(5)
h.root.left_child.left_child = Node(8)
h.root.left_child.right_child = Node(7)
h.root.right_child.left_child = Node(9)

#                       __2__
#                      /     \
#                     3       5
#                    / \     / \
#                   8   7   9   ⨂
#                               ↑
#                            what am
#                          looking for
h.search()
#             for i in range(1, self.capacity):
#                 x = self.search(self.root, i)
#                 if x == None:
#                     print('30')
#                     x = Node(data)
# h.printLevelOrder()
#
#
# def search(self, as_root, level):
#     print('level', level)
#     if as_root == None:
#         return as_root
#
#     if level == 1:
#         return as_root
#     if level > 1:
#         self.search(as_root.left_child, level - 1)
#         self.search(as_root.right_child, level - 1)
#
#
# # Function to  print level order traversal of tree
# def printLevelOrder(self):
#     h = self.capacity
#
#     for i in range(1, h + 1):
#         self.printCurrentLevel(self.root, i)
#
#
# # Print nodes at a current level
# def printCurrentLevel(self, root, level):
#     if root is None:
#         return
#     if level == 1:
#         print(root.data, end=" ")
#     elif level > 1:
#         self.printCurrentLevel(root.left_child, level - 1)
#         self.printCurrentLevel(root.right_child, level - 1)
