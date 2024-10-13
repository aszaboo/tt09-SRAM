/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_sram (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  // All output pins must be assigned. If not used, assign to 0.
  assign uo_out  = ui_in + uio_in;  // Example: ou_out is the sum of ui_in and uio_in
  assign uio_out = 0;
  assign uio_oe  = 0;


// Setup data for RAM Module

  wire [7:0] RAM_A; // Address Lines
  wire [7:0] RAM_D; // Data Lines
  wire [7:0] RAM_O; // Output Lines
  wire CS_n;
  wire WE_n;

  // ... instanciate ram module


  // Setup for the DM7404 Hex Inverting Gates
  wire [7:0] INV_O; // output lines of inverter

  hex_inverter inverter_array( .A(RAM_O), .Y(INV_O) );

  // Setup for Octal Bus Transceiver

  // Note: Not sure about the BUS inputs but for now making var
  wire [7:0] BT_B;
  wire CE;
  wire AtoB;

  bus_transceiver inverter_to_bus ( .OE_n(CE), .DIR(AtoB), .A(INV_O), .B(BT_B));

  // Not complete











  // List all unused inputs to prevent warnings
  wire _unused = &{ena, clk, rst_n, 1'b0};


  

endmodule
