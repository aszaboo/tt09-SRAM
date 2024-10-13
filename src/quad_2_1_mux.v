module quad_2_1_mux (
    input wire strobe,
    input wire select,
    input wire [3:0] A,
    input wire [3:0] B,
    output wire [3:0] Y
);

  wire enable;
  assign enable = ~strobe;
  

  // MUX logic
  assign Y = enable ? (select ? B : A) : 4'b0000;

endmodule