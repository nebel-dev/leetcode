class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Codec:
    def serialize(self, head: ListNode) -> list:
        if not head:
            return []
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    def deserialize(self, data: list) -> ListNode:
        if not data:
            return None
        head = ListNode(data.pop(0))
        nodes = [head]
        while data:
            val = data.pop(0)
            node = nodes.pop()
            node.next = ListNode(val)
            nodes.append(node.next)
        return head


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    data1 = []
    ser = Codec()
    deser = Codec()

    ans = deser.deserialize(data)
    print(ser.serialize(ans))