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

    spot_frequency = Instrument.control(
        "F1 FRR EX", "FR %gEN",
        """An integer point property that controls the spot frequency in
        hertz. Takes values between 5 and 13000000.""",
        validator=truncated_range,
        set_process=lambda v: v / 1000,
        get_process=lambda v: int(float(v[2][1:]) * 1000),
        values=[5, 13000000],
    )

    start_frequency = Instrument.control(
        "F1 TFR EX", "TF %gEN",
        """An integer property that controls the start frequency in
        hertz. Takes values between 5 and 13000000.""",
        validator=truncated_range,
        set_process=lambda v: v / 1000,
        get_process=lambda v: int(float(v[2][1:]) * 1000),
        values=[5, 13000000],
    )
