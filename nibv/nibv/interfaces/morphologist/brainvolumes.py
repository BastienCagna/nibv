from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class BrainvolumesInputSpec(CommandLineInputSpec):
    split_brain = traits.File(
        exists=True,
        desc='Split brain mask, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    left_grey_white = traits.File(
        exists=True,
        desc='Left Grey White Mask, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    right_grey_white = traits.File(
        exists=True,
        desc='Right Grey White Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    left_csf = traits.File(
        exists=False,
        desc='Left CSF Mask, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    right_csf = traits.File(
        exists=False,
        desc='Right CSF Mask, Aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    subject = traits.String(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%s', mandatory=False)
    brain_volumes_file = traits.File(
        exists=False,
        desc='Brain volumetry measurements,  CSV file',
        position=6, mandatory=False, argstr='%s')


class BrainvolumesOutputSpec(TraitedSpec):
    left_csf = traits.File(
        desc='Left CSF Mask, Aims writable volume formats')
    right_csf = traits.File(
        desc='Right CSF Mask, Aims writable volume formats')
    brain_volumes_file = traits.File(
        desc='Brain volumetry measurements,  CSV file')


class Brainvolumes(BVCommand):
    input_spec = BrainvolumesInputSpec
    output_spec = BrainvolumesOutputSpec
    _cmd = 'Brainvolumes'

