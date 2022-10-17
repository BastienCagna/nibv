from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowBrainMaskInputSpec(CommandLineInputSpec):
    brain_mask = traits.File(
        exists=True,
        desc='Brain Mask,  Anatomist volume formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Anatomist volume formats',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowBrainMaskOutputSpec(TraitedSpec):
    pass


class AnatomistShowBrainMask(BVCommand):
    input_spec = AnatomistShowBrainMaskInputSpec
    output_spec = AnatomistShowBrainMaskOutputSpec
    _cmd = 'AnatomistShowBrainMask'

