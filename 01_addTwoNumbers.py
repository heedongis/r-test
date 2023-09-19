'''
    두 개의 음수가 아닌 정수를 나타내는 Linked list 두 개가 제공됩니다. 숫자는 역순으로 저장되며 각 노드는 숫자 하나를 포함합니다.  두 숫자를 더한 값을 나타내는 Linked list를 반환하십시오.
    제약 조건
        • 숫자 0 자체를 제외하고 두 숫자는 0으로 시작하지 않습니다.
        • Linked list의 길이는 최대 1000입니다.
        • 각노드에는한자리정수N만저장됩니다.(0<=N<=9)
        • 문자열로 변환하지 않고 풀어야 합니다.
        • time-complexity O(n)으로 풀어야 합니다.
'''

from typing import Optional
# Definition for singly-linked list.
# Don't modify the class ListNode
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # write your code

        def rev_list(head: ListNode) -> ListNode:
            node, prev = head, None
            rev_int = ''
            # node.next를 이전 prev 리스트로 계속 연결하면 뒤집어진 연결 리스트를 얻을 수 있다.
            while node:
                next, node.next = node.next, prev
                prev, node = node, next

            while prev:
                rev_int += str(prev.val)
                prev = prev.next

            return rev_int

        # 역순의 LinkedList
        rev_l1 = rev_list(l1)
        rev_l2 = rev_list(l2)
        # 각 자리수에 대한 연산 결과를 저장할 변수
        carry = 0
        # 새로운 Linked list의 첫번째 노드
        head = ListNode()
        # 현재 노드
        curr = head
        # while rev_l1:
        #     print(rev_l1.val, end=" ")
        #     rev_l1 = rev_l1.next

        while l1 or l2 or carry:
            # 각 자리수에 대한 덧셈 연산 수행
            total = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            # 다음 자리수에 대한 연산 결과 계산
            carry = total // 10
            # 현재 자리수에 대한 연산 결과를 Linked list에 추가
            curr.next = ListNode(total % 10)
            # 현재 노드를 다음 노드로 이동
            curr = curr.next
            # 다음 자리수에 대한 연산을 위해 l1, l2를 다음 노드로 이동
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        next_node = head.next
        # 새로운 Linked list의 첫번째 노드를 반환
        output = [] # output value
        while next_node:
            print(next_node.val, end=" ")
            output.append(next_node.val)
            next_node = next_node.next

        print(rev_l1 + ' + ' + rev_l2 + ' = ' + str(int(rev_l1)+int(rev_l2)))

        return head.next

if __name__ == '__main__':
    # Solution().addTwoNumbers(l1=[5,3,1], l2=[3,2,6])
    # 입력값 생성
    l1 = ListNode(5, ListNode(3, ListNode(1)))
    l2 = ListNode(3, ListNode(2, ListNode(6)))

    # Solution 클래스의 인스턴스 생성
    sol = Solution()

    # addTwoNumbers 함수 호출
    result = sol.addTwoNumbers(l1, l2)