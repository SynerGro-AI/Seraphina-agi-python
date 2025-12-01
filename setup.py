from setuptools import setup, find_packages

setup(
    name="seraphina-agi-companion",
    version="0.1.0",
    description="Pure Python AGI Companion for Seraphina - No mining, no wallets",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Seraphina AGI",
    author_email="seraphina@agi.example.com",
    url="https://github.com/SynerGro-AI/Seraphina-agi-python",
    packages=find_packages(),
    install_requires=[
        "requests",  # for HTTP
        "cryptography",  # for crypto
        "pyttsx3",  # for text-to-speech
        "speechrecognition",  # for speech recognition
        "pyaudio",  # for microphone access
    ],
    entry_points={
        "console_scripts": [
            "seraphina-agi=seraphina_agi.runner:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)