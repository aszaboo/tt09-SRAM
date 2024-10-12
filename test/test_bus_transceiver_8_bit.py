import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_G_n_High(dut):

    # Set Enable to high (isolation)
    dut.G_n.value = 1
    await Timer(1, units='ns')
    expected = 
    assert 
        
    cocotb.log.info("All tests passed!")

@cocotb.test()
async def test_B_to_A(dut):
    # Set Enable to low (allow data transfer)
    dut.G_n.value = 0

    # Set initial an initial value for A
    for B in range(255)
    await Timer(1, units='ns')
    expected = 
    assert 
        
    cocotb.log.info("All tests passed!")