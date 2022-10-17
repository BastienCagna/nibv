from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ImportBrainMaskInputSpec(CommandLineInputSpec):
    input = traits.File(
        exists=True,
        desc='Raw T1 MRI,  Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    output = traits.File(
        exists=False,
        desc='T1 Brain Mask, Aims writable volume formats,  exactType=1',
        position=1, mandatory=False, argstr='%s')
    copy_referential_of = traits.File(
        exists=True,
        desc='Raw T1 MRI, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')


class ImportBrainMaskOutputSpec(TraitedSpec):
    output = traits.File(
        desc='T1 Brain Mask, Aims writable volume formats,  exactType=1')


class ImportBrainMask(BVCommand):
    input_spec = ImportBrainMaskInputSpec
    output_spec = ImportBrainMaskOutputSpec
    _cmd = 'ImportBrainMask'

