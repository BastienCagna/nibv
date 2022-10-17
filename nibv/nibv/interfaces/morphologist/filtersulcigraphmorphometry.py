from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class FiltersulcigraphmorphometryInputSpec(CommandLineInputSpec):
    sulcal_morpho_measures = traits.File(
        exists=True,
        desc='Sulcal morphometry measurements, CSV File',
        position=0, mandatory=False, argstr='%s')
    separator = traits.String(
        None,
        usedefault=False,
        desc='',
        position=1, argstr='%s', mandatory=False)
    filter_sulci = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=2, mandatory=False)
    prop_sulci = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%f', mandatory=False)
    filter_subjects = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=4, mandatory=False)
    prop_subjects = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%f', mandatory=False)
    replace_missing = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=6, mandatory=False)
    replace_method = traits.Enum(
        "median", "mean",
        usedefault=False,
        desc='median,  mean',
        position=7, mandatory=False)
    verbose = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=8, mandatory=False)
    filtered_sulcal_morpho_measures = traits.File(
        exists=False,
        desc='Sulcal morphometry measurements, CSV File, requiredAttributes={filtered: True}',
        position=9, mandatory=False, argstr='%s')


class FiltersulcigraphmorphometryOutputSpec(TraitedSpec):
    filtered_sulcal_morpho_measures = traits.File(
        desc='Sulcal morphometry measurements, CSV File, requiredAttributes={filtered: True}')


class Filtersulcigraphmorphometry(BVCommand):
    input_spec = FiltersulcigraphmorphometryInputSpec
    output_spec = FiltersulcigraphmorphometryOutputSpec
    _cmd = 'Filtersulcigraphmorphometry'

