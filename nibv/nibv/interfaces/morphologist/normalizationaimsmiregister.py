from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class NormalizationAimsmiregisterInputSpec(CommandLineInputSpec):
    anatomy_data = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    anatomical_template = traits.File(
        exists=True,
        desc='anatomical Template, aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    transformation_to_template = traits.File(
        exists=False,
        desc='Transformation matrix, Transformation matrix',
        position=2, mandatory=False, argstr='%s')
    normalized_anatomy_data = traits.File(
        exists=False,
        desc='Raw T1 MRI, aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    transformation_to_mni = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix',
        position=4, mandatory=False, argstr='%s')
    transformation_to_acpc = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=5, mandatory=False, argstr='%s')
    mni_to_acpc = traits.File(
        exists=True,
        desc='Transformation matrix, Transformation matrix',
        position=6, mandatory=False, argstr='%s')
    smoothing = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=7, argstr='%f', mandatory=False)


class NormalizationAimsmiregisterOutputSpec(TraitedSpec):
    transformation_to_template = traits.File(
        desc='Transformation matrix, Transformation matrix')
    normalized_anatomy_data = traits.File(
        desc='Raw T1 MRI, aims writable volume formats')
    transformation_to_mni = traits.File(
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix')
    transformation_to_acpc = traits.File(
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix')


class NormalizationAimsmiregister(BVCommand):
    input_spec = NormalizationAimsmiregisterInputSpec
    output_spec = NormalizationAimsmiregisterOutputSpec
    _cmd = 'NormalizationAimsmiregister'

