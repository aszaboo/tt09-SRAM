import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_quad_nand(dut):
    for a in range(16):
        for b in range(16):
            dut.a.value = a
            dut.b.value = b
            await Timer(1, units='ns')
            expected = ~(a & b) & 0xF
            assert dut.y.value == expected, f"Error: a={a}, b={b}, y={dut.y.value}, expected={expected}"

    cocotb.log.info("All tests passed!")