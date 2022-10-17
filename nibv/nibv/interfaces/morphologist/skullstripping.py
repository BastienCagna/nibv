from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SkullstrippingInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    brain_mask = traits.File(
        exists=True,
        desc='Brain Mask,  Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    skull_stripped = traits.File(
        exists=False,
        desc='Raw T1 MRI Brain Masked, Aims writable volume formats',
        position=2, mandatory=False, argstr='%s')


class SkullstrippingOutputSpec(TraitedSpec):
    skull_stripped = traits.File(
        desc='Raw T1 MRI Brain Masked, Aims writable volume formats')


class Skullstripping(BVCommand):
    input_spec = SkullstrippingInputSpec
    output_spec = SkullstrippingOutputSpec
    _cmd = 'Skullstripping'

