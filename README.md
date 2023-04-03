
## Adder

In this question, you will implement a Verilog module that adds two 3-bit input numbers and outputs their sum.

### Specifications

The Verilog module should have the following specifications:

- Name: `three_bit_adder`
- Inputs: 
  - `a`: 3-bit input number
  - `b`: 3-bit input number
- Outputs:
  - `sum`: 3-bit output number that is the sum of `a` and `b`

### Verilog Code Template

Here's a Verilog code template that you can use to implement the `three_bit_adder` module:

```verilog
module three_bit_adder (
  input [2:0] a,
  input [2:0] b,
  output [2:0] sum
);

// Add your code here

endmodule
```
### Task
Implement the `three_bit_adder` module according to the given specifications. Your Verilog code should be correct and syntactically valid. Make sure that your Verilog code uses proper formatting and indentation to ensure readability.

### Example
Here's an example of how the `three_bit_adder` module should work:

***Input:***
```
a = 011
b = 101
```
***Output***
```
sum = 000  (Carry out = 1)

```

***Explanation***
```
011 (a)
+ 101 (b)
-----
  000 (sum)
```

**Note that the result is `000` because we are working with 3-bit numbers and there is a carry out from the most significant bit.**
