"""
 https://nipype.readthedocs.io/en/latest/devel/interface_specs.html#traited-attributes
"""
from warnings import warn
from nibv.generator.utils import remove_characters


def generate_file_trait(argname, position, description="", input=True, mandatory=False):
    """
        t1_file = traits.File(
            exists=True,
            desc='Whole-head T1w image',
            mandatory=True, position=0, argstr="%s")
    """
    return "    {} = traits.File(\n        exists={},\n        desc='{}',\n        position={}, mandatory={}, argstr='%s')\n".format(
        argname, "True" if input else "False", description, position, "True" if mandatory else "False")


def generate_out_file_trait(argname, description):
    """
        t2_coreg_file = File(
            desc="coreg T2 from T1")
    """
    return "    {} = traits.File(\n        desc='{}')\n".format(argname, description)


def generate_float_trait(argname, position, description="", default=None, mandatory=False):
    """
        f = traits.Float(
            0.5, usedefault=True,
            desc='-f options of BET: fractional intensity threshold (0->1); \
                default=0.5; smaller values give larger brain outline estimates',
            argstr="-f %f", mandatory=False)
    """
    description = remove_characters(description, '"', "'")
    return "    {} = traits.Float(\n        {},\n        usedefault={},\n        desc='{}',\n        position={}, argstr='%f', mandatory={})\n".format(
        argname, default, "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")


def generate_int_trait(argname, position, description="", default=None, mandatory=False):
    description = remove_characters(description, '"', "'")
    return "    {} = traits.Int(\n        {},\n        usedefault={},\n        desc='{}',\n        position={}, argstr='%d', mandatory={})\n".format(
        argname, default, "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")


def generate_str_trait(argname, position, description="", default=None, mandatory=False):
    description = remove_characters(description, '"', "'")
    return "    {} = traits.String(\n        {},\n        usedefault={},\n        desc='{}',\n        position={}, argstr='%s', mandatory={})\n".format(
        argname, default, "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")


def generate_bool_trait(argname, position, description="", default=None, mandatory=False):
    """
        k = traits.Bool(
            False, usedefault=True, argstr="-k",
            desc="Will keep temporary files",
            mandatory=False)
    """
    description = remove_characters(description, '"', "'")
    return "    {} = traits.Bool(\n        {}, usedefault={},\n        argstr='%s',\n        desc='{}',\n        position={}, mandatory={})\n".format(
        argname, "True" if default else "False", "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")


def generate_enum_trait(argname, position, values, description="", default=None, mandatory=False):
    """
        jobtype = traits.Enum('estwrite', 'estimate', 'write',
                          desc='one of: estimate, write, estwrite',
                          usedefault=True)
    """
    if len(values) > 0 and len(values[0]) > 0:
        if len(values) == 1 and isinstance(values[0], tuple) and values[0][0] == '':
            # ('', [('Exclude the lesion mask', None), ('e', None), ('Include the lesion mask', None), (' i', None)])
            values = values[0][1]
            values = list((values[i][0], values[i+1][0])
                          for i in range(0, len(values)-1, 2))

        if isinstance(values[0], (list, tuple)):
            values = list(('' if len(v[1]) == 0 else '"{}"'.format(
                remove_characters(v[1], "'", '"').strip())) for v in values)
        else:
            values = list(('' if len(v) == 0 else '"{}"'.format(
                remove_characters(v, "'", '"').strip())) for v in values)
        vals = []
        for v in values:
            if len(v) > 0:
                vals.append(v)
        values_str = (", ".join(vals) + ",\n        ")
    else:
        warn("/!\ empty enum {argname}: {values}")
        return ""

    description = remove_characters(description, '"', "'")
    return "    {} = traits.Enum(\n        {}usedefault={},\n        desc='{}',\n        position={}, mandatory={})\n".format(
        argname, values_str, "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")
