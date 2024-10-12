module bus_transceiver_8_bit (
    input OE_n, // Output enable (active low)
    input DIR, // Direction control (0: B to A, 1: A to B)
    inout [7:0] A, // Port A (8-bits)
    inout [7:0] B // Port B (8-bits)
);

  assign A = ~OE_n ? (~DIR ? B : A) : 8'bz;
  assign B = ~OE_n ? (DIR ? A : B) : 8'bz;

endmodule