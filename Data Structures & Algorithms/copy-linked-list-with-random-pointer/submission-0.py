"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        result = collections.defaultdict(lambda: Node(0))
        result[None] = None

        cur = head
        while cur:
            result[cur].val = cur.val
            result[cur].next = result[cur.next]
            result[cur].random = result[cur.random]
            cur = cur.next
        return result[head]

        