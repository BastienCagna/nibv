from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class AnaT1toBrainMaskCorrectionInputSpec(CommandLineInputSpec):
    mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  aims readable Volume Formats',
        position=0, mandatory=False, argstr='%s')
    brain_mask = traits.File(
        exists=False,
        desc='T1 Brain Mask, Aims writable volume formats',
        position=1, mandatory=False, argstr='%s')
    variant = traits.Enum(
        "Standard + iterative erosion from 2mm", "Standard + iterative erosion from 1.5mm", "Standard + fixed 1.5mm erosion", "Standard + fixed 2mm erosion", "Standard + fixed 2.5mm erosion", "Standard + fixed 3mm erosion", "Standard + fixed 3.5mm erosion", "Standard + fixed 4mm erosion", "Standard + iterative erosion from 2mm without regularisation", "Robust + iterative erosion from 2mm", "Robust + iterative erosion from 1.5mm", "Robust + fixed 1.5mm erosion", "Robust + fixed 2mm erosion", "Robust + fixed 2.5mm erosion", "Robust + fixed 3mm erosion", "Robust + fixed 3.5mm erosion", "Robust + fixed 4mm erosion", "Robust + iterative erosion from 2mm without regularisation", "Fast 1.5mm erosion", "Fast 2mm erosion", "Fast 2.5mm erosion", "Fast 3mm erosion", "Fast 3.5mm erosion", "Fast 4mm erosion", "Nothing",
        usedefault=False,
        desc='Standard + iterative erosion from 2mm, Standard + iterative erosion from 1.5mm, Standard + fixed 1.5mm erosion, Standard + fixed 2mm erosion, Standard + fixed 2.5mm erosion, Standard + fixed 3mm erosion, Standard + fixed 3.5mm erosion, Standard + fixed 4mm erosion, Standard + iterative erosion from 2mm without regularisation, Robust + iterative erosion from 2mm, Robust + iterative erosion from 1.5mm, Robust + fixed 1.5mm erosion, Robust + fixed 2mm erosion, Robust + fixed 2.5mm erosion, Robust + fixed 3mm erosion, Robust + fixed 3.5mm erosion, Robust + fixed 4mm erosion, Robust + iterative erosion from 2mm without regularisation, Fast 1.5mm erosion, Fast 2mm erosion, Fast 2.5mm erosion, Fast 3mm erosion, Fast 3.5mm erosion, Fast 4mm erosion, Nothing',
        position=2, mandatory=False)
    help = traits.Enum(
        "Nothing", "Mask visualization", "Histogram analysis visualization",
        usedefault=False,
        desc='Nothing, Mask visualization, Histogram analysis visualization',
        position=3, mandatory=False)
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=4, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=True,
        desc='Histo Analysis,  Histo Analysis',
        position=5, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=6, mandatory=False, argstr='%s')
    lesion_mask = traits.File(
        exists=True,
        desc='3D Volume,  aims readable Volume Formats',
        position=7, mandatory=False, argstr='%s')
    first_slice = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=8, argstr='%d', mandatory=False)
    last_slice = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=9, argstr='%d', mandatory=False)


class AnaT1toBrainMaskCorrectionOutputSpec(TraitedSpec):
    brain_mask = traits.File(
        desc='T1 Brain Mask, Aims writable volume formats')


class AnaT1toBrainMaskCorrection(BVCommand):
    input_spec = AnaT1toBrainMaskCorrectionInputSpec
    output_spec = AnaT1toBrainMaskCorrectionOutputSpec
    _cmd = 'AnaT1toBrainMaskCorrection'

