from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class T1BiasCorrectionInputSpec(CommandLineInputSpec):
    t1mri = traits.File(
        exists=True,
        desc='Raw T1 MRI,  Aims readable volume formats',
        position=0, mandatory=False, argstr='%s')
    commissure_coordinates = traits.File(
        exists=True,
        desc='Commissure coordinates, Commissure coordinates',
        position=1, mandatory=False, argstr='%s')
    sampling = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=2, argstr='%f', mandatory=False)
    field_rigidity = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=3, argstr='%f', mandatory=False)
    zdir_multiply_regul = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=4, argstr='%f', mandatory=False)
    wridges_weight = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=5, argstr='%f', mandatory=False)
    ngrid = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=6, argstr='%d', mandatory=False)
    t1mri_nobias = traits.File(
        exists=False,
        desc='T1 MRI Bias Corrected, Aims writable volume formats',
        position=8, mandatory=False, argstr='%s')
    mode = traits.Enum(
        "write_minimal", "write_all", "delete_useless", "write_minimal without correction",
        usedefault=False,
        desc='write_minimal, write_all, delete_useless,  write_minimal without correction',
        position=9, mandatory=False)
    write_field = traits.Enum(
        "yes", "no",
        usedefault=False,
        desc='yes,  no',
        position=10, mandatory=False)
    field = traits.File(
        exists=False,
        desc='T1 MRI Bias Field, Aims writable volume formats',
        position=11, mandatory=False, argstr='%s')
    write_hfiltered = traits.Enum(
        "yes", "no",
        usedefault=False,
        desc='yes,  no',
        position=12, mandatory=False)
    hfiltered = traits.File(
        exists=False,
        desc='T1 MRI Filtered For Histo, Aims writable volume formats',
        position=13, mandatory=False, argstr='%s')
    write_wridges = traits.Enum(
        "yes", "no", "read",
        usedefault=False,
        desc='yes, no,  read',
        position=14, mandatory=False)
    white_ridges = traits.File(
        exists=False,
        desc='T1 MRI White Matter Ridges, Aims writable volume formats,  exactType=1',
        position=15, mandatory=False, argstr='%s')
    variance_fraction = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=16, argstr='%d', mandatory=False)
    write_variance = traits.Enum(
        "yes", "no",
        usedefault=False,
        desc='yes,  no',
        position=17, mandatory=False)
    variance = traits.File(
        exists=False,
        desc='T1 MRI Variance, Aims writable volume formats',
        position=18, mandatory=False, argstr='%s')
    edge_mask = traits.Enum(
        "yes", "no",
        usedefault=False,
        desc='yes,  no',
        position=19, mandatory=False)
    write_edges = traits.Enum(
        "yes", "no",
        usedefault=False,
        desc='yes,  no',
        position=20, mandatory=False)
    edges = traits.File(
        exists=False,
        desc='T1 MRI Edges, Aims writable volume formats',
        position=21, mandatory=False, argstr='%s')
    write_meancurvature = traits.Enum(
        "yes", "no",
        usedefault=False,
        desc='yes,  no',
        position=22, mandatory=False)
    meancurvature = traits.File(
        exists=False,
        desc='T1 MRI Mean Curvature, Aims writable volume formats',
        position=23, mandatory=False, argstr='%s')
    fix_random_seed = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=24, mandatory=False)
    modality = traits.Enum(
        "T1", "T2",
        usedefault=False,
        desc='T1,  T2',
        position=25, mandatory=False)
    use_existing_ridges = traits.Bool(
        False, usedefault=True,
        argstr='%s',
        desc='',
        position=26, mandatory=False)


class T1BiasCorrectionOutputSpec(TraitedSpec):
    t1mri_nobias = traits.File(
        desc='T1 MRI Bias Corrected, Aims writable volume formats')
    field = traits.File(
        desc='T1 MRI Bias Field, Aims writable volume formats')
    hfiltered = traits.File(
        desc='T1 MRI Filtered For Histo, Aims writable volume formats')
    white_ridges = traits.File(
        desc='T1 MRI White Matter Ridges, Aims writable volume formats,  exactType=1')
    variance = traits.File(
        desc='T1 MRI Variance, Aims writable volume formats')
    edges = traits.File(
        desc='T1 MRI Edges, Aims writable volume formats')
    meancurvature = traits.File(
        desc='T1 MRI Mean Curvature, Aims writable volume formats')


class T1BiasCorrection(BVCommand):
    input_spec = T1BiasCorrectionInputSpec
    output_spec = T1BiasCorrectionOutputSpec
    _cmd = 'T1BiasCorrection'

