from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SPMnormalizationPipelineInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI, NIFTI-1 image, gz compressed NIFTI-1 image, SPM image',
        position=0, mandatory=False, argstr='%s')
    transformation = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix',
        position=1, mandatory=False, argstr='%s')
    spm_transformation = traits.File(
        exists=False,
        desc='SPM2 normalization matrix, Matlab file',
        position=2, mandatory=False, argstr='%s')
    normalized_t1mri = traits.File(
        exists=False,
        desc='Raw T1 MRI, NIFTI-1 image, SPM image, {normalization: SPM}',
        position=3, mandatory=False, argstr='%s')
    template = traits.File(
        exists=True,
        desc='anatomical Template, NIFTI-1 image, gz compressed NIFTI-1 image, MINC image',
        position=4, mandatory=False, argstr='%s')
    allow_flip_initial_mri = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=5, mandatory=False)
    allow_retry_initialization = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=6, mandatory=False)
    reoriented_t1mri = traits.File(
        exists=False,
        desc='Raw T1 MRI, aims writable volume formats',
        position=7, mandatory=False, argstr='%s')
    init_translation_origin = traits.Enum(
        "0", "1",
        usedefault=False,
        desc='',
        position=8, mandatory=False)
    voxel_size = traits.Enum(
        "[1 1 1]",
        usedefault=False,
        desc='1 1 1',
        position=9, mandatory=False)
    cutoff_option = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=10, argstr='%d', mandatory=False)
    nbiteration = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=11, argstr='%d', mandatory=False)


class SPMnormalizationPipelineOutputSpec(TraitedSpec):
    transformation = traits.File(
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix')
    spm_transformation = traits.File(
        desc='SPM2 normalization matrix, Matlab file')
    normalized_t1mri = traits.File(
        desc='Raw T1 MRI, NIFTI-1 image, SPM image, {normalization: SPM}')
    reoriented_t1mri = traits.File(
        desc='Raw T1 MRI, aims writable volume formats')


class SPMnormalizationPipeline(BVCommand):
    input_spec = SPMnormalizationPipelineInputSpec
    output_spec = SPMnormalizationPipelineOutputSpec
    _cmd = 'SPMnormalizationPipeline'

