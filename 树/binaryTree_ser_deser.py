from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 序列化：将树转化为字符串
# 反序列化：将字符串转化为树
class Codec:
    # 前序遍历
    def pre_serialize(self, root):
        def dfs(root):
            if not root:
                return 'null,'
            left = dfs(root.left)
            right = dfs(root.right)
            return str(root.val) + ',' + left + right
        if not root:
            return ''
        return dfs(root)[:-1]

    def pre_deserialize(self, data):
        def dfs(data):
            val = data.pop(0)
            if val != 'null':
                node = TreeNode(int(val))
            else:
                return None
            node.left = dfs(data)
            node.right = dfs(data)
            return node
        if not data:
            return None
        dataList = data.split(',')
        return dfs(dataList)

    # 中序遍历
    def in_serialize(self, root):
        def dfs(root):
            if not root:
                return 'null,'
            left = dfs(root.left)
            right = dfs(root.right)
            return left + str(root.val) + ',' + right
        if not root:
            return ''
        return dfs(root)[:-1]

    # 后序遍历
    def post_serialize(self, root):
        def dfs(root):
            if not root:
                return 'null,'
            left = dfs(root.left)
            right = dfs(root.right)
            return left + right + str(root.val) + ','
        if not root:
            return ''
        return dfs(root)[:-1]

    def post_deserialize(self, data):
        def dfs(data):
            val = data.pop(0)
            if val != 'null':
                node = TreeNode(int(val))
            else:
                return None
            node.right = dfs(data)
            node.left = dfs(data)
            return node
        if not data:
            return None
        dataList = data.split(',')
        dataList.reverse()
        # if dataList[0] == '':
        #     dataList.pop(0)
        return dfs(dataList)

    # 层序遍历
    def bfs_serialize(self, root):
        if not root:
            return ''
        res = ''
        nodes = deque()
        nodes.append(root)
        while nodes:
            node = nodes.popleft()
            if not node:
                res += 'null,'
            else:
                res += str(node.val) + ','
                nodes.append(node.left)
                nodes.append(node.right)
        return res[:-1]

    def bfs_deserialize(self, data):
        if not data:
            return None
        dataList = data.split(',')
        # if not dataList[-1]:
        #     dataList = dataList[:-1]
        root = TreeNode(int(dataList.pop(0)))
        nodes = deque()
        nodes.append(root)
        while nodes:
            node = nodes.popleft()
            if dataList:
                val = dataList.pop(0)
                if val != 'null':
                    node.left = TreeNode(int(val))
                    nodes.append(node.left)
            if dataList:
                val = dataList.pop(0)
                if val != 'null':
                    node.right = TreeNode(int(val))
                    nodes.append(node.right)
        return root


if __name__ == '__main__':
    data = "1,2,null,null,3,4,null,null,5,null,null"  # 前序遍历
    data2 = "null,null,2,null,null,4,null,null,5,3,1"  # 后序遍历
    data3 = ""
    data4 = "null,null,1"
    data5 = "1,2,3,null,null,4,5,null,null,null,null"  # 层序遍历

    ser = Codec()
    deser = Codec()

    '前序遍历'
    pre_ser = ser.pre_serialize(deser.pre_deserialize(data))
    print('pre  :', pre_ser)
    pre_deser = deser.pre_deserialize(pre_ser)

    '后序遍历'
    post_ser = ser.post_serialize(deser.post_deserialize(data2))
    print('post :', post_ser)
    post_deser = deser.post_deserialize(post_ser)

    '中序遍历'
    in_ser = ser.in_serialize(deser.pre_deserialize(data))
    print('in   :', in_ser)

    '层序遍历'
    bfs_ser = ser.bfs_serialize(deser.bfs_deserialize(data5))
    print('bfs  :', bfs_ser)
    bfs_deser = deser.bfs_deserialize(bfs_ser)
