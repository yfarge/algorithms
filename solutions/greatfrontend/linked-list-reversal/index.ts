interface ListNode {
    val: number;
    next: ListNode | null;
}

export default function reverseLinkedList(
    head: ListNode | null,
): ListNode | null {
    let prev: ListNode | null = null;
    while (head != null) {
        const next = head.next;
        head.next = prev;
        prev = head;
        head = next;
    }

    return prev
}
