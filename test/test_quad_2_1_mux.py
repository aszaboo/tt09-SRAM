import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_strobe_high_select_high(dut):
    dut.strobe.value = 1
    dut.select.value = 1
    expected = 0b0000
    for A in range(16):
        for B in range(16):   
            dut.A.value = A
            dut.B.value = B
            await Timer(1, units='ns')
            assert dut.Y.value == expected, f"Error: a={A}, b={B}, y={dut.Y.value}, expected={expected}"

    cocotb.log.info("Strobe High, Select High Test Passed!")

@cocotb.test()
async def test_strobe_high_select_low(dut):
    dut.strobe.value = 1
    dut.select.value = 0
    expected = 0b0000
    for A in range(16):
        for B in range(16):
            dut.A.value = A
            dut.B.value = B
            await Timer(1, units='ns')
            assert dut.Y.value == expected, f"Error: a={A}, b={B}, y={dut.Y.value}, expected={expected}"

    cocotb.log.info("Strobe High, Select Low Test Passed!")

@cocotb.test()
async def test_select_low(dut):
    dut.strobe.value = 0
    dut.select.value = 0
    for A in range(16):
        for B in range(16):
            dut.A.value = A
            dut.B.value = B
            expected = A
            await Timer(1, units='ns')
            assert dut.Y.value == expected, f"Error: a={A}, b={B}, y={dut.Y.value}, expected={expected}"

    cocotb.log.info("Strobe Low, Select Low Test Passed!")

@cocotb.test()
async def test_select_high(dut):
    dut.strobe.value = 0
    dut.select.value = 1
    for A in range(16):
        for B in range(16):
            dut.A.value = A
            dut.B.value = B
            expected = B
            await Timer(1, units='ns')
            assert dut.Y.value == expected, f"Error: a={A}, b={B}, y={dut.Y.value}, expected={expected}"

    cocotb.log.info("Strobe Low, Select High Test Passed!")