class Requisition:
    counter = 1              #shared by All requisitioons 
    all_requisitions = []    #used later for display and statistics
    
    def __init__(self, date, staff_id, staff_name):
        self.name = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisitions_id = Requisition.counter + 10000
        Requisition.counter += 1
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"
        Requisition.all_requisitions.append(self)
    def add_requisition(self,items):
        for name, cost in items:
            if cost < 0:
                print(f"Invalid cost for {name} , skipped")
                continue
            self.items.append((name,cost))
            self.total += cost
        return self.total
    def approve_requisition(self):
        if self.total <= 0:
            self.status = "pending"
        elif self.total < 500:
            self.status = "Approved"
            self.approval_ref = self.staff_id +str(self.requisitions_id)[-3:]
        else:
            self.status = "Pending"
        return self.status