from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaSplitBrainFromBrainMaskCorrectionInputSpec(CommandLineInputSpec):
    pass


class AnaSplitBrainFromBrainMaskCorrectionOutputSpec(TraitedSpec):
    pass


class AnaSplitBrainFromBrainMaskCorrection(BVCommand):
    input_spec = AnaSplitBrainFromBrainMaskCorrectionInputSpec
    output_spec = AnaSplitBrainFromBrainMaskCorrectionOutputSpec
    _cmd = 'AnaSplitBrainFromBrainMaskCorrection'

