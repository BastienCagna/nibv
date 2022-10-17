from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class Anatomist3DActivationsInputSpec(CommandLineInputSpec):
    activations = traits.File(
        exists=True,
        desc='fMRI activations,  anatomist Volume Formats',
        position=0, mandatory=False, argstr='%s')
    minimumsize = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=2, argstr='%d', mandatory=False)
    mri = traits.File(
        exists=True,
        desc='T1 MRI,   anatomist Volume Formats',
        position=3, mandatory=False, argstr='%s')
    show_mri = traits.Enum(
        "Yes", "No",
        usedefault=False,
        desc='Yes,  No',
        position=4, mandatory=False)
    fmritomri = traits.File(
        exists=True,
        desc='Transformation matrix, Transformation matrix',
        position=5, mandatory=False, argstr='%s')
    head_mesh = traits.File(
        exists=True,
        desc='Head mesh,  anatomist Mesh Formats',
        position=7, mandatory=False, argstr='%s')
    brain_mesh = traits.File(
        exists=True,
        desc='Brain mesh,  anatomist Mesh Formats',
        position=9, mandatory=False, argstr='%s')


class Anatomist3DActivationsOutputSpec(TraitedSpec):
    pass


class Anatomist3DActivations(BVCommand):
    input_spec = Anatomist3DActivationsInputSpec
    output_spec = Anatomist3DActivationsOutputSpec
    _cmd = 'Anatomist3DActivations'

