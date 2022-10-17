from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class NormalizationSPMInputSpec(CommandLineInputSpec):
    anatomy_data = traits.File(
        exists=True,
        desc='Raw T1 MRI, NIFTI-1 image,  SPM image',
        position=0, mandatory=False, argstr='%s')
    anatomical_template = traits.File(
        exists=True,
        desc='anatomical Template, NIFTI-1 image, MINC image,  SPM image',
        position=1, mandatory=False, argstr='%s')
    job_file = traits.File(
        exists=False,
        desc='SPM2 parameters,  Matlab file',
        position=2, mandatory=False, argstr='%s')
    voxel_size = traits.Enum(
        "[1 1 1]",
        usedefault=False,
        desc='1 1 1',
        position=3, mandatory=False)
    cutoff_option = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%d', mandatory=False)
    nbiteration = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%d', mandatory=False)
    transformations_informations = traits.File(
        exists=False,
        desc='SPM2 normalization matrix,  Matlab file',
        position=6, mandatory=False, argstr='%s')
    normalized_anatomy_data = traits.File(
        exists=False,
        desc='Raw T1 MRI, NIFTI-1 image, SPM image,  {normalization: SPM}',
        position=7, mandatory=False, argstr='%s')


class NormalizationSPMOutputSpec(TraitedSpec):
    job_file = traits.File(
        desc='SPM2 parameters,  Matlab file')
    transformations_informations = traits.File(
        desc='SPM2 normalization matrix,  Matlab file')
    normalized_anatomy_data = traits.File(
        desc='Raw T1 MRI, NIFTI-1 image, SPM image,  {normalization: SPM}')


class NormalizationSPM(BVCommand):
    input_spec = NormalizationSPMInputSpec
    output_spec = NormalizationSPMOutputSpec
    _cmd = 'NormalizationSPM'

