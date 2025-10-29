*** FunctionalUnit_ReservationStation.py ***

Contains two classes, ReservationStation and ReservationEntry. ReservationStation is instantiated by specifying its ID and number of entries. Also has an attribute 'full', which signifies if the station is full or not (Boolean value).

Entries in reservation station are ReservationEntry objects, which have an attribute 'index', ranging from 0 to (number of entries - 1). Index cannot be edited or deleted. Other attributes are 'operation', 'operand 1', 'operand 2', 'source 1', 'source 2' and 'busy'. All these attributes are None by default. 

A new entry can be made by calling new_entry() function, with attributes as parameters specified in the order : operation, operand1, operand2, src1, src2, busy. If RS is not full, function returns index where this entry is created. If RS is full, it returns -1, indicating entry is not created.

An entry can be cleared by calling delete_entry() function with the entry index as parameter. This resets all attributes (except index) to None. 

Any field in an entry can be changed (except index) by calling function update_entry(), passing the entry index and a dict as parameters. Format of dict : {'Field Name' : New Field Value}. Editable field names : 'Operation', 'Operand 1', 'Operand 2', 'Source 1', 'Source 2', 'Busy'. Returns 0 if update is successful. Returns -1 if unsuccessful. 

is_full() returns a Boolean value indicating if RS is currently full or not. 

get_state() returns a dict with all details of the current state of RS. 
get_entry(i) returns a dict with the current attributes of the entry at index i. Empty dict implies index is out of range.