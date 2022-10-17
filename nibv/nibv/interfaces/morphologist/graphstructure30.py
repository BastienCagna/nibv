from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class Graphstructure30InputSpec(CommandLineInputSpec):
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
    hemi_cortex = traits.File(
        exists=True,
        desc='CSF+GREY Mask, Aims readable volume formats',
        position=3, mandatory=False, argstr='%s')
    skeleton = traits.File(
        exists=False,
        desc='Cortex Skeleton, Aims writable volume formats',
        position=4, mandatory=False, argstr='%s')
    roots = traits.File(
        exists=False,
        desc='Cortex Catchment Bassins, Aims writable volume formats',
        position=5, mandatory=False, argstr='%s')
    graph = traits.File(
        exists=False,
        desc='Cortical folds graph, Graph, requiredAttributes={graph_version: 3.0,  labelled: No}',
        position=6, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=7, mandatory=False, argstr='%s')
    compute_fold_meshes = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=8, mandatory=False)


class Graphstructure30OutputSpec(TraitedSpec):
    skeleton = traits.File(
        desc='Cortex Skeleton, Aims writable volume formats')
    roots = traits.File(
        desc='Cortex Catchment Bassins, Aims writable volume formats')
    graph = traits.File(
        desc='Cortical folds graph, Graph, requiredAttributes={graph_version: 3.0,  labelled: No}')


class Graphstructure30(BVCommand):
    input_spec = Graphstructure30InputSpec
    output_spec = Graphstructure30OutputSpec
    _cmd = 'Graphstructure30'

