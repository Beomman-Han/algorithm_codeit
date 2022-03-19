from typing import Iterator, Type, TypeVar

E = TypeVar('E')

class Node:
    """Node class for LinkedList element"""
    
    ## memory efficiency and restrict attributes
    __slots__ = ('_data', '_next')
    
    def __init__(self,
        data : E
        ) -> None:
        
        self.data = data
        self.next: Type['Node'] = None
        
        return

    ## data getter/setter (property)
    @property
    def data(self) -> E:
        return self._data
    
    @data.setter
    def data(self, data : E) -> None:
        self._data = data
        return
    
    ## next getter/setter (property)
    @property
    def next(self) -> Type['Node']:
        return self._next
    
    @next.setter
    def next(self, node : Type['Node']) -> None:
        self._next = node
        return
    

class LinkedList:
    """LinkedList class containing Node objects"""
    
    def __init__(self) -> None:
        
        self.head = None
        self.tail = None

        return
    
    def append(self, data : E) -> None:
        """Append method for adding element at linked list"""
        
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:  
            self.tail.next = new_node
            self.tail = new_node

        return
    
    def __getitem__(self, index : int) -> Type['Node']:
        """Get node by index"""
        
        print(index)
        iterator = self.head
        for _ in range(index):
            try:
                iterator = iterator.next
            except AttributeError:
                raise Exception('IndexError: index out of range')
        
        return iterator
    
    def __str__(self) -> str:
        """Special method for printing LinkedList object"""
        
        delimiter = '->'
        
        string = ''
        iterator = self.head
        while iterator is not None:
            string += f'{str(iterator.data)}->'
            iterator = iterator.next
        string += '*'
                        
        return string
    
if __name__ == '__main__':
    
    def main():
        
        ## init nodes
        head_node = Node(2)
        node_1 = Node(3)
        node_2 = Node(5)
        node_3 = Node(7)
        tail_node = Node(11)
        
        ## connect nodes
        head_node.next = node_1
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = tail_node
        
        ## print nodes
        iterator = head_node
        while iterator != None:
            print(iterator.data)
            iterator = iterator.next
        
        linked_list = LinkedList()
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(5)
        linked_list.append(7)
        
        iterator = linked_list.head
        while iterator is not None:
            print(iterator.data)
            iterator = iterator.next
        
        ## test __str__ method
        print(linked_list)
        
        ## test __getitem__ method
        print(linked_list[0].data)
        
        
        return
    
    main()