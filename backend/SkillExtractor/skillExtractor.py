import spacy
from spacy.matcher import PhraseMatcher
from pydantic import BaseModel
from model.src.general_params import SKILL_DB
from model.src.skill_extractor_class import SkillExtractor
import numpy as np

# class JobDescription(BaseModel):
#     description: str

nlp = spacy.load("en_core_web_lg")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)


def convert_numpy_types(obj):
    """Convert numpy types to Python native types for JSON serialization"""
    if isinstance(obj, dict):
        return {key: convert_numpy_types(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(item) for item in obj]
    elif isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj

def extractSkills(job_description: str):
    annotations = skill_extractor.annotate(job_description)
    serializable_annotations = convert_numpy_types(annotations)
    return serializable_annotations

def extractSkillsHtml(job_description:str):
    annotations = skill_extractor.annotate(job_description)
    return skill_extractor.describe(annotations)