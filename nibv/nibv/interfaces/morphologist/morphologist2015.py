from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class Morphologist2015InputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI, Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    perform_normalization = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=1, mandatory=False)
    t1mri_nobias = traits.File(
        exists=False,
        desc='T1 MRI Bias Corrected, Aims writable volume formats',
        position=6, mandatory=False, argstr='%s')
    histo_analysis = traits.File(
        exists=False,
        desc='Histo Analysis,  Histo Analysis',
        position=7, mandatory=False, argstr='%s')
    split_brain = traits.File(
        exists=False,
        desc='Split Brain Mask, Aims writable volume formats',
        position=8, mandatory=False, argstr='%s')
    left_graph = traits.File(
        exists=False,
        desc='Cortical Folds Graph, Graph, requiredAttributes={labelled: No,  side: left}',
        position=9, mandatory=False, argstr='%s')
    right_graph = traits.File(
        exists=False,
        desc='Cortical Folds Graph, Graph, requiredAttributes={labelled: No,  side: right}',
        position=10, mandatory=False, argstr='%s')
    perform_sulci_recognition = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=11, mandatory=False)
    left_labelled_graph = traits.File(
        exists=False,
        desc='Labelled Cortical Folds Graph, Graph, requiredAttributes={labelled: Yes,  side: left}',
        position=12, mandatory=False, argstr='%s')
    right_labelled_graph = traits.File(
        exists=False,
        desc='Labelled Cortical Folds Graph, Graph, requiredAttributes={labelled: Yes,  side: right}',
        position=13, mandatory=False, argstr='%s')


class Morphologist2015OutputSpec(TraitedSpec):
    t1mri_nobias = traits.File(
        desc='T1 MRI Bias Corrected, Aims writable volume formats')
    histo_analysis = traits.File(
        desc='Histo Analysis,  Histo Analysis')
    split_brain = traits.File(
        desc='Split Brain Mask, Aims writable volume formats')
    left_graph = traits.File(
        desc='Cortical Folds Graph, Graph, requiredAttributes={labelled: No,  side: left}')
    right_graph = traits.File(
        desc='Cortical Folds Graph, Graph, requiredAttributes={labelled: No,  side: right}')
    left_labelled_graph = traits.File(
        desc='Labelled Cortical Folds Graph, Graph, requiredAttributes={labelled: Yes,  side: left}')
    right_labelled_graph = traits.File(
        desc='Labelled Cortical Folds Graph, Graph, requiredAttributes={labelled: Yes,  side: right}')


class Morphologist2015(BVCommand):
    input_spec = Morphologist2015InputSpec
    output_spec = Morphologist2015OutputSpec
    _cmd = 'Morphologist2015'

