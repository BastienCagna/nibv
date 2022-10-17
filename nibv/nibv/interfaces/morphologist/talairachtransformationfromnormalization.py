from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class TalairachTransformationFromNormalizationInputSpec(CommandLineInputSpec):
    normalization_transformation = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM,  Transformation matrix',
        position=0, mandatory=False, argstr='%s')
    talairach_transform = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=1, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=False,
        desc='Commissure coordinates, Commissure coordinates',
        position=2, mandatory=False, argstr='%s')
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  Aims Readable Volume Formats',
        position=3, mandatory=False, argstr='%s')
    source_referential = traits.File(
        exists=True,
        desc='Referential,  Referential',
        position=4, mandatory=False, argstr='%s')
    normalized_referential = traits.File(
        exists=True,
        desc='Referential,  Referential',
        position=5, mandatory=False, argstr='%s')
    acpc_referential = traits.File(
        exists=True,
        desc='Referential,  Referential',
        position=7, mandatory=False, argstr='%s')


class TalairachTransformationFromNormalizationOutputSpec(TraitedSpec):
    talairach_transform = traits.File(
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix')
    commissure_coordinates = traits.File(
        desc='Commissure coordinates, Commissure coordinates')


class TalairachTransformationFromNormalization(BVCommand):
    input_spec = TalairachTransformationFromNormalizationInputSpec
    output_spec = TalairachTransformationFromNormalizationOutputSpec
    _cmd = 'TalairachTransformationFromNormalization'

