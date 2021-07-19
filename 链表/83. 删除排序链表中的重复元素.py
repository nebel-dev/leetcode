"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。

示例 1：

输入：head = [1,1,2]
输出：[1,2]
示例 2：

输入：head = [1,1,2,3,3]
输出：[1,2,3]

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from list_ser_deser import ListNode, Codec


class Solution:
    def deleteDuplicates_bfs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-101)
        tail = dummy
        while head:
            if tail.val != head.val:
                tail.next = head
                tail = tail.next
            head = head.next
        tail.next = None
        return dummy.next

    # 在无序的链表中删除重复的元素，先出现的被保留
    def deleteDuplicates_bfs_not_sorted(self, head: ListNode) -> ListNode:
        if not head:
            return None
        cur = head
        vals = [cur.val]
        while cur and cur.next:
            if cur.next.val in vals:
                cur.next = cur.next.next
            else:
                vals.append(cur.next.val)
                cur = cur.next
        return head

    # 遇到重复的元素，删除上一个元素
    def deleteDuplicates_dfs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates_dfs(head.next)
        if head.val == head.next.val:
            return head.next
        else:
            return head


if __name__ == '__main__':
    data1 = [1, 1, 2]
    data2 = [1, 1, 2, 3, 3]
    data3 = [6, 1, 1, 2, 3, 3, 4]
    deser = Codec()
    ser = Codec()
    head1 = deser.deserialize(data1)
    head2 = deser.deserialize(data2)
    head3 = deser.deserialize(data3)
    solution = Solution()

    # res = solution.deleteDuplicates_bfs(head2)
    # res_list = ser.serialize(res)
    # print(res_list)

    res2 = solution.deleteDuplicates_bfs_not_sorted(head1)
    res2_list = ser.serialize(res2)
    print(res2_list)

    res3 = solution.deleteDuplicates_dfs(head3)
    res3_list = ser.serialize(res3)
    print(res3_list)


