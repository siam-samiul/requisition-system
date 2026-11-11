from requisition_system import Requisition
r1 = Requisition("03/04/2024", "FN19", "John Paul")
r1.add_requisition([("Pens", 200), ("Paper", 250)])
r1.approve_requisition()
print(r1.status, r1.approval_ref)