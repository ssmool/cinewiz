from setuptools import setup, find_packages

setup(
    name="cinewiz",
    version="1.0.0",
    author="ssmool",
    author_email="contact@ssmool.dev",
    description="CineWiz — GenAI Creative Image/Text Toolkit for visual storytelling and compositing.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ssmool/cinewiz",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "rembg>=2.0.56",
        "Pillow>=10.0.0",
        "selenium>=4.24.0",
        "beautifulsoup4>=4.12.3",
        "requests>=2.32.3",
        "transformers>=4.45.0",
        "torch>=2.3.0",
        "nltk>=3.9",
        "scikit-image>=0.24.0",
        "qrcode[pil]>=7.4.2",
        "opencv-python>=4.10.0.84",
        "numpy>=1.26.4",
        "sentencepiece>=0.2.0",
        "safetensors>=0.4.4"
    ],
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics :: Editors",
        "Intended Audience :: Developers",
        "Natural Language :: English"
    ],
)
