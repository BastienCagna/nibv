from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class BaladinNormalizationToAimsInputSpec(CommandLineInputSpec):
    read = traits.File(
        exists=True,
        desc='Baladin Transformation,  Text file',
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
    set_transformation_in_source_volume = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=4, mandatory=False)


class BaladinNormalizationToAimsOutputSpec(TraitedSpec):
    write = traits.File(
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM,  Transformation matrix')


class BaladinNormalizationToAims(BVCommand):
    input_spec = BaladinNormalizationToAimsInputSpec
    output_spec = BaladinNormalizationToAimsOutputSpec
    _cmd = 'BaladinNormalizationToAims'

