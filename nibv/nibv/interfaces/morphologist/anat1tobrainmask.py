from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaT1toBrainMaskInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    contrast = traits.Enum(
        "High grey/white contrast", "Low grey/white contrast",
        usedefault=False,
        desc='High grey/white contrast,  Low grey/white contrast',
        position=1, mandatory=False)
    bias_type = traits.Enum(
        "Standard bias field", "High bias in Z direction",
        usedefault=False,
        desc='Standard bias field,  High bias in Z direction',
        position=2, mandatory=False)
    mri_corrected = traits.File(
        exists=False,
        desc='T1 MRI Bias Corrected, Aims writable volume formats',
        position=3, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=False,
        desc='Histo Analysis,  Histo Analysis',
        position=4, mandatory=False, argstr='%s')
    brain_mask = traits.File(
        exists=False,
        desc='T1 Brain Mask, Aims writable volume formats',
        position=5, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=6, mandatory=False, argstr='%s')
    lesion_mask = traits.File(
        exists=True,
        desc='3D Volume,  aims readable Volume Formats',
        position=7, mandatory=False, argstr='%s')


class AnaT1toBrainMaskOutputSpec(TraitedSpec):
    mri_corrected = traits.File(
        desc='T1 MRI Bias Corrected, Aims writable volume formats')
    histo_analysis = traits.File(
        desc='Histo Analysis,  Histo Analysis')
    brain_mask = traits.File(
        desc='T1 Brain Mask, Aims writable volume formats')


class AnaT1toBrainMask(BVCommand):
    input_spec = AnaT1toBrainMaskInputSpec
    output_spec = AnaT1toBrainMaskOutputSpec
    _cmd = 'AnaT1toBrainMask'

