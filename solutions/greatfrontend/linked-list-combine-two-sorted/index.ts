interface ListNode {
    val: number;
    next: ListNode | null;
}

export default function linkedListCombineTwoSorted(
    listA: ListNode | null,
    listB: ListNode | null,
): ListNode | null {
    const dummy: ListNode = { val: 0, next: null };
    let current = dummy;
    while (listA != null || listB != null) {
        if (listA == null) {
            current.next = listB;
            return dummy.next;
        }

        if (listB == null) {
            current.next = listA;
            return dummy.next;
        }

        if (listA.val < listB.val) {
            current.next = listA;
            listA = listA.next;
        } else {
            current.next = listB;
            listB = listB.next;
        }
        current = current.next;
    }
    return dummy.next;
}
