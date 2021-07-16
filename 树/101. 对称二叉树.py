"""
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树[1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3

但是下面这个[1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

进阶：

你可以运用递归和迭代两种方法解决这个问题吗？


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binaryTree_ser_deser import TreeNode, Codec


class Solution:
    def isSymmetric_iter(self, root: TreeNode) -> bool:
        nodes = [root]
        while nodes:
            val_layer = []
            node_next_layer = []
            for node in nodes:
                if not node:
                    val_layer.append(None)
                    continue
                val_layer.append(node.val)
                node_next_layer.append(node.left)
                node_next_layer.append(node.right)
            # 判断这一层节点值是否构成回文数组
            if val_layer != val_layer[::-1]:
                return False
            nodes = node_next_layer
        return True

    def isSymmetric_recur(self, root: TreeNode) -> bool:
        def check(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return left.val == right.val and check(left.left, right.right) and check(left.right, right.left)
        return check(root, root)


if __name__ == '__main__':
    deser = Codec()
    data1 = "1,2,2,3,4,4,3"
    data2 = "1,2,2,null,3,null,3,null,null"
    root1 = deser.bfs_deserialize(data1)
    root2 = deser.bfs_deserialize(data2)

    solution = Solution()
    res = solution.isSymmetric_iter(root2)
    res2 = solution.isSymmetric_recur(root2)
    print(res2)
    print("\nEND")