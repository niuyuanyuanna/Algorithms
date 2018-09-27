from queue import Queue


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def find_node(pre, tin, start_pre, end_pre, start_tin, end_tin):
    """
    中序遍历当前元素左边的是左子树元素，右边的是右子树元素
    前序遍历第一个元素即为根节点，根据中序遍历查找到左子树根节点及右子树根节点
    :param pre:
    :param tin:
    :param start_pre:
    :param end_pre:
    :param start_tin:
    :param end_tin:
    :return:
    """
    if start_pre > end_pre or start_tin > end_tin:
        return None
    tree_root = TreeNode(pre[start_pre])
    for i in range(start_tin, end_tin):
        if pre[start_pre] == tin[i]:
            tree_root.left = find_node(pre, tin, start_pre + 1, start_pre + i - start_tin, start_tin, i - 1)
            tree_root.right = find_node(pre, tin, start_pre + i - start_tin + 1, end_pre, i + 1, end_tin)
    return tree_root


def reconstruct_binaryTree(pre, tin):
    """
    根据前序遍历和中序遍历重建二叉树
    :param pre:
    :param tin:
    :return:
    """
    if pre is None or tin is None or len(pre) != len(tin):
        return -1
    start_pre = 0
    end_pre = len(pre) - 1
    start_tin = 0
    end_tin = len(tin) - 1
    find_node(pre, tin, start_pre, end_pre, start_tin, end_tin)


def get_next_treeNode_inSequence(tree_node):
    """
    找到当前节点中序遍历的下一节点
    分为两种情况：1.当前节点有右子节点，下一节点就是沿着当前右子节点子树的最左子节点
                 2.当前节点无右子节点，下一节点应为沿着其父节点查找，
                 直到找到一个祖先节点的左子节点为上一个查找的节点时，下一节点就是这个父节点
    :param tree_node:
    :return:
    """
    if tree_node is None:
        return tree_node
    ans_node = tree_node
    if ans_node.right is not None:
        while ans_node.right is not None:
            ans_node = ans_node.right
        return ans_node
    while ans_node.next is not None:
        par_node = ans_node.next
        if par_node.left == ans_node:
            return par_node
        ans_node = par_node
    return None


def is_the_same_tree(tree1, tree2):
    """
    递归判断两棵树是否相同
    :param tree1:
    :param tree2:
    :return:
    """
    if tree2 is None:
        return True
    if tree1 is None:
        return False
    if tree1.val == tree2.val:
        return is_the_same_tree(tree1.left, tree2.left) and is_the_same_tree(tree1.right, tree2.right)
    pass


def has_subTree(tree1, tree2):
    """
    递归判定第二克树是否是第一颗树的子树
    :param tree1:
    :param tree2:
    :return:
    """
    if tree1 is None or tree2 is None:
        return False
    return is_the_same_tree(tree1, tree2) or has_subTree(tree1.left, tree2) or has_subTree(tree1.right, tree2)


def mirror_binary_tree(tree_root):
    """
    递归调用本函数，依次对所有节点的左右子节点翻转
    :param tree_root:
    :return:
    """
    if tree_root is None:
        return tree_root
    if tree_root.left is not None and tree_root.right is not None:
        temp = tree_root.left
        tree_root.left = tree_root.right
        tree_root.right = temp
        mirror_binary_tree(tree_root.left)
        mirror_binary_tree(tree_root.right)


def is_symmetric_subbinaryTree(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    return is_symmetric_subbinaryTree(left.left, right.right) and is_symmetric_subbinaryTree(left.right, right.left)


def is_symmetric_binary_tree(tree_root):
    if tree_root is None:
        return True
    return is_symmetric_subbinaryTree(tree_root.left, tree_root.right)


def print_topToBottom(tree_root):
    if tree_root is None:
        return
    que_node = Queue()
    que_node.put(tree_root)
    next_level_node_num = 0
    print_num = 1
    node_level_list = []
    node_list = []
    while not que_node.empty():
        now_root = que_node.get()
        node_level_list.append(now_root.val)
        if now_root.left is not None:
            que_node.put(now_root.left)
            next_level_node_num += 1
        if now_root.right is not None:
            que_node.put(now_root.right)
            next_level_node_num += 1
        print_num -= 1
        if print_num == 0:
            node_list.append(node_level_list)
            node_level_list = []
            print_num = next_level_node_num
            next_level_node_num = 0
    print(node_list)


def visit_node(cur_node):
    print(cur_node.val)
    pass


def pre_traverse(tree_root):
    stack = []
    cur_node = tree_root
    while not cur_node is None or not len(stack) <= 0:
        while cur_node is not None:
            visit_node(cur_node)
            stack.append(cur_node)
            cur_node = cur_node.left
        if len(stack) > 0:
            temp = stack.pop()
            cur_node = temp.right


def in_traverse(tree_root):
    stack = []
    cur_node = tree_root
    while not cur_node is None or not len(stack) <= 0:
        while cur_node is not None:
            stack.append(cur_node)
            cur_node = cur_node.left
        if len(stack) > 0:
            tmp = stack.pop()
            visit_node(tmp)
            cur_node = tmp.right


def back_traverse(tree_root):
    """
    第一种思路：对于任一结点P，将其入栈，然后沿其左子树一直往下搜索，直到搜索到没有左孩子的结点，
    此时该结点出现在栈顶，但是此时不能将其出栈并访问，因此其右孩子还为被访问。
    所以接下来按照相同的规则对其右子树进行相同的处理，当访问完其右孩子时，该结点又出现在栈顶，此时可以将其出栈并访问。
    这样就保证了正确的访问顺序。在这个过程中，每个结点都两次出现在栈顶，只有在第二次出现在栈顶时，才能访问它。
    因此需要多设置一个变量标识该结点是否是第一次出现在栈顶。
    :param tree_root:
    :return:
    """
    stack = []
    cur_node = tree_root
    while not cur_node is None or not len(stack) <= 0:
        while cur_node is not None:
            cur_node.isFirst = True
            stack.append(cur_node)
            cur_node = cur_node.left
        if len(stack) >= 0:
            tmp = stack[-1]
            stack.pop()
            if tmp.isFirst:
                tmp.isFirst = not tmp.isFirst
                stack.append(tmp)
                cur_node = tmp.right
            elif tmp.isFirst == 2:
                visit_node(tmp)
                tmp = None


def height(root):
    if root is None:
        return 0
    height_left = height(root.left)
    height_right = height(root.right)
    if height_left > height_right:
        return height_left + 1
    else:
        return height_right + 1


def tree_distance(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 0
    dis = max(height(root.left) + height(root.right), tree_distance(root.left), tree_distance(root.right))
    return dis


if __name__ == '__main__':
    root_node = TreeNode(3)
    root_node.left = TreeNode(5)
    root_node.right = TreeNode(10)
    root_node.left.left = TreeNode(9)
    root_node.left.right = TreeNode(4)
    root_node.left.left.left = TreeNode(2)
    root_node.right.left = TreeNode(5)
    root_node.right.right = TreeNode(6)
    # pre_traverse(root_node)
    tree_distance(root_node)
