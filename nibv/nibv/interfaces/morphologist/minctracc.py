from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)
from nipype.interfaces.base import traits
from nibv.base import BVCommand


class MinctraccInputSpec(CommandLineInputSpec):
    source = traits.File(
        exists=True,
        desc='MINC image,  MINC image',
        position=0, mandatory=False, argstr='%s')
    target = traits.File(
        exists=True,
        desc='MINC image,  MINC image',
        position=1, mandatory=False, argstr='%s')
    transformed_source = traits.File(
        exists=False,
        desc='MINC image,  MINC image',
        position=2, mandatory=False, argstr='%s')
    output_transfile = traits.File(
        exists=False,
        desc='MINC transformation matrix,  MINC transformation matrix',
        position=3, mandatory=False, argstr='%s')
    transformation_type = traits.Enum(
        "nonlinear", "principal axis", "3 translations", "3 translations + 3 rotations", "3 translations + 3 rotations + global scale", "3 translation + 3 rotations + 3 scales", "3 translation + 3 rotations + 3 scales + 1 shear", "3 translation + 3 rotations + 3 scales + 3 shears",
        usedefault=False,
        desc='nonlinear, principal axis, 3 translations, 3 translations + 3 rotations, 3 translations + 3 rotations + global scale, 3 translation + 3 rotations + 3 scales, 3 translation + 3 rotations + 3 scales + 1 shear,  3 translation + 3 rotations + 3 scales + 3 shears',
        position=4, mandatory=False)
    transformation_direction = traits.Enum(
        "Forward", "Invert",
        usedefault=False,
        desc='Forward,  Invert',
        position=5, mandatory=False)
    initial_transformation = traits.File(
        exists=True,
        desc='MINC transformation matrix,  MINC transformation matrix',
        position=6, mandatory=False, argstr='%s')
    estimation_init_transfo = traits.Enum(
        "Gravity_center", "Identity",
        usedefault=False,
        desc='Gravity_center,  Identity',
        position=7, mandatory=False)
    estimation_center = traits.Enum(
        "No", "Yes",
        usedefault=False,
        desc='No,  Yes',
        position=8, mandatory=False)
    estimation_scales = traits.Enum(
        "No", "Yes",
        usedefault=False,
        desc='No,  Yes',
        position=9, mandatory=False)
    estimation_translations = traits.Enum(
        "No", "Yes",
        usedefault=False,
        desc='No,  Yes',
        position=10, mandatory=False)
    rotation_type = traits.Enum(
        "Rotations", "Quaternions",
        usedefault=False,
        desc='Rotations,  Quaternions',
        position=12, mandatory=False)
    model_mask = traits.File(
        exists=True,
        desc='MINC image,  MINC image',
        position=13, mandatory=False, argstr='%s')
    source_mask = traits.File(
        exists=True,
        desc='MINC image,  MINC image',
        position=14, mandatory=False, argstr='%s')
    interpolation = traits.Enum(
        "trilinear", "tricubic", "nearest_neighbour",
        usedefault=False,
        desc='trilinear, tricubic,  nearest_neighbour',
        position=15, mandatory=False)
    optimization_function = traits.Enum(
        "cross_correlation", "normalized_difference", "stochastic_sign_change", "variance_of_ratio", "mutual_information",
        usedefault=False,
        desc='cross_correlation, normalized_difference, stochastic_sign_change, variance_of_ratio,  mutual_information',
        position=16, mandatory=False)
    group_number = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=17, argstr='%d', mandatory=False)
    blur_pdf = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=19, argstr='%d', mandatory=False)
    speckle = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=20, argstr='%f', mandatory=False)
    tol = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=21, argstr='%f', mandatory=False)
    simplex = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=26, argstr='%f', mandatory=False)
    num_steps = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=27, argstr='%d', mandatory=False)
    source_lattice = traits.File(
        exists=True,
        desc='MINC image,  MINC image',
        position=28, mandatory=False, argstr='%s')
    model_lattice = traits.File(
        exists=True,
        desc='MINC image,  MINC image',
        position=29, mandatory=False, argstr='%s')
    xstep = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=31, argstr='%d', mandatory=False)
    ystep = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=32, argstr='%d', mandatory=False)
    zstep = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=33, argstr='%d', mandatory=False)
    sub_lattice = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=34, argstr='%d', mandatory=False)
    max_def_magnitude = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=36, argstr='%f', mandatory=False)
    param1 = traits.Enum(
        "magnitude", "optical_flow",
        usedefault=False,
        desc='magnitude,  optical_flow',
        position=37, mandatory=False)
    param2 = traits.Enum(
        "simplex", "quadratic",
        usedefault=False,
        desc='simplex,  quadratic',
        position=38, mandatory=False)
    smoothing = traits.Enum(
        "Global", "Local",
        usedefault=False,
        desc='Global,  Local',
        position=39, mandatory=False)
    smoothing_direction = traits.Enum(
        "Isotropic", "Anisotropic",
        usedefault=False,
        desc='Isotropic,  Anisotropic',
        position=40, mandatory=False)
    super = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=41, argstr='%d', mandatory=False)
    iterations = traits.Int(
        None,
        usedefault=False,
        desc='',
        position=42, argstr='%d', mandatory=False)
    weight = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=43, argstr='%f', mandatory=False)
    stiffness = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=44, argstr='%f', mandatory=False)
    similarity_cost_ratio = traits.Float(
        None,
        usedefault=False,
        desc='',
        position=45, argstr='%f', mandatory=False)


class MinctraccOutputSpec(TraitedSpec):
    transformed_source = traits.File(
        desc='MINC image,  MINC image')
    output_transfile = traits.File(
        desc='MINC transformation matrix,  MINC transformation matrix')


class Minctracc(BVCommand):
    input_spec = MinctraccInputSpec
    output_spec = MinctraccOutputSpec
    _cmd = 'Minctracc'

