from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class ReorientAnatomyInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    output_t1mri = traits.File(
        exists=False,
        desc='Raw T1 MRI,  Aims writable volume formats',
        position=1, mandatory=False, argstr='%s')
    transformation = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix',
        position=2, mandatory=False, argstr='%s')
    output_transformation = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix',
        position=3, mandatory=False, argstr='%s')
    commissures_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=4, mandatory=False, argstr='%s')
    output_commissures_coordinates = traits.File(
        exists=False,
        desc='Commissure coordinates, Commissure coordinates',
        position=5, mandatory=False, argstr='%s')
    allow_flip_initial_mri = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=6, mandatory=False)


class ReorientAnatomyOutputSpec(TraitedSpec):
    output_t1mri = traits.File(
        desc='Raw T1 MRI,  Aims writable volume formats')
    output_transformation = traits.File(
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix')
    output_commissures_coordinates = traits.File(
        desc='Commissure coordinates, Commissure coordinates')


class ReorientAnatomy(BVCommand):
    input_spec = ReorientAnatomyInputSpec
    output_spec = ReorientAnatomyOutputSpec
    _cmd = 'ReorientAnatomy'

