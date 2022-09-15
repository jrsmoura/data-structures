from binary_trees.tree import Node, Tree
from linked_lists.linked_lists import Node, LinkedList


def main():
    # node = Node(10)

    # A rede é do tipo binária, então os maiores valores ficam a direita
    # enquanto os menores, a esquerda.
    # node.left = Node(5)
    # node.right = Node(10)
    #
    # node.left.left = Node(2)
    # node.left.right = Node(6)
    #
    # node.right.left = Node(13)
    # node.right.right = Node(20)

    # print(node.data)
    # print(node.right.right.data)

    # my_tree = Tree(node, "My Tree")
    #
    # print(my_tree.name)
    # print(my_tree.root.left.data)
    # print(my_tree.root.right.right.data)
    #
    # found = my_tree.search(220)
    # print(found)

    # tree = Tree(Node(50), "Transversal Tree")
    # tree.root.left = Node(25)
    # tree.root.right = Node(75)
    # tree.root.left.left = Node(10)
    # tree.root.left.right = Node(35)
    # tree.root.left.right.left = Node(30)
    # tree.root.left.right.right = Node(42)
    # tree.root.left.left.left = Node(5)
    # tree.root.left.left.right = Node(13)
    # tree.root.left.left.left.left = Node(2)
    #
    # print("Transverse Pre-Order")
    # tree.transverse_pre_order()
    #
    # print("Transverse In-Order")
    # tree.transverse_in_order()
    #
    # print("Transverse Post-Order")
    # tree.transverse_post_order()
    #
    # print("="*20)
    # print(tree.height())
    #
    # tree = Tree(Node(50), "Árvore apenas com a raiz")
    # print(tree.height())

    llist = LinkedList()
    # Iniciamos com a criação do head
    llist.head = Node(2)
    second = Node(3)
    third = Node(4)
    # linkamos o primeiro node com o segundo
    llist.head.next = second
    # linkamos o primeiro node com o terceiro
    second.next = third

    # insere um novo dado no início da lista
    llist.push(1)

    # insere um novo dado após o no second
    llist.insert_after(second, 33)

    # insere um novo dado ao final da lista
    llist.append(99)

    datas = llist.print_list()
    print(datas)


if __name__ == "__main__":
    main()
