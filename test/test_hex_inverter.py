import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_hex_inverter(dut):
    for a in range(64):
        dut.a.value = a
        await Timer(1, units='ns')
        expected = ~a & 0b111111
        assert dut.y.value == expected, f"Error: a={a}, y={dut.y.value}, expected={expected}"
        
    cocotb.log.info("All tests passed!")