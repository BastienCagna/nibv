from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class NlfitSmrInputSpec(CommandLineInputSpec):
    source = traits.File(
        exists=True,
        desc='MINC image,  MINC image',
        position=0, mandatory=False, argstr='%s')
    model = traits.File(
        exists=True,
        desc='MINC image,  MINC image',
        position=1, mandatory=False, argstr='%s')
    transformed_source = traits.File(
        exists=False,
        desc='MINC image,  MINC image',
        position=2, mandatory=False, argstr='%s')
    output_transfile = traits.File(
        exists=False,
        desc='MINC transformation matrix,  MINC transformation matrix',
        position=3, mandatory=False, argstr='%s')


class NlfitSmrOutputSpec(TraitedSpec):
    transformed_source = traits.File(
        desc='MINC image,  MINC image')
    output_transfile = traits.File(
        desc='MINC transformation matrix,  MINC transformation matrix')


class NlfitSmr(BVCommand):
    input_spec = NlfitSmrInputSpec
    output_spec = NlfitSmrOutputSpec
    _cmd = 'NlfitSmr'

