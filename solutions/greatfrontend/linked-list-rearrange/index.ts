interface ListNode {
  val: number;
  next: ListNode | null;
}

export default function rearrangeLinkedList(head: ListNode | null): void {
  if (!head) return;

  let fast: ListNode | null = head;
  let slow: ListNode | null = head;
  while (fast !== null && fast.next !== null) {
    fast = fast.next.next;
    slow = slow!.next;
  }

  let prev: ListNode | null = null;
  while (slow !== null) {
    const next = slow.next;
    slow.next = prev;
    prev = slow;
    slow = next;
  }

  let l1 = head;
  let l2 = prev;
  while (l2 != null && l2.next != null) {
    const l1Next = l1.next;
    l1.next = l2;
    l1 = l1Next!

    const l2Next = l2.next;
    l2.next = l1;
    l2 = l2Next;
  }
}

