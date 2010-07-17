#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required.The domain package is a data dictionary of quantities and units that define datatypes for attributes (properties) that may be used by any class in any other package.  This package contains the definition of primitive datatypes, including units of measure and permissible values. Each datatype contains a value attribute and an optional unit of measure, which is specified as a static variable initialized to the textual description of the unit of measure. The value of the 'units' string may be country or customer specific. Typical values are given. Permissible values for enumerations are listed in the documentation for the attribute using UML constraint syntax inside curly braces. Lengths of variable strings are listed in the descriptive text where required.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------




from enthought.traits.api import Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------
Resistance = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatResistance (real part of impedance).Resistance (real part of impedance).")
ApparentPower = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of the RMS value of the voltage and the RMS value of the currentProduct of the RMS value of the voltage and the RMS value of the current")
ActivePower = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatProduct of RMS value of the voltage and the RMS value of the in-phase component of the currentProduct of RMS value of the voltage and the RMS value of the in-phase component of the current")
Reactance = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatReactance (imaginary part of impedance), at rated frequency.Reactance (imaginary part of impedance), at rated frequency.")
Seconds = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatTime, in secondsTime, in seconds")
Voltage = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatElectrical voltage.Electrical voltage.")
Frequency = Float(0, desc="http://www.w3.org/2001/XMLSchema#floatCycles per secondCycles per second")




# EOF -------------------------------------------------------------------------