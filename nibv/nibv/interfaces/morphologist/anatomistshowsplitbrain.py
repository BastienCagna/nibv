from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowSplitBrainInputSpec(CommandLineInputSpec):
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Anatomist volume formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Anatomist volume formats',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowSplitBrainOutputSpec(TraitedSpec):
    pass


class AnatomistShowSplitBrain(BVCommand):
    input_spec = AnatomistShowSplitBrainInputSpec
    output_spec = AnatomistShowSplitBrainOutputSpec
    _cmd = 'AnatomistShowSplitBrain'

