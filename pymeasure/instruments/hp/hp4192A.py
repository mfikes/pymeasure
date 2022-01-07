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

from pymeasure.instruments import Instrument
from pymeasure.instruments.validators import truncated_range
from decimal import Decimal

class HP4192A(Instrument):
    """ Represents the Hewlett Packard 4192A LF Impedance Analyzer
    and provides a high-level interface for interacting with the
    instrument.
    """

    def __init__(self, resourceName, **kwargs):
        super().__init__(
            resourceName,
            "Hewlett Packard 4192A LF Impedance Analyzer",
            includeSCPI=False,
            **kwargs
        )

    def __frequency_set_process(f):
        if f < 10000.0:
            resolution = Decimal('0.000001')
        elif f < 100000.0:
            resolution = Decimal('0.00001')
        elif f < 1000000.0:
            resolution = Decimal('0.0001')
        else:
            resolution = Decimal('0.001')
        return str(Decimal(f).scaleb(-3).quantize(resolution))

    def __frequency_get_process(v):
        return float(Decimal(v[2][1:]).scaleb(3))

    def __bias_get_process(v):
        return float(v[2][1:])

    spot_frequency = Instrument.control(
        "F1 FRR EX", "FR %sEN",
        """A floating point property that controls the spot frequency in
        hertz. Takes values between 5 Hz and 13000000 Hz. """,
        validator=truncated_range,
        set_process=__frequency_set_process,
        get_process=__frequency_get_process,
        values=[5, 13000000],
    )

    start_frequency = Instrument.control(
        "F1 TFR EX", "TF %sEN",
        """A floating point property that controls the start frequency in
        hertz. Takes values between 5 Hz and 13000000 Hz. """,
        validator=truncated_range,
        set_process=__frequency_set_process,
        get_process=__frequency_get_process,
        values=[5, 13000000],
    )

    stop_frequency = Instrument.control(
        "F1 TFR EX", "TF %sEN",
        """A floating point property that controls the stop frequency in
        hertz. Takes values between 5 Hz and 13000000 Hz. """,
        validator=truncated_range,
        set_process=__frequency_set_process,
        get_process=__frequency_get_process,
        values=[5, 13000000],
    )

    step_frequency = Instrument.control(
        "F1 SFR EX", "SF %sEN",
        """A floating point property that controls the step frequency in
        hertz. Takes values between 1 Hz and 13000000 Hz. """,
        validator=truncated_range,
        set_process=__frequency_set_process,
        get_process=__frequency_get_process,
        values=[1, 13000000],
    )

    spot_bias = Instrument.control(
        "F1 BIR EX", "BI %gEN",
        """A floating point property that controls the spot bias in
        volts. Takes values between -35 V and +35 V. """,
        validator=truncated_range,
        get_process=__bias_get_process,
        values=[-35, 35],
    )

    start_bias = Instrument.control(
        "F1 TBR EX", "TB %gEN",
        """A floating point property that controls the start bias in
        volts. Takes values between -35 V and +35 V. """,
        validator=truncated_range,
        get_process=__bias_get_process,
        values=[-35, 35],
    )

    stop_bias = Instrument.control(
        "F1 PBR EX", "PB %gEN",
        """A floating point property that controls the stop bias in
        volts. Takes values between -35 V and +35 V. """,
        validator=truncated_range,
        get_process=__bias_get_process,
        values=[-35, 35],
    )

    step_bias = Instrument.control(
        "F1 SBR EX", "SB %gEN",
        """A floating point property that controls the step bias in
        volts. Takes values between 0.01 V and 35 V. """,
        validator=truncated_range,
        get_process=__bias_get_process,
        values=[0.01, 35],
    )

    impedance = Instrument.measurement(
        "F0 A2 C2 EX",
        """Reads the complex impedance in ohms. """,
        get_process=lambda v: complex(float(v[0][4:]), float(v[1][4:]))
    )

    admittance = Instrument.measurement(
        "F0 A2 C3 EX",
        """Reads the complex admittance in siemens. """,
        get_process=lambda v: complex(float(v[0][4:]), float(v[1][4:]))
    )

    def bias_off(self):
        """Turns off the DC bias. """
        self.write("I0")
