from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class BaladinNormalizationPipelineInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI, NIFTI-1 image,  gz compressed NIFTI-1 image',
        position=0, mandatory=False, argstr='%s')
    transformation = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix',
        position=1, mandatory=False, argstr='%s')
    template = traits.File(
        exists=True,
        desc='anatomical Template, NIFTI-1 image,  gz compressed NIFTI-1 image',
        position=2, mandatory=False, argstr='%s')
    set_transformation_in_source_volume = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=3, mandatory=False)
    allow_flip_initial_mri = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=4, mandatory=False)
    reoriented_t1mri = traits.File(
        exists=False,
        desc='Raw T1 MRI, aims writable volume formats',
        position=5, mandatory=False, argstr='%s')


class BaladinNormalizationPipelineOutputSpec(TraitedSpec):
    transformation = traits.File(
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix')
    reoriented_t1mri = traits.File(
        desc='Raw T1 MRI, aims writable volume formats')


class BaladinNormalizationPipeline(BVCommand):
    input_spec = BaladinNormalizationPipelineInputSpec
    output_spec = BaladinNormalizationPipelineOutputSpec
    _cmd = 'BaladinNormalizationPipeline'

