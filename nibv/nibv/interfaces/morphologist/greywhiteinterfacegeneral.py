from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class GreyWhiteInterfaceGeneralInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=1, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    lgw_interface = traits.File(
        exists=False,
        desc='Left Grey White Mask, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    rgw_interface = traits.File(
        exists=False,
        desc='Right Grey White Mask, Aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    left_hemi_cortex = traits.File(
        exists=False,
        desc='Left CSF+GREY Mask, Aims writable volume formats',
        position=5, mandatory=False, argstr='%s')
    right_hemi_cortex = traits.File(
        exists=False,
        desc='Right CSF+GREY Mask, Aims writable volume formats',
        position=6, mandatory=False, argstr='%s')
    left_white_mesh = traits.File(
        exists=False,
        desc='Left Hemisphere White Mesh, Aims mesh formats',
        position=7, mandatory=False, argstr='%s')
    right_white_mesh = traits.File(
        exists=False,
        desc='Right Hemisphere White Mesh, Aims mesh formats',
        position=8, mandatory=False, argstr='%s')
    left_white_mesh_fine = traits.File(
        exists=False,
        desc='Left Fine Hemisphere White Mesh, Aims mesh formats',
        position=9, mandatory=False, argstr='%s')
    right_white_mesh_fine = traits.File(
        exists=False,
        desc='Right Fine Hemisphere White Mesh, Aims mesh formats',
        position=10, mandatory=False, argstr='%s')
    use_ridges = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=11, mandatory=False)
    white_ridges = traits.File(
        exists=True,
        desc='T1 MRI White Matter Ridges, Aims readable volume formats',
        position=12, mandatory=False, argstr='%s')


class GreyWhiteInterfaceGeneralOutputSpec(TraitedSpec):
    lgw_interface = traits.File(
        desc='Left Grey White Mask, Aims writable volume formats')
    rgw_interface = traits.File(
        desc='Right Grey White Mask, Aims writable volume formats')
    left_hemi_cortex = traits.File(
        desc='Left CSF+GREY Mask, Aims writable volume formats')
    right_hemi_cortex = traits.File(
        desc='Right CSF+GREY Mask, Aims writable volume formats')
    left_white_mesh = traits.File(
        desc='Left Hemisphere White Mesh, Aims mesh formats')
    right_white_mesh = traits.File(
        desc='Right Hemisphere White Mesh, Aims mesh formats')
    left_white_mesh_fine = traits.File(
        desc='Left Fine Hemisphere White Mesh, Aims mesh formats')
    right_white_mesh_fine = traits.File(
        desc='Right Fine Hemisphere White Mesh, Aims mesh formats')


class GreyWhiteInterfaceGeneral(BVCommand):
    input_spec = GreyWhiteInterfaceGeneralInputSpec
    output_spec = GreyWhiteInterfaceGeneralOutputSpec
    _cmd = 'GreyWhiteInterfaceGeneral'

