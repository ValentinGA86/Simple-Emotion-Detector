from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'transformers',
        'torch',    # Add other dependencies as needed
        'tf-keras', # If you're using TensorFlow-based models
    ],
    entry_points={
        'console_scripts': [
            'emotion_detection=EmotionDetection.server:app.run',  # Entry point for running the app
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A Flask-based emotion detection web app",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/emotion-detection",  # Replace with your repository URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
