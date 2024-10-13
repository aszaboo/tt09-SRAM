`ifndef HEX_INVERTER_V
`define HEX_INVERTER_V

module hex_inverter (
    input [7:0] A,
    output [7:0] Y
);

  assign Y = ~A;


endmodule

`endif HEX_INVERTER_V