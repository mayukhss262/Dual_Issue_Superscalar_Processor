class ReservationEntry:

    def __init__(self, i, op, op1, op2, s1, s2, b):
        self.index = i
        self.busy = b
        self.operation = op
        self.op_1 = op1
        self.op_2 = op2 
        self.src_1 = s1
        self.src_2 = s2

    def clear(self):
        
        self.busy = False
        self.operation = None
        self.op_1 = None 
        self.op_2 = None 
        self.src_1 = None
        self.src_2 = None 

    def update_fields(self, updates):

        ret = None
        for k in updates:
            if k == 'Operation':
                self.operation = updates[k]
                ret = 0
            elif k == 'Operand 1':
                self.op_1 = updates[k]
                ret = 0
            elif k == 'Operand 2':
                self.op_2 = updates[k]
                ret = 0
            elif k == 'Source 1':
                self.src_1 = updates[k]
                ret = 0
            elif k == 'Source 2':
                self.src_2 = updates[k]
                ret = 0
            elif k == 'Busy':
                self.busy = updates[k]
                ret = 0
            else:
                ret = -1
        return ret
            
class ReservationStation:

    def __init__(self, id, n):
        self.id = id
        self.total_entries = n
        self.entries = []
        for k in range(n):
            self.entries.append(ReservationEntry(k, None, None, None, None, None, None))
        self.full = False
        
    def new_entry(self, operation, op_1, op_2, src_1, src_2, busy):

        if self.full == False:
            index = None
            for e in self.entries:
                if e.operation is None:
                    e.op_1 = op_1
                    e.op_2 = op_2
                    e.src_1 = src_1
                    e.src_2 = src_2
                    e.busy = busy 
                    e.operation = operation
                    index = e.index
                    break
            
            num_entries = 0
            for entry in self.entries:
                if entry.operation is not None:
                    num_entries = num_entries + 1

            if num_entries == self.total_entries:
                self.full = True
            else:
                self.full = False
            return index #sucess
        else:
            return -1 #failure  

    def delete_entry(self, i):
         
        for entry in self.entries:
            if entry.index == i:
                entry.clear()
                return 0
            else:
                return -1
    
    def update_entry(self, i, updates):

        # updates is a dict with format {field : newvalue}
        # Fields : 'Operation' , 'Busy', 'Operand 1', 'Operand 2', 'Source 1', 'Source 2'
        for entry in self.entries:
            if entry.index == i:
                ret = entry.index.update_fields(updates)
                return ret
            else:
                return -1
    
    def is_full(self):
        return self.full
    
    def get_state(self):

        state={}
        state['RSID'] = self.id
        state['Capacity'] = self.num_entries
        state['Entries'] = {}
        for entry in self.entries:
            state['Entries'][entry.index] = {}
            state['Entries'][entry.index]['Operation'] = entry.operation
            state['Entries'][entry.index]['Operand 1'] = entry.op_1
            state['Entries'][entry.index]['Operand 2'] = entry.op_2
            state['Entries'][entry.index]['Source 1'] = entry.src_1
            state['Entries'][entry.index]['Source 2'] = entry.src_2
            state['Entries'][entry.index]['Busy'] = entry.busy

        state['Full'] = self.full 
        return state 

    def get_entry(self, i):

        entry_info = {}
        for entry in self.entries:
            if entry.index == i:
                entry_info['Operation'] = entry.operation
                entry_info['Operand 1'] = entry.op_1
                entry_info['Operand 2'] = entry.op_2
                entry_info['Source 1'] = entry.src_1
                entry_info['Source 2'] = entry.src_2
                entry_info['Busy'] = entry.busy
                break 
        
        return entry_info
