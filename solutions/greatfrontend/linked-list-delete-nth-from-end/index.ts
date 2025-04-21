interface ListNode {
    val: number;
    next: ListNode | null;
}

export default function deleteNthNodeFromEnd(
    head: ListNode | null,
    n: number,
): ListNode | null {
    let first = head;
    while (n > 0 && first != null) {
        first = first.next;
        n--;
    }

    const dummy: ListNode = { val: 0, next: head };
    let second: ListNode | null = dummy;
    while (first != null && second != null) {
        first = first.next;
        second = second.next;
    }

    if (second != null && second.next != null) {
        second.next = second.next.next;
    }

    return dummy.next;
}
