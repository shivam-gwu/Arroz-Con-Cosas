from setuptools import setup, find_packages

setup(
    name='arroz',
    packages=find_packages(),
    description='Arroz Con Cosas',
    version='0.1.0',
    url='https://github.com/pabloppp/Arroz-Con-Cosas',
    author='Pablo Pernías',
    author_email='pablo@pernias.com',
    keywords=['pip', 'pytorch', 'generative', 'ldm', 'vqgan'],
    zip_safe=False,
    install_requires=[
        'torch~=2.0',
        'torchvision',
        'numpy==1.*',
        'pytorch_wavelets @ git+https://github.com/fbcotter/pytorch_wavelets',
        'PyWavelets',
        'open_clip_torch~=2.7'
    ],
    include_package_data=True,
)
