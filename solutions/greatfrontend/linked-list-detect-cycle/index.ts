interface ListNode {
  val: number;
  next: ListNode | null;
}

export default function linkedListDetectCycle(head: ListNode | null): boolean {
  let fast = head;
  let slow = head;

  while (fast != null && fast.next != null) {
    fast = fast.next.next;
    slow = slow!.next;
    if (fast == slow) {
      return true;
    }
  }

  return false;
}
