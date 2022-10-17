from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class T1BiasCorrectionGeneralInputSpec(CommandLineInputSpec):
    mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=False,
        desc='T1 MRI Bias Corrected, aims Writable Volume Formats',
        position=1, mandatory=False, argstr='%s')
    write_hfiltered = traits.Enum(
        "yes", "no",
        usedefault=False,
        desc='yes,  no',
        position=2, mandatory=False)
    hfiltered = traits.File(
        exists=False,
        desc='T1 MRI Filtered For Histo, aims Writable Volume Formats',
        position=3, mandatory=False, argstr='%s')
    write_wridges = traits.Enum(
        "yes", "no", "read",
        usedefault=False,
        desc='yes, no,  read',
        position=4, mandatory=False)
    white_ridges = traits.File(
        exists=False,
        desc='T1 MRI White Matter Ridges, aims Writable Volume Formats',
        position=5, mandatory=False, argstr='%s')


class T1BiasCorrectionGeneralOutputSpec(TraitedSpec):
    mri_corrected = traits.File(
        desc='T1 MRI Bias Corrected, aims Writable Volume Formats')
    hfiltered = traits.File(
        desc='T1 MRI Filtered For Histo, aims Writable Volume Formats')
    white_ridges = traits.File(
        desc='T1 MRI White Matter Ridges, aims Writable Volume Formats')


class T1BiasCorrectionGeneral(BVCommand):
    input_spec = T1BiasCorrectionGeneralInputSpec
    output_spec = T1BiasCorrectionGeneralOutputSpec
    _cmd = 'T1BiasCorrectionGeneral'

