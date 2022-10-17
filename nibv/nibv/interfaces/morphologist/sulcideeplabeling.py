from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulciDeepLabelingInputSpec(CommandLineInputSpec):
    roots = traits.File(
        exists=True,
        desc='Cortex catchment bassins, aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    skeleton = traits.File(
        exists=True,
        desc='Cortex skeleton, aims readable volume formats',
        position=1, mandatory=False, argstr='%s')


class SulciDeepLabelingOutputSpec(TraitedSpec):
    pass


class SulciDeepLabeling(BVCommand):
    input_spec = SulciDeepLabelingInputSpec
    output_spec = SulciDeepLabelingOutputSpec
    _cmd = 'SulciDeepLabeling'

