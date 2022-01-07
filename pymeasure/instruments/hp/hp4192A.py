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
        return str(Decimal(f).scaleb(-3).quantize(Decimal("0.000001")))

    def __frequency_get_process(v):
        return float(Decimal(v[2][1:]).scaleb(3))

    spot_frequency = Instrument.control(
        "F1 FRR EX", "FR %gEN",
        """A floating point property that controls the spot frequency in
        hertz. Takes values between 5 and 13000000.""",
        validator=truncated_range,
        set_process=__frequency_set_process,
        get_process=__frequency_get_process,
        values=[5, 13000000],
    )

    start_frequency = Instrument.control(
        "F1 TFR EX", "TF %sEN",
        """A floating point property that controls the start frequency in
        hertz. Takes values between 5 and 13000000.""",
        validator=truncated_range,
        set_process=__frequency_set_process,
        get_process=__frequency_get_process,
        values=[5, 13000000],
    )

    stop_frequency = Instrument.control(
        "F1 TFR EX", "TF %gEN",
        """A floating point property that controls the stop frequency in
        hertz. Takes values between 5 and 13000000.""",
        validator=truncated_range,
        set_process=__frequency_set_process,
        get_process=__frequency_get_process,
        values=[5, 13000000],
    )

    step_frequency = Instrument.control(
        "F1 TFR EX", "TF %gEN",
        """A floating point property that controls the step frequency in
        hertz. Takes values between 0.001 and 13000000.""",
        validator=truncated_range,
        set_process=__frequency_set_process,
        get_process=__frequency_get_process,
        values=[0.001, 13000000],
    )
