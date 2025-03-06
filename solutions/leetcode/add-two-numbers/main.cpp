// Definition for singly-linked list.
struct ListNode {
  int val;
  ListNode *next;
  ListNode() : val(0), next(nullptr) {}
  ListNode(int x) : val(x), next(nullptr) {}
  ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
  ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode dummy(0);
    ListNode *node = &dummy;
    int carry = 0;
    while (l1 != nullptr || l2 != nullptr || carry != 0) {
      int v1 = (l1 != nullptr) ? l1->val : 0;
      int v2 = (l2 != nullptr) ? l2->val : 0;

      int total = v1 + v2 + carry;
      int remainder = total % 10;
      carry = total / 10;
      node->next = new ListNode(remainder);

      node = node->next;
      l1 = (l1 != nullptr) ? l1->next : nullptr;
      l2 = (l2 != nullptr) ? l2->next : nullptr;
    }

    return dummy.next;
  }
};
