"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意:合并必须从两个树的根节点开始。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binaryTree_ser_deser import TreeNode, Codec


class Solution:
    def mergeTrees_recur_pre(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode(0)
        root.val = root1.val + root2.val
        root.left = self.mergeTrees_recur_pre(root1.left, root2.left)
        root.right = self.mergeTrees_recur_pre(root1.right, root2.right)
        return root

    def mergeTrees_recur_in(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        root = TreeNode(0)
        root1.left = self.mergeTrees_recur_in(root1.left, root2.left)
        root.val = root1.val + root2.val
        root1.right = self.mergeTrees_recur_in(root1.right, root2.right)
        return root

    def mergeTrees_bfs(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1

        nodes1 = [root1]
        nodes2 = [root2]
        root = root1
        while nodes1 and nodes2:
            root1 = nodes1.pop(0)
            root2 = nodes2.pop(0)
            root1.val += root2.val

            if not root1.left:
                root1.left = root2.left
            elif root1.left and root2.left:
                nodes1.append(root1.left)
                nodes2.append(root2.left)

            if not root1.right:
                root1.right = root2.right
            elif root1.right and root2.right:
                nodes1.append(root1.right)
                nodes2.append(root2.right)
        return root


if __name__ == '__main__':
    data1 = "1,3,2,5"
    data2 = "2,1,3,null,4,null,7"
    deser = Codec()
    ser = Codec()
    root1 = deser.bfs_deserialize(data1)
    root2 = deser.bfs_deserialize(data2)

    solution = Solution()
    # pre
    ans_pre = solution.mergeTrees_recur_pre(root1, root2)
    ans_str_pre = ser.bfs_serialize(ans_pre)
    print(ans_str_pre)

    # in
    # ans_in = solution.mergeTrees_recur_in(root1, root2)
    # ans_str_in = ser.bfs_serialize(ans_in)
    # print(ans_str_in)

    # bfs
    ans_bfs = solution.mergeTrees_bfs(root1, root2)
    ans_str_bfs = ser.bfs_serialize(ans_bfs)
    print(ans_str_bfs)


