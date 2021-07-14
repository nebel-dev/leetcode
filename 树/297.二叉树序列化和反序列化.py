root1 = [1, 2, 3, None, None, 4, 5]
root2 = []
root3 = [1]
root4 = [1, 2]
root5 = [1, 2, None, None, 3, 4, None, None, 5, None, None]
data = "1,2,null,null,3,4,null,null,5,null,null,"

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):  # 要求转化为字符串格式
        def dfs(root):
            if not root:
                return 'null,'
            left = dfs(root.left)
            right = dfs(root.right)

            return str(root.val) + ',' + left + right
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
        dataList = data.split(',')  # 将二叉树序列化后得到的字符串转化为数组
        print('dataList :', dataList)
        return dfs(dataList)
if __name__ == '__main__':
    root = TreeNode(1)
    ser = Codec()
    deser = Codec()
    # tree = ser.serialize(root)
    # print(tree)
    root = deser.deserialize(data)
    print(root)

    ans = ser.serialize(deser.deserialize(data))
    print('ans :', ans)
    ans2 = deser.deserialize(ser.serialize(deser.deserialize(data)))
    print(ans2)
    print(root == ans2)
