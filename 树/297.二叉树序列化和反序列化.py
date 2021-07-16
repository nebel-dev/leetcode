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

data = "1,2,null,null,3,4,null,null,5,null,null"  # 前序遍历
data2 = "null,null,2,null,null,4,null,null,5,3,1"  # 后序遍历
data3 = ""
data4 = "null,null,1"
data5 = "1,2,3,null,null,4,5,null,null,null,null"  # 层序遍历


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 前序遍历
class Codec:
    def serialize(self, root):  # 要求转化为字符串格式
        def dfs(root):
            if not root:
                return 'null,'
            left = dfs(root.left)
            right = dfs(root.right)

            return str(root.val) + ',' + left + right
        if not root:
            return ""
        return dfs(root)

    def deserialize(self, data):
        def dfs(data):
            val = data.pop(0)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = dfs(data)
            node.right = dfs(data)
            return node
        if not data:
            return None
        dataList = data.split(',')  # 将二叉树序列化后得到的字符串转化为数组
        print('dataList :', dataList)
        return dfs(dataList)


# 后序遍历
class Codec2:
    def serialize(self, root):  # 要求转化为字符串格式
        def dfs(root):
            if not root:
                return 'null,'
            left = dfs(root.left)
            right = dfs(root.right)
            return left + right + str(root.val) + ','
        if not root:
            return ''
        return dfs(root)

    def deserialize(self, data):
        def dfs(data):
            val = data.pop(0)
            if val == 'null':
                return None
            node = TreeNode(val)
            node.right = dfs(data)
            node.left = dfs(data)
            return node
        if not data:
            return None
        dataList = data.split(',')  # 将二叉树序列化后得到的字符串转化为倒序数组
        dataList.reverse()
        if not dataList[0]:
            dataList.pop(0)
        print('dataList :', dataList)
        return dfs(dataList)


# 中序遍历
# 中序遍历无法反序列化，因为无法确定root的位置
class Codec3:
    def serialize(self, root):
        def dfs(root):
            if not root:
                return 'null,'
            left = dfs(root.left)
            right = dfs(root.right)
            return left + str(root.val) + ',' + right
        if not root:
            return ''
        return dfs(root)


# 层序遍历
from collections import deque


class Codec4:
    def serialize(self, root):
        res = ""
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res = res + str(node.val) + ','
                queue.append(node.left)
                queue.append(node.right)
            else:
                res = res + 'null,'
        return res

    def deserialize(self, data):
        if not data:
            return None
        dataList = data.split(',')
        if dataList[-1] == '':
            dataList = dataList[:-1]
        print(dataList)
        root = TreeNode(int(    dataList.pop(0)))
        # queue = [root]
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if dataList:
                val = dataList.pop(0)
                if val != 'null':
                    node.left = TreeNode(int(val))
                    queue.append(node.left)
            if dataList:
                val = dataList.pop(0)
                if val != 'null':
                    node.right = TreeNode(int(val))
                    queue.append(node.right)
        return root


# 别人的代码，学习一下
class Codec5:
    def serialize(self, root):
        def f(r):
            return str(r.val) + ',' + f(r.left) + f(r.right) if r else ','
        return f(root)

    def deserialize(self, data):
        lis = data.split(',')[::-1]

        def f():
            val = lis.pop()
            return TreeNode(val, f(), f()) if val else None
        return f()


if __name__ == '__main__':
    '前序遍历'
    ser = Codec()
    deser = Codec()
    # ans = ser.serialize(deser.deserialize(data))
    # print('ans :', ans)
    # ans2 = deser.deserialize(ser.serialize(deser.deserialize(data)))

    '后序遍历'
    ser2 = Codec2()
    deser2 = Codec2()
    # ans = ser2.serialize(deser2.deserialize(data4))
    # print('ans :', ans)
    # ans2 = deser2.deserialize(ser2.serialize(deser2.deserialize(data2)))

    '中序遍历'
    ser3 = Codec3()
    # ans = ser3.serialize(deser.deserialize(data))
    # print('ans :', ans)

    '层序遍历'
    ser4 = Codec4()
    deser4 = Codec4()
    ans = ser4.serialize(deser4.deserialize(data5))
    print('ans :', ans)
    ans2 = deser4.deserialize(ans)

    print("\nEND")
