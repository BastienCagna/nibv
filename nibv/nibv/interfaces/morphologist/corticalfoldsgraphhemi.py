from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CorticalFoldsGraphHemiInputSpec(CommandLineInputSpec):
    side = traits.Enum(
        "Left", "Right",
        usedefault=False,
        desc='Left,  Right',
        position=0, mandatory=False)
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=2, mandatory=False, argstr='%s')
    graph = traits.File(
        exists=False,
        desc='Cortical folds graph, Graph, requiredAttributes={labelled: No}',
        position=3, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=4, mandatory=False, argstr='%s')
    talairach_transform = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=5, mandatory=False, argstr='%s')


class CorticalFoldsGraphHemiOutputSpec(TraitedSpec):
    graph = traits.File(
        desc='Cortical folds graph, Graph, requiredAttributes={labelled: No}')


class CorticalFoldsGraphHemi(BVCommand):
    input_spec = CorticalFoldsGraphHemiInputSpec
    output_spec = CorticalFoldsGraphHemiOutputSpec
    _cmd = 'CorticalFoldsGraphHemi'

