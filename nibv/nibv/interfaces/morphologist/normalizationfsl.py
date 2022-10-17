from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class NormalizationFSLInputSpec(CommandLineInputSpec):
    anatomy_data = traits.File(
        exists=True,
        desc='Raw T1 MRI, NIFTI-1 image,  gz compressed NIFTI-1 image',
        position=0, mandatory=False, argstr='%s')
    anatomical_template = traits.File(
        exists=True,
        desc='anatomical Template, NIFTI-1 image,  gz compressed NIFTI-1 image',
        position=1, mandatory=False, argstr='%s')
    alignment = traits.Enum(
        "Already Virtualy Aligned", "Not Aligned but Same Orientation", "Incorrectly Oriented",
        usedefault=False,
        desc='Already Virtualy Aligned, Not Aligned but Same Orientation,  Incorrectly Oriented',
        position=2, mandatory=False)
    transformation_matrix = traits.File(
        exists=False,
        desc='FSL Transformation,  Matlab file',
        position=3, mandatory=False, argstr='%s')
    normalized_anatomy_data = traits.File(
        exists=False,
        desc='Raw T1 MRI,  gz compressed NIFTI-1 image',
        position=4, mandatory=False, argstr='%s')
    cost_function = traits.Enum(
        "corratio", "mutualinfo", "normmi", "labeldiff",
        usedefault=False,
        desc='',
        position=5, mandatory=False)
    search_cost_function = traits.Enum(
        "corratio", "mutualinfo", "normmi", "labeldiff",
        usedefault=False,
        desc='',
        position=6, mandatory=False)


class NormalizationFSLOutputSpec(TraitedSpec):
    transformation_matrix = traits.File(
        desc='FSL Transformation,  Matlab file')
    normalized_anatomy_data = traits.File(
        desc='Raw T1 MRI,  gz compressed NIFTI-1 image')


class NormalizationFSL(BVCommand):
    input_spec = NormalizationFSLInputSpec
    output_spec = NormalizationFSLOutputSpec
    _cmd = 'NormalizationFSL'

