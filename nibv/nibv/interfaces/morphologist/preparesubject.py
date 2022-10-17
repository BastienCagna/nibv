from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class PreparesubjectInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=False,
        desc='Commissure coordinates,  Commissure coordinates',
        position=1, mandatory=False, argstr='%s')
    normalised = traits.Enum(
        "No", "MNI from SPM", "MNI from Mritotal", "Marseille from SPM",
        usedefault=False,
        desc='No, MNI from SPM, MNI from Mritotal,  Marseille from SPM',
        position=2, mandatory=False)
    allow_flip_initial_mri = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=7, mandatory=False)
    reoriented_t1mri = traits.File(
        exists=False,
        desc='Raw T1 MRI, aims writable volume formats',
        position=8, mandatory=False, argstr='%s')
    remove_older_mni_normalization = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=9, mandatory=False)
    older_mni_normalization = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix',
        position=10, mandatory=False, argstr='%s')


class PreparesubjectOutputSpec(TraitedSpec):
    commissure_coordinates = traits.File(
        desc='Commissure coordinates,  Commissure coordinates')
    reoriented_t1mri = traits.File(
        desc='Raw T1 MRI, aims writable volume formats')


class Preparesubject(BVCommand):
    input_spec = PreparesubjectInputSpec
    output_spec = PreparesubjectOutputSpec
    _cmd = 'Preparesubject'

