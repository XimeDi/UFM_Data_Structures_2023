from playList import DNode
from playList import Canciones
from playList import DLinkedList


dll = DLinkedList()

node_a = Canciones('1', 'Unravel', 'TK from Ling tosite sigure', 'Fantastic Magic')
dnode_a = DNode(node_a)
dll.insert(dnode_a)


node_b = Canciones(2, "Kaikai Kitan", "Eve", "Ao no Waltz")
node_c = Canciones(3, "Cry Baby", "Miura Jam", "Cry Baby (Tokyo Revengers)")
node_d = Canciones(4, "Black Catcher", "Vickeblanka", "Black Catcher")
node_e = Canciones(5, "Break in to break out", "Nordex", "Break in to break out (From Persona 5)")
node_f = Canciones(6, "Asphyxia", "Akano", "Asphyxia (From Tokyo Ghoul:Re)")
node_g = Canciones(7, "Blue Bird", "Akano", "Blue Bird (From Naruto Shippuden)")
node_h = Canciones(8, "Drops", "Hypnosis Mic D.R.B Fling Posse", "Fling Posse FPSM")
node_i = Canciones(9, "3$EVEN", "Hypnosis Mic D.R.B Fling Posse", "Fling Posse")
node_j = Canciones(10, "Shibuya Marbel Texture", "Hypnosis Mic D.R.B Fling Posse", "Fling Posse FPSM")


dnode_b = DNode(node_b)
dnode_c = DNode(node_c)
dnode_d = DNode(node_d)
dnode_e = DNode(node_e)
dnode_f = DNode(node_f)
dnode_g = DNode(node_g)
dnode_h = DNode(node_h)
dnode_i = DNode(node_i)
dnode_j = DNode(node_j)


dll.insert(dnode_b)
dll.insert(dnode_c)
dll.insert(dnode_d)
dll.insert(dnode_e)
dll.insert(dnode_f)
dll.insert(dnode_g)
dll.insert(dnode_h)
dll.insert(dnode_i)
dll.insert(dnode_j)


dll.print_list()






