module d_register (
    input CLR,
    input CLK,
    input G1_n,
    input G2_n,
    input M,
    input N,
    input [3:0] D,
    output reg [3:0] Q
);

  // Internal storage register
  reg [3:0] storage;

  // Set initial value for storage register
  initial begin
    storage = 4'b0000;
  end

  // Asynchronous Clear Logic and High-Impedance Handling
  always @(*) begin
    if (CLR) begin
      Q = 4'b0000;  // Clear output immediately when CLR is asserted
    end else if (M || N) begin
      Q = 4'bzzzz;  // Set output to high-impedance if M or N is high
    end else begin
      Q = storage;  // Otherwise, output the stored value
    end
  end

  // Clock-Driven Data Load Logic
  always @(posedge CLK) begin
    if (!CLR && !G1_n && !G2_n) begin
      storage <= D;  // Load data into storage on positive clock edge if enabled
    end
  end

endmodule
