# NiPype wrapping of BrainVISA processes

This python projects is made to automatically generate BrainVISA processes wraps for nipype.

## Install

Here is the commands to install it:

```shell
git clone https://github.com/BastienCagna/nibv.git
cd nibv
python setup.py develop
```

Then, as for now no hard release of the wraps exists, you can generate them by running the generate_wraps.py script (here we choose the morphologist toolbox but you can use it also for others):

```shell
python scripts/generate_wraps.py morphologist ./morphologist.json
```

## Usage example

## Contribute

Do not hesitate to post new issues and/or pull requests if you have any idea to enhance or extend this project.

## Related

Here some usefull links:

- [BrainVISA documentation](https://brainvisa.info/web/)
- [Install BrainVISA 5 to develop with python 3](http://bablab.fr/blog/brainvisa-setup.html)
