from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class VipBiasCorrectionInputSpec(CommandLineInputSpec):
    mri = traits.File(
        exists=True,
        desc='T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    mri_corrected = traits.File(
        exists=False,
        desc='T1 MRI Bias Corrected, aims Writable Volume Formats',
        position=1, mandatory=False, argstr='%s')
    field_rigidity = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=2, argstr='%f', mandatory=False)
    write_field = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=3, mandatory=False)
    dim_rigidity = traits.Enum(
        "2D", "3D",
        usedefault=False,
        desc='2D,  3D',
        position=4, mandatory=False)
    sampling = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%f', mandatory=False)
    ngrid = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%d', mandatory=False)
    geometric = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=7, argstr='%f', mandatory=False)
    nincrement = traits.Enum(
        "1", "2", "3", "4", "5",
        usedefault=False,
        desc='1, 2, 3, 4,  5',
        position=8, mandatory=False)
    init_temperature = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%f', mandatory=False)
    increment = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=10, argstr='%f', mandatory=False)
    init_amplitude = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=11, argstr='%f', mandatory=False)
    zdir_multiply_regul = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=12, argstr='%f', mandatory=False)


class VipBiasCorrectionOutputSpec(TraitedSpec):
    mri_corrected = traits.File(
        desc='T1 MRI Bias Corrected, aims Writable Volume Formats')


class VipBiasCorrection(BVCommand):
    input_spec = VipBiasCorrectionInputSpec
    output_spec = VipBiasCorrectionOutputSpec
    _cmd = 'VipBiasCorrection'

