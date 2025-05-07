import setuptools


dependencies = [
    "numpy",
    "pandas",
    "nltk",
    "spacy",
    "jellyfish",
    "ipython",
    "scipy"
]

setuptools.setup(
    name="skillMatcher",
    version="1.0.3",
    author="Swapnil Suman",
    author_email="swapnilsuman65@gmail.com",
    description="An NLP module to automatically Extract skills and certifications from unstructured job postings, texts, and applicant's resumes",
    url="https://github.com/swaaap-nil/skillMatcher",
    keywords=["skillNer", 'python', 'NLP', "NER",
              "skills-extraction", "job-description"],
    download_url='https://github.com/AnasAito/SkillNER/archive/refs/tags/v1.0.3.tar.gz',
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
)
