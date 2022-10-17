from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class Morphologist2012InputSpec(CommandLineInputSpec):
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


class Morphologist2012OutputSpec(TraitedSpec):
    mri_corrected = traits.File(
        desc='T1 MRI Bias Corrected, Aims writable volume formats')


class Morphologist2012(BVCommand):
    input_spec = Morphologist2012InputSpec
    output_spec = Morphologist2012OutputSpec
    _cmd = 'Morphologist2012'

