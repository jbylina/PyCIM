# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class WindingPiImpedance(IdentifiedObject):
    """Transformer Pi-model impedance that accurately reflects impedance for transformers with 2 or 3 windings. For transformers with 4 or more windings, you must use TransformerInfo.
    """

    def __init__(self, x=0.0, r0=0.0, b0=0.0, g=0.0, g0=0.0, x0=0.0, b=0.0, r=0.0, Windings=None, *args, **kw_args):
        """Initializes a new 'WindingPiImpedance' instance.

        @param x: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
        @param r0: Zero sequence series resistance of the winding. 
        @param b0: Zero sequence magnetizing branch susceptance. 
        @param g: Magnetizing branch conductance (G mag). 
        @param g0: Zero sequence magnetizing branch conductance. 
        @param x0: Zero sequence series reactance of the winding. 
        @param b: Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        @param r: DC resistance of the winding. 
        @param Windings: All windings having this Pi impedance.
        """
        #: Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding. 
        self.x = x

        #: Zero sequence series resistance of the winding. 
        self.r0 = r0

        #: Zero sequence magnetizing branch susceptance. 
        self.b0 = b0

        #: Magnetizing branch conductance (G mag). 
        self.g = g

        #: Zero sequence magnetizing branch conductance. 
        self.g0 = g0

        #: Zero sequence series reactance of the winding. 
        self.x0 = x0

        #: Magnetizing branch susceptance (B mag).  The value can be positive or negative. 
        self.b = b

        #: DC resistance of the winding. 
        self.r = r

        self._Windings = []
        self.Windings = [] if Windings is None else Windings

        super(WindingPiImpedance, self).__init__(*args, **kw_args)

    def getWindings(self):
        """All windings having this Pi impedance.
        """
        return self._Windings

    def setWindings(self, value):
        for x in self._Windings:
            x._PiImpedance = None
        for y in value:
            y._PiImpedance = self
        self._Windings = value

    Windings = property(getWindings, setWindings)

    def addWindings(self, *Windings):
        for obj in Windings:
            obj._PiImpedance = self
            self._Windings.append(obj)

    def removeWindings(self, *Windings):
        for obj in Windings:
            obj._PiImpedance = None
            self._Windings.remove(obj)
