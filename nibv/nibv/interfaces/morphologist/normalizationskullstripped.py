from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class NormalizationSkullstrippedInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    brain_mask = traits.File(
        exists=True,
        desc='Brain Mask,  Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    template = traits.File(
        exists=True,
        desc='anatomical Template, NIFTI-1 image, MINC image, SPM image, requiredAttributes={skull_stripped: yes}',
        position=2, mandatory=False, argstr='%s')
    skull_stripped = traits.File(
        exists=False,
        desc='Raw T1 MRI Brain Masked, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    transformation = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix',
        position=4, mandatory=False, argstr='%s')
    talairach_transformation = traits.File(
        exists=False,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=5, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=False,
        desc='Commissure coordinates, Commissure coordinates',
        position=6, mandatory=False, argstr='%s')


class NormalizationSkullstrippedOutputSpec(TraitedSpec):
    skull_stripped = traits.File(
        desc='Raw T1 MRI Brain Masked, Aims writable volume formats')
    transformation = traits.File(
        desc='Transform Raw T1 MRI to Talairach-MNI template-SPM, Transformation matrix')
    talairach_transformation = traits.File(
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix')
    commissure_coordinates = traits.File(
        desc='Commissure coordinates, Commissure coordinates')


class NormalizationSkullstripped(BVCommand):
    input_spec = NormalizationSkullstrippedInputSpec
    output_spec = NormalizationSkullstrippedOutputSpec
    _cmd = 'NormalizationSkullstripped'

