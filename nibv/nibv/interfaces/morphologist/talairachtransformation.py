from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class TalairachTransformationInputSpec(CommandLineInputSpec):
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=1, mandatory=False, argstr='%s')
    talairach_transform = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=2, mandatory=False, argstr='%s')


class TalairachTransformationOutputSpec(TraitedSpec):
    talairach_transform = traits.File(
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix')


class TalairachTransformation(BVCommand):
    input_spec = TalairachTransformationInputSpec
    output_spec = TalairachTransformationOutputSpec
    _cmd = 'TalairachTransformation'

