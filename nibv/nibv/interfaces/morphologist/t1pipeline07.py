from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class T1pipeline07InputSpec(CommandLineInputSpec):
    mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=False,
        desc='T1 MRI Bias Corrected, Aims writable volume formats',
        position=1, mandatory=False, argstr='%s')
    perform_normalization = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    normalised = traits.Enum(
        "No", "MNI from SPM", "MNI from Mritotal", "Marseille from SPM",
        usedefault=False,
        desc='No, MNI from SPM, MNI from Mritotal, Marseille from SPM',
        position=3, mandatory=False)


class T1pipeline07OutputSpec(TraitedSpec):
    mri_corrected = traits.File(
        desc='T1 MRI Bias Corrected, Aims writable volume formats')


class T1pipeline07(BVCommand):
    input_spec = T1pipeline07InputSpec
    output_spec = T1pipeline07OutputSpec
    _cmd = 'T1pipeline07'

