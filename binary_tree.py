class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.item)


class BiTree(object):

    def __init__(self):
        self.root = Node('root')

    def add(self, item):
        node = Node(item)

        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)  # pop还是挺实用的，既可以取出元素，同时也可以删除它
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    q.append(pop_node.left)
                    q.append(pop_node.right)

    def get_parent(self, item):

        if self.root.item == item:
            return None

        tmp = [self.root]
        while tmp:
            pop_node = tmp.pop(0)
            if pop_node.left and pop_node.left == item:  # 先判断存在性，再判断是否相等
                return pop_node
            if pop_node.right and pop_node.right == item:  # 先判断存在性，再判断是否相等
                return pop_node
            if pop_node.left is not None:
                tmp.append(pop_node.left)
            if pop_node.right is not None:
                tmp.append(pop_node.right)

        return None

    # 一次默认删一个数据，不是把数里面的数据都删除
    def delete(self, item):
        if self.root is None:
            return False

        parent = self.get_parent(item)  # 上面写了这个函数就利用这个函数查找

        if parent:

            # 明确要删除的节点
            if parent.left.item == item:
                del_node = parent.left
            else:
                del_node = parent.right

            # 删除节点后的处理，主要是处理子节点的问题

            if del_node.left is None:  # del_node左子节点为空，所以注意处理右子节点
                # 如果要删除的item是他父节点的左子节点，同时删除的item的左子节点为空，那么直接把item的右子节点设置为父节点的左子节点
                if parent.left.item == item:
                    parent.left = del_node.right
                else:
                    parent.right = del_node.right
                del del_node  # 处理完之后再删除
                return True
            elif del_node.right is None:  # 同理，如果右子节点为空，则处理左子节点
                if parent.left.item == item:
                    parent.left = del_node.left
                else:
                    parent.right = del_node.left
                del del_node
                return True

            # 最麻烦的是两个子节点都不为空，两边都要处理
            # 虽然这里最后接上了，但是没有按照原来的规则，感觉不大好
            else:
                tmp_pre = del_node
                tmp_next = del_node.right
                if tmp_next.left is None:
                    # 替代
                    tmp_pre.right = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                else:
                    while tmp_next.left:  # 让tmp指向右子树的最后一个叶子
                        tmp_pre = tmp_next
                        tmp_next = tmp_next.left
                    # 替代
                    tmp_pre.left = tmp_next.right
                    tmp_next.left = del_node.left
                    tmp_next.right = del_node.right
                if parent.left.item == item:
                    parent.left = tmp_next
                else:
                    parent.right = tmp_next
                del del_node
                return True
        else:
            return False



