from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ViewInHippocampicReferentialInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    transformation_to_hippocamic_ref = traits.File(
        exists=False,
        desc='Transformation matrix,  Transformation matrix',
        position=1, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=False,
        desc='Commissure coordinates,  Commissure coordinates',
        position=2, mandatory=False, argstr='%s')
    normalised = traits.Enum(
        "No", "SHFJ from SPM", "MNI from Mritotal", "Marseille from SPM",
        usedefault=False,
        desc='No, SHFJ from SPM, MNI from Mritotal,  Marseille from SPM',
        position=3, mandatory=False)
    allow_flip_initial_mri = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=8, mandatory=False)
    rotation_angle = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%f', mandatory=False)
    rotation_axis = traits.Enum(
        "x", "y", "z",
        usedefault=False,
        desc='x, y,  z',
        position=10, mandatory=False)


class ViewInHippocampicReferentialOutputSpec(TraitedSpec):
    transformation_to_hippocamic_ref = traits.File(
        desc='Transformation matrix,  Transformation matrix')
    commissure_coordinates = traits.File(
        desc='Commissure coordinates,  Commissure coordinates')


class ViewInHippocampicReferential(BVCommand):
    input_spec = ViewInHippocampicReferentialInputSpec
    output_spec = ViewInHippocampicReferentialOutputSpec
    _cmd = 'ViewInHippocampicReferential'

