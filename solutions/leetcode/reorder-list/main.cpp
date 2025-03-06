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
  void reorderList(ListNode *head) {
    ListNode *fast = head;
    ListNode *slow = head;
    while (fast != nullptr && fast->next != nullptr) {
      fast = fast->next->next;
      slow = slow->next;
    }

    ListNode *node = slow->next;
    slow->next = nullptr;
    ListNode *prev = nullptr;
    while (node != nullptr) {
      ListNode *next = node->next;
      node->next = prev;
      prev = node;
      node = next;
    }

    while (prev != nullptr) {
      ListNode *n1 = head->next;
      ListNode *n2 = prev->next;
      head->next = prev;
      prev->next = n1;
      head = n1;
      prev = n2;
    }
  }
};
