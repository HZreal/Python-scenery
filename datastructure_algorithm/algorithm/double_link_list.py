# -*- coding:utf-8 -*-
"""
 @author: huang
 @date: 2024-04-18
 @File: linkList.py
 @Description: 
"""


class ApprovalNode:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.prev = None

    def approve(self):
        if self.next:
            return self.next
        else:
            print(f"Approval complete. Final approval by: {self.name}")
            return None

    def reject(self):
        if self.prev:
            print(f"Rejected by {self.name}. Returning to {self.prev.name}")
            return self.prev
        else:
            print("Rejection at first step, cannot return further.")
            return None


class ApprovalChain:
    def __init__(self, start_node):
        self.current_node = start_node

    def start(self):
        while self.current_node:
            decision = input(f"Approve/Reject at {self.current_node.name}? (approve/reject): ")
            if decision.lower() == 'approve':
                self.current_node = self.current_node.approve()
            elif decision.lower() == 'reject':
                self.current_node = self.current_node.reject()


# Create nodes
hr = ApprovalNode("Human Resources")
comp_dept = ApprovalNode("Comprehensive Department")
ceo = ApprovalNode("CEO")

# Link nodes
hr.next = comp_dept
comp_dept.prev = hr
comp_dept.next = ceo
ceo.prev = comp_dept

# Create and run approval chain
chain = ApprovalChain(hr)
chain.start()
