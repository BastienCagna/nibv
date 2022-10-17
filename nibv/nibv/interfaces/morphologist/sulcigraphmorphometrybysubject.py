from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class SulcigraphmorphometrybysubjectInputSpec(CommandLineInputSpec):
    left_sulci_graph = traits.File(
        exists=True,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={side: left}',
        position=0, mandatory=False, argstr='%s')
    right_sulci_graph = traits.File(
        exists=True,
        desc='Labelled Cortical folds graph, Graph, requiredAttributes={side: right}',
        position=1, mandatory=False, argstr='%s')
    sulci_file = traits.File(
        exists=True,
        desc='Sulci groups list,  JSON file',
        position=2, mandatory=False, argstr='%s')
    use_attribute = traits.Enum(
        "label", "name",
        usedefault=False,
        desc='label,  name',
        position=3, mandatory=False)
    sulcal_morpho_measures = traits.File(
        exists=False,
        desc='Sulcal morphometry measurements,  CSV File',
        position=4, mandatory=False, argstr='%s')


class SulcigraphmorphometrybysubjectOutputSpec(TraitedSpec):
    sulcal_morpho_measures = traits.File(
        desc='Sulcal morphometry measurements,  CSV File')


class Sulcigraphmorphometrybysubject(BVCommand):
    input_spec = SulcigraphmorphometrybysubjectInputSpec
    output_spec = SulcigraphmorphometrybysubjectOutputSpec
    _cmd = 'Sulcigraphmorphometrybysubject'

