import cocotb
from cocotb.triggers import RisingEdge, Timer

async def clock_generator(clk):
    """Generate a clock signal with a period of 20 ns."""
    while True:
        clk.value = 0
        await Timer(10, units='ns')
        clk.value = 1
        await Timer(10, units='ns')

@cocotb.test()
async def test_dregister(dut):
    """Test the '173/'LS173A register functionality based on the truth table, with G1_n and G2_n inversed"""

    # Start the clock generator
    cocotb.fork(clock_generator(dut.CLK))

    # Initialize signals
    dut.CLR.value = 0
    dut.G1_n.value = 1
    dut.G2_n.value = 1
    dut.M.value = 0
    dut.N.value = 0
    dut.D.value = 0b0000

    await RisingEdge(dut.CLK)  # Wait for a clock edge before starting the test

    # Test cases
    # Case 1: CLR = H, Outputs should be low
    dut.CLR.value = 1
    await RisingEdge(dut.CLK)
    assert dut.Q.value.integer == 0b0000, f"Output mismatch: Expected Q=0b0000, got Q={dut.Q.value.integer}"

    # Case 2: CLR = L, G1_n = G2_n = 1 (enabled), M = N = 0, Data = 1010
    dut.CLR.value = 0
    dut.G1_n.value = 1
    dut.G2_n.value = 1
    dut.M.value = 0
    dut.N.value = 0
    dut.D.value = 0b1010
    await RisingEdge(dut.CLK)
    assert dut.Q.value.integer == 0b1010, f"Output mismatch: Expected Q=0b1010, got Q={dut.Q.value.integer}"

    # Case 3: Set M or N to high (output should be high impedance)
    dut.M.value = 1
    await RisingEdge(dut.CLK)
    if dut.Q.value.is_resolvable:
        raise TestFailure(f"Output should be high impedance but is: {dut.Q.value}")
