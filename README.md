# quant
Quant is a proof-of-concept Python package for detecting 'kind-of-quantity' errors in Python code.  
Expressions are 'annotated' with their 'kind-of-quantity' names, allowing Quant to flag Type 1 KOQ errors.  
It achieves this by maintaining a simple dictionary of names that it uses to check the operands of an addition or subtraction.  
Quant also allows KOQ relations to be declared which it uses to detect Type 2 KOQ errors.  
Detecting Type 2 errors is more complex, and requires both a dictionary of relations, and run-time interception of mathematical operations 
to record both the operators and their operands. 
On completion, Quant compares the expression executed with the dictionary of relations and flags any mismatch (i.e., a Type 2 KOQ error).  
Quant's expression comparison is currently simplistic, and can be fooled. 
A more robust implementation would need to be able to simplify and/or re-arrange expressions to recognise equivalence in more complex cases.
Similarly, Quant only supports basic arithmetic operators at this time, but it could be extended to cater for additional operators and 
functions.
