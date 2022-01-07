#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2021 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
import time

import pytest
import math
from pymeasure.instruments.hp.hp4192A import HP4192A
from pymeasure.adapters import PrologixAdapter
adapter = PrologixAdapter('/dev/cu.usbserial-PXEFMYB9', serial_timeout=1)

#pytest.skip('Only work with connected hardware', allow_module_level=True)


class TestHP4192A:
    """
    Unit tests for HP4192A class.
    This test suite, needs the following setup to work properly:
        - A HP4192A device should be connected to the computer;
        - The device's address must be set in the RESOURCE constant;
    """

    ##################################################
    # HP4192A device address goes here:
    RESOURCE = "USB0::10893::6039::CN57266430::INSTR"
    ##################################################

    #########################
    # PARAMETRIZATION CASES #
    #########################

    BOOLEANS = [False, True]
    FREQUENCIES = [5, 1234.567, 12345.67, 123456.7, 1234567, 12345670, 13000000]
    STEP_FREQUENCIES = [1, 5, 1234.567, 12345.67, 123456.7, 1234567, 12345670, 13000000]
    BIASES = [-35, -0.01, 0, 0.01, 35]

    INSTR = HP4192A(adapter.gpib(17))

    ############
    # FIXTURES #
    ############

    @pytest.fixture
    def instr(self):
        #self.INSTR.reset()
        return self.INSTR

    #########
    # TESTS #
    #########

    @pytest.mark.parametrize("case", FREQUENCIES)
    def test_spot_frequency(self, instr, case):
        if case > 10000:
            instr.spot_frequency = case
            assert instr.spot_frequency == case

    @pytest.mark.parametrize("case", FREQUENCIES)
    def test_start_frequency(self, instr, case):
        instr.start_frequency = case
        assert instr.start_frequency == case

    @pytest.mark.parametrize("case", FREQUENCIES)
    def test_stop_frequency(self, instr, case):
        instr.stop_frequency = case
        assert instr.stop_frequency == case

    @pytest.mark.parametrize("case", STEP_FREQUENCIES)
    def test_step_frequency(self, instr, case):
        instr.step_frequency = case
        assert instr.step_frequency == case

    @pytest.mark.parametrize("case", BIASES)
    def test_spot_bias(self, instr, case):
        instr.spot_bias = case
        assert instr.spot_bias == case
        instr.bias_off()
