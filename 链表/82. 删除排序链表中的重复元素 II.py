"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中没有重复出现的数字。

返回同样按升序排列的结果链表。

示例 1：

输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：

输入：head = [1,1,1,2,3]
输出：[2,3]

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from list_ser_deser import ListNode, Codec


class Solution:
    def deleteDuplicates_bfs(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-101, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                val = cur.next.val
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

    #
    def deleteDuplicates_bfs_not_sorted(self, head: ListNode) -> ListNode:
        if not head:
            return None
        return head

    #
    def deleteDuplicates_dfs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        return head


if __name__ == '__main__':
    data1 = [1, 1, 2]
    data2 = [1, 1, 3, 3, 4]
    data3 = [1, 1, 2, 3, 3, 4, 6]
    deser = Codec()
    ser = Codec()
    head1 = deser.deserialize(data1)
    head2 = deser.deserialize(data2)
    head3 = deser.deserialize(data3)
    solution = Solution()

    res = solution.deleteDuplicates_bfs(head3)
    res_list = ser.serialize(res)
    print(res_list)

    # res2 = solution.deleteDuplicates_bfs_not_sorted(head1)
    # res2_list = ser.serialize(res2)
    # print(res2_list)
    #
    # res3 = solution.deleteDuplicates_dfs(head3)
    # res3_list = ser.serialize(res3)
    # print(res3_list)
