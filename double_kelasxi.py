class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    
    # Insert di awal (prepend)
    def insert_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    # Insert di akhir (append)
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
            new_node.prev = last
    
    # Hapus node tertentu
    def delete_node(self, key):
        current = self.head
        
        # Jika node yang dihapus adalah head
        if current and current.data == key:
            self.head = current.next
            if self.head:  # Jika list tidak kosong setelah penghapusan
                self.head.prev = None
            current = None
            return
        
        # Cari node yang akan dihapus
        while current and current.data != key:
            current = current.next
        
        # Jika node tidak ditemukan
        if current is None:
            print(f"Data {key} tidak ditemukan")
            return
        
        # Update pointer prev dan next
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        current = None
    
    # Tampilkan dari depan ke belakang
    def display_forward(self):
        current = self.head
        print("Forward: ", end="")
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    
    # Tampilkan dari belakang ke depan
    def display_backward(self):
        if self.head is None:
            return
        
        # Pergi ke node terakhir
        last = self.head
        while last.next:
            last = last.next
        
        print("Backward: ", end="")
        while last:
            print(last.data, end=" <-> ")
            last = last.prev
        print("None")

# Contoh penggunaan
dll = DoubleLinkedList()
dll.insert_end(30) # 30
dll.insert_end(40) # 40
dll.insert_front(50) # 50
dll.insert_end(60) # 60
dll.insert_end(70) # 70
dll.insert_end(80) # 80
# TAMBAHKAN 5 INSERT END, ANGKA BEBAS

dll.display_forward()  # Output: 5 <-> 10 <-> 20 <-> 30 <-> None
dll.display_backward() # Output: 30 <-> 20 <-> 10 <-> 5 <-> None

dll.delete_node(70)
dll.display_forward()  # Output: 5 <-> 10 <-> 30 <-> None
