from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class FSLnormalizationToAimsInputSpec(CommandLineInputSpec):
    read = traits.File(
        exists=True,
        desc='FSL Transformation, Matlab file, enableConversion=0',
        position=0, mandatory=False, argstr='%s')
    source_volume = traits.File(
        exists=True,
        desc='4D Volume, aims readable Volume Formats',
        position=1, mandatory=False, argstr='%s')
    write = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM,  Transformation matrix',
        position=2, mandatory=False, argstr='%s')
    registered_volume = traits.File(
        exists=True,
        desc='4D Volume, aims readable Volume Formats, requiredAttributes={normalized: yes}',
        position=3, mandatory=False, argstr='%s')
    standard_template = traits.Enum(
        "1x1x1 mm", "FSL 91x109x91", "1", "1x1x1 mm", "",
        usedefault=False,
        desc='',
        position=4, mandatory=False)
    set_transformation_in_source_volume = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=5, mandatory=False)


class FSLnormalizationToAimsOutputSpec(TraitedSpec):
    write = traits.File(
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM,  Transformation matrix')


class FSLnormalizationToAims(BVCommand):
    input_spec = FSLnormalizationToAimsInputSpec
    output_spec = FSLnormalizationToAimsOutputSpec
    _cmd = 'FSLnormalizationToAims'

