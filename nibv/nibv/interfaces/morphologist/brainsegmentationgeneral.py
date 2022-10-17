from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class BrainSegmentationGeneralInputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    brain_mask = traits.File(
        exists=False,
        desc='T1 Brain Mask, aims Writable Volume Formats',
        position=1, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=2, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=3, mandatory=False, argstr='%s')
    lesion_mask = traits.File(
        exists=True,
        desc='Lesion Mask,  aims readable Volume Formats',
        position=4, mandatory=False, argstr='%s')
    white_ridges = traits.File(
        exists=True,
        desc='T1 MRI White Matter Ridges, aims Writable Volume Formats',
        position=5, mandatory=False, argstr='%s')


class BrainSegmentationGeneralOutputSpec(TraitedSpec):
    brain_mask = traits.File(
        desc='T1 Brain Mask, aims Writable Volume Formats')


class BrainSegmentationGeneral(BVCommand):
    input_spec = BrainSegmentationGeneralInputSpec
    output_spec = BrainSegmentationGeneralOutputSpec
    _cmd = 'BrainSegmentationGeneral'

