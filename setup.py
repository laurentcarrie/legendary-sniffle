import setuptools
#with open("README.md", "r") as fh:
#    long_description = fh.read()
long_description = "hello world"
setuptools.setup(
     name='mylc_docker_util',
     version='0.1',
#     scripts=['dokr'] ,
     author="lc",
     author_email="xxx@gmail.com",
     description="a Docker utility package",
     long_description=long_description,
   long_description_content_type="text",
 #    url="https://github.com/javatechy/dokr",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )