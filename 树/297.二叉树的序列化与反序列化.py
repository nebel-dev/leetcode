"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，
采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个
字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这
个问题。

示例 1：

输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：

输入：root = [1,2]
输出：[1,2]

提示：

树中结点数在范围 [0, 104] 内
-1000 <= Node.val <= 1000


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

root1 = [1, 2, 3, None, None, 4, 5]
root2 = []
root3 = [1]
root4 = [1, 2]
root5 = [1, 2, None, None, 3, 4, None, None, 5, None, None]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 先序遍历
class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if not root:
                return 'null,'
            left = dfs(root.left)
            right = dfs(root.right)
            return str(root.val) + ',' + left + right
        return dfs(root)
        # if not root:
        #     return [None]
        # left_tree = self.serialize(root.left)
        # right_tree = self.serialize(root.right)
        # return str([root.val] + left_tree + right_tree)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs(data):
            val = data.pop(0)

            if val == 'null':
                return None
            node = TreeNode(val)
            node.left = dfs(data)
            node.right = dfs(data)

            return node
        # data_list = data.split(',')
        return dfs(data)
        # root_val = data_list.pop(0)
        # if root_val == None:
        #     return None
        # root = TreeNode(root_val)
        # root.left = self.deserialize(data_list)
        # root.right = self.deserialize(data_list)
        # return root


# 中序遍历
class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


# 后序遍历
class Codec3:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


# 层序遍历
class Codec4:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


# Your Codec object will be instantiated and called as such:
if __name__ == "__main__":
    # data_list = eval(data5)
    ser = Codec1()
    deser = Codec1()
    # ans = deser.deserialize(ser.serialize(root5))
    # ans = ser.serialize(deser.deserialize(root5))
    root = deser.deserialize(root1)
