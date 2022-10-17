from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class HeadMeshInputSpec(CommandLineInputSpec):
    t1mri_nobias = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=1, mandatory=False, argstr='%s')
    head_mesh = traits.File(
        exists=False,
        desc='Head Mesh,  Aims mesh formats',
        position=2, mandatory=False, argstr='%s')
    head_mask = traits.File(
        exists=False,
        desc='Head Mask, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    keep_head_mask = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=4, mandatory=False)
    remove_mask = traits.File(
        exists=True,
        desc='3D Volume,  Aims readable volume formats',
        position=5, mandatory=False, argstr='%s')
    first_slice = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%d', mandatory=False)
    threshold = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=7, argstr='%d', mandatory=False)
    closing = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%f', mandatory=False)


class HeadMeshOutputSpec(TraitedSpec):
    head_mesh = traits.File(
        desc='Head Mesh,  Aims mesh formats')
    head_mask = traits.File(
        desc='Head Mask, Aims writable volume formats')


class HeadMesh(BVCommand):
    input_spec = HeadMeshInputSpec
    output_spec = HeadMeshOutputSpec
    _cmd = 'HeadMesh'

