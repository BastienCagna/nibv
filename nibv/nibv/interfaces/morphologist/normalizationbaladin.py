from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class NormalizationBaladinInputSpec(CommandLineInputSpec):
    anatomy_data = traits.File(
        exists=True,
        desc='Raw T1 MRI,  GIS Image',
        position=0, mandatory=False, argstr='%s')
    anatomical_template = traits.File(
        exists=True,
        desc='anatomical Template,  GIS Image',
        position=1, mandatory=False, argstr='%s')
    transformation_matrix = traits.File(
        exists=False,
        desc='baladin Transformation, Text file',
        position=2, mandatory=False, argstr='%s')
    normalized_anatomy_data = traits.File(
        exists=False,
        desc='Raw T1 MRI, GIS image, NIFTI-1 image, gz compressed NIFTI-1 image, requiredAttributes={normalized: yes, normalization: baladin}',
        position=3, mandatory=False, argstr='%s')


class NormalizationBaladinOutputSpec(TraitedSpec):
    transformation_matrix = traits.File(
        desc='baladin Transformation, Text file')
    normalized_anatomy_data = traits.File(
        desc='Raw T1 MRI, GIS image, NIFTI-1 image, gz compressed NIFTI-1 image, requiredAttributes={normalized: yes, normalization: baladin}')


class NormalizationBaladin(BVCommand):
    input_spec = NormalizationBaladinInputSpec
    output_spec = NormalizationBaladinOutputSpec
    _cmd = 'NormalizationBaladin'

