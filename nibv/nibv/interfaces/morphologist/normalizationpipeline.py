from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class NormalizationPipelineInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    transformation = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix',
        position=1, mandatory=False, argstr='%s')
    allow_flip_initial_mri = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    commissures_coordinates = traits.File(
        exists=True,
        desc='Commissure Coordinates, Commissure Coordinates',
        position=3, mandatory=False, argstr='%s')
    reoriented_t1mri = traits.File(
        exists=False,
        desc='Raw T1 MRI, aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    output_commissures_coordinates = traits.File(
        exists=False,
        desc='Commissure Coordinates, Commissure Coordinates',
        position=5, mandatory=False, argstr='%s')


class NormalizationPipelineOutputSpec(TraitedSpec):
    transformation = traits.File(
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix')
    reoriented_t1mri = traits.File(
        desc='Raw T1 MRI, aims writable volume formats')
    output_commissures_coordinates = traits.File(
        desc='Commissure Coordinates, Commissure Coordinates')


class NormalizationPipeline(BVCommand):
    input_spec = NormalizationPipelineInputSpec
    output_spec = NormalizationPipelineOutputSpec
    _cmd = 'NormalizationPipeline'

