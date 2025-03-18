from typing import Dict, Any, List, Tuple
from templates.form_template import STEP4_FIELDS
import os

def validate_job_input(job_input: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Validate the job input data"""
    errors = []
    
    # Required fields
    required_fields = [
        "company_name",
        "cultural_fit_factors",
        "personality_traits",
        "work_experience",
        "technology_domain",
        "tools",
        "role_title",
        "core_responsibilities",
        "skills_competencies",
        "education_requirements",
        "specialized_role_focus"
    ]
    
    # Check for required fields
    for field in required_fields:
        if field not in job_input or not job_input[field]:
            errors.append(f"Missing required field: {field}")
    
    # Check for list fields
    list_fields = ["cultural_fit_factors", "personality_traits", "technology_domain", "tools"]
    for field in list_fields:
        if field in job_input and not isinstance(job_input[field], list):
            errors.append(f"Field {field} must be a list")
    
    # Validate specific fields
# Validate specific fields



    # Find the specialized_role_focus field
    role_focus_field = next(field for field in STEP4_FIELDS if field["key"] == "specialized_role_focus")
    valid_roles = role_focus_field["options"]

    if "specialized_role_focus" in job_input and job_input["specialized_role_focus"] not in valid_roles:
        errors.append(f"Invalid role focus: {job_input['specialized_role_focus']}")        
                
    if "employment_type" in job_input:
        valid_types = ["Full-Time", "Part-Time", "Contract", "Freelance"]
        if job_input["employment_type"] not in valid_types:
            errors.append(f"Invalid employment type: {job_input['employment_type']}")
    
    return len(errors) == 0, errors


def format_error_message(errors: List[str]) -> str:
    """Format error messages for display"""
    if not errors:
        return ""
        
    return "Please fix the following errors:\n" + "\n".join([f"- {error}" for error in errors])


"""def check_api_credentials(platform):

# checks if the required API credentials are set
    if platform == "twitter":
        return all([
            os.getenv("TWITTER_API_KEY"),
            os.getenv("TWITTER_API_SECRET"),
            os.getenv("TWITTER_ACCESS_TOKEN"),
            os.getenv("TWITTER_ACCESS_SECRET")
        ])
    elif platform == "linkedin":
        return all([
            os.getenv("LINKEDIN_CLIENT_ID"),
            os.getenv("LINKEDIN_CLIENT_SECRET"),
            os.getenv("LINKEDIN_ACCESS_TOKEN"),
            os.getenv("LINKEDIN_COMPANY_ID")
        ])
    elif platform == "google_jobs":
        return all([
            os.getenv("GOOGLE_JOBS_SERVICE_ACCOUNT_PATH"),
            os.getenv("GOOGLE_CLOUD_PROJECT_ID"),
            os.getenv("GOOGLE_JOBS_TENANT_ID"),
            os.getenv("GOOGLE_JOBS_COMPANY_ID")
        ])
    elif platform == "naukri":
        return bool(os.getenv("NAUKRI_API_KEY"))
    elif platform == "upwork":
        return all([
            os.getenv("UPWORK_API_KEY"),
            os.getenv("UPWORK_API_SECRET")
        ])
    return False"""