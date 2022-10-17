from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class InspectMultipleSulciGraphsInputSpec(CommandLineInputSpec):
    pass


class InspectMultipleSulciGraphsOutputSpec(TraitedSpec):
    pass


class InspectMultipleSulciGraphs(BVCommand):
    input_spec = InspectMultipleSulciGraphsInputSpec
    output_spec = InspectMultipleSulciGraphsOutputSpec
    _cmd = 'InspectMultipleSulciGraphs'

