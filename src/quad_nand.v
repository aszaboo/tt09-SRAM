`ifndef QUAD_NAND_V
`define QUAD_NAND_V

module quad_nand (
    input [3:0] a,
    input [3:0] b,
    output [3:0] y
);


assign y = ~(a & b);

endmodule

`endif QUAD_NAND_V

