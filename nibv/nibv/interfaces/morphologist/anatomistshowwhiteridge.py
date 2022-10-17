from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnatomistShowWhiteRidgeInputSpec(CommandLineInputSpec):
    white_ridges = traits.File(
        exists=True,
        desc='T1 MRI White Matter Ridges, Anatomist volume formats',
        position=0, mandatory=False, argstr='%s')
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI, Anatomist volume formats, exactType=True',
        position=1, mandatory=False, argstr='%s')


class AnatomistShowWhiteRidgeOutputSpec(TraitedSpec):
    pass


class AnatomistShowWhiteRidge(BVCommand):
    input_spec = AnatomistShowWhiteRidgeInputSpec
    output_spec = AnatomistShowWhiteRidgeOutputSpec
    _cmd = 'AnatomistShowWhiteRidge'

