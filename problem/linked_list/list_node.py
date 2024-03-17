class ListNode:
    def __init__(self, elem):
        self.elem = elem
        self.next = None

    def __str__(self):
        res = []
        p = self
        while p is not None:
            res.append(p.elem)
            p = p.next
        return "->".join(map(str, res))

    @staticmethod
    def deserialize(s: str):
        if not s:
            return None
        s = s.split("->")
        head = ListNode(int(s[0]))
        p = head
        for i in range(1, len(s)):
            p.next = ListNode(int(s[i]))
            p = p.next
        return head

    def println(self):
        p = self
        while p is not None:
            print(p.elem, end="")
            if p.next is not None:
                print("->", end="")
            p = p.next
        print("")


if __name__ == "__main__":
    head = ListNode.deserialize("1->2->3->4->5")
    print(head)
    head.println()
