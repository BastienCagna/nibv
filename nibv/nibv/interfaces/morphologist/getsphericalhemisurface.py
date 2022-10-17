from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GetSphericalHemiSurfaceInputSpec(CommandLineInputSpec):
    side = traits.Enum(
        "Both", "Left", "Right",
        usedefault=False,
        desc='Both, Left,  Right',
        position=0, mandatory=False)
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    left_hemi_cortex = traits.File(
        exists=True,
        desc='Left CSF+GREY Mask, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    right_hemi_cortex = traits.File(
        exists=True,
        desc='Right CSF+GREY Mask, Aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    left_hemi_mesh = traits.File(
        exists=False,
        desc='Left Hemisphere Mesh, Aims mesh formats',
        position=5, mandatory=False, argstr='%s')
    right_hemi_mesh = traits.File(
        exists=False,
        desc='Right Hemisphere Mesh, Aims mesh formats',
        position=6, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=7, mandatory=False)


class GetSphericalHemiSurfaceOutputSpec(TraitedSpec):
    left_hemi_mesh = traits.File(
        desc='Left Hemisphere Mesh, Aims mesh formats')
    right_hemi_mesh = traits.File(
        desc='Right Hemisphere Mesh, Aims mesh formats')


class GetSphericalHemiSurface(BVCommand):
    input_spec = GetSphericalHemiSurfaceInputSpec
    output_spec = GetSphericalHemiSurfaceOutputSpec
    _cmd = 'GetSphericalHemiSurface'

