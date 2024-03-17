class TreeNode():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return " ".join(map(str, self.get_pre_list()))
    
    def print_tree(self):
        return self.__str__()

    def get_pre_list(self):
        """得到前序遍历列表"""
        if self.left is None and self.right is None:
            return [self.val, "^", "^"]
        elif self.left is None:
            return [self.val, "^", *self.right.get_pre_list()]
        elif self.right is None:
            return [self.val, *self.left.get_pre_list(), "^"]

        return [self.val, *self.left.get_pre_list(), *self.right.get_pre_list()]

    @staticmethod
    def deserialize(pre_list):
        """前序遍历序列转化为树"""

        def core(pre_list, index):
            """
            Args:
                pre_list: 前缀序列
                index: 树开始位置

            Returns:
                tree: 前缀序列所表示的树
                index: 树结束位置
            """
            if index >= len(pre_list):
                return None, -1

            root = None
            if pre_list[index] != '^':
                root = TreeNode(pre_list[index])
                root.left, index = core(pre_list, index + 1)
                root.right, index = core(pre_list, index + 1)

            return root, index

        root, _ = core(pre_list, 0)
        return root


if __name__ == "__main__":
    s = [5, 3, 2, '^', '^', 4, '^', '^', 7, 6, '^', '^', 8, '^', '^']
    tree = TreeNode.deserialize(s)

    print(tree)