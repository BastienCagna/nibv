from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class NormalizationT1Spm8ReinitInputSpec(CommandLineInputSpec):
    anatomy_data = traits.File(
        exists=True,
        desc='Raw T1 MRI, NIFTI-1 image,  SPM image',
        position=0, mandatory=False, argstr='%s')
    anatomical_template = traits.File(
        exists=True,
        desc='anatomical Template, NIFTI-1 image, MINC image,  SPM image',
        position=1, mandatory=False, argstr='%s')
    voxel_size = traits.Enum(
        "[1 1 1]",
        usedefault=False,
        desc='1 1 1',
        position=2, mandatory=False)
    cutoff_option = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%d', mandatory=False)
    nbiteration = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%d', mandatory=False)
    transformations_informations = traits.File(
        exists=False,
        desc='SPM2 normalization matrix,  Matlab file',
        position=5, mandatory=False, argstr='%s')
    normalized_anatomy_data = traits.File(
        exists=False,
        desc='Raw T1 MRI, NIFTI-1 image, SPM image,  {normalization: SPM}',
        position=6, mandatory=False, argstr='%s')
    allow_retry_initialization = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=7, mandatory=False)


class NormalizationT1Spm8ReinitOutputSpec(TraitedSpec):
    transformations_informations = traits.File(
        desc='SPM2 normalization matrix,  Matlab file')
    normalized_anatomy_data = traits.File(
        desc='Raw T1 MRI, NIFTI-1 image, SPM image,  {normalization: SPM}')


class NormalizationT1Spm8Reinit(BVCommand):
    input_spec = NormalizationT1Spm8ReinitInputSpec
    output_spec = NormalizationT1Spm8ReinitOutputSpec
    _cmd = 'NormalizationT1Spm8Reinit'

