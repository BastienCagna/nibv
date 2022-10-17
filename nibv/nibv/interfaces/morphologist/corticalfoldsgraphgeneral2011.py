from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class CorticalFoldsGraphGeneral2011InputSpec(CommandLineInputSpec):
    mri_corrected = traits.File(
        exists=True,
        desc='T1 MRI Bias Corrected, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    split_mask = traits.File(
        exists=True,
        desc='Split Brain Mask, Aims readable volume formats',
        position=1, mandatory=False, argstr='%s')
    left_graph = traits.File(
        exists=False,
        desc='Cortical folds graph, Graph, requiredAttributes={labelled: No, side: left, }',
        position=2, mandatory=False, argstr='%s')
    right_graph = traits.File(
        exists=False,
        desc='Cortical folds graph, Graph, requiredAttributes={labelled: No, side: right, }',
        position=3, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=4, mandatory=False, argstr='%s')
    talairach_transform = traits.File(
        exists=True,
        desc='Transform Raw T1 MRI to Talairach-AC/PC-Anatomist, Transformation matrix',
        position=5, mandatory=False, argstr='%s')


class CorticalFoldsGraphGeneral2011OutputSpec(TraitedSpec):
    left_graph = traits.File(
        desc='Cortical folds graph, Graph, requiredAttributes={labelled: No, side: left, }')
    right_graph = traits.File(
        desc='Cortical folds graph, Graph, requiredAttributes={labelled: No, side: right, }')


class CorticalFoldsGraphGeneral2011(BVCommand):
    input_spec = CorticalFoldsGraphGeneral2011InputSpec
    output_spec = CorticalFoldsGraphGeneral2011OutputSpec
    _cmd = 'CorticalFoldsGraphGeneral2011'

