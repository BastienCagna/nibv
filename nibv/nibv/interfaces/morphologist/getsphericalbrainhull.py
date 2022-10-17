from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GetSphericalBrainHullInputSpec(CommandLineInputSpec):
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    left_hemi_cortex = traits.File(
        exists=True,
        desc='Left CSF+GREY Mask, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    right_hemi_cortex = traits.File(
        exists=True,
        desc='Right CSF+GREY Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    left_hemi_hull = traits.File(
        exists=False,
        desc='Hemisphere Hull Mesh, Aims mesh formats,  requiredAttributes={side: left}',
        position=3, mandatory=False, argstr='%s')
    right_hemi_hull = traits.File(
        exists=False,
        desc='Hemisphere Hull Mesh, Aims mesh formats,  requiredAttributes={side: right}',
        position=4, mandatory=False, argstr='%s')
    both_hemi_hull = traits.File(
        exists=False,
        desc='Hemisphere Hull Mesh, Aims mesh formats,  requiredAttributes={side: both}',
        position=5, mandatory=False, argstr='%s')
    brain_hull = traits.File(
        exists=False,
        desc='Brain Hull Mesh, Aims mesh formats',
        position=6, mandatory=False, argstr='%s')


class GetSphericalBrainHullOutputSpec(TraitedSpec):
    left_hemi_hull = traits.File(
        desc='Hemisphere Hull Mesh, Aims mesh formats,  requiredAttributes={side: left}')
    right_hemi_hull = traits.File(
        desc='Hemisphere Hull Mesh, Aims mesh formats,  requiredAttributes={side: right}')
    both_hemi_hull = traits.File(
        desc='Hemisphere Hull Mesh, Aims mesh formats,  requiredAttributes={side: both}')
    brain_hull = traits.File(
        desc='Brain Hull Mesh, Aims mesh formats')


class GetSphericalBrainHull(BVCommand):
    input_spec = GetSphericalBrainHullInputSpec
    output_spec = GetSphericalBrainHullOutputSpec
    _cmd = 'GetSphericalBrainHull'

