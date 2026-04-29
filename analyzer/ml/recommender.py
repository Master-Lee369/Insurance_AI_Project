def generate_recommendation(document_type, premium, coverage, exclusions, claim_terms):
    recommendation = []

    risk_level = "Low"

    if document_type == "policy":
        recommendation.append("This appears to be an insurance policy document.")

        if premium == "Not found":
            recommendation.append("Premium amount is missing. User should verify premium details manually.")
            risk_level = "Medium"

        if coverage == "Not found":
            recommendation.append("Coverage amount is missing. This may reduce policy transparency.")
            risk_level = "High"

        if exclusions and exclusions != "No major exclusions found.":
            recommendation.append("Important exclusions are present. User should carefully review excluded conditions.")
            risk_level = "Medium"

        recommendation.append("Policy should be checked for coverage, exclusions, premium, and claim terms before approval.")

    elif document_type == "claim":
        recommendation.append("This appears to be a claim-related document.")
        recommendation.append("Verify claim amount, supporting documents, hospital records, and settlement terms.")
        risk_level = "Medium"

    elif document_type == "medical":
        recommendation.append("This appears to be a medical document.")
        recommendation.append("Medical history and diagnosis should be verified before claim approval.")
        risk_level = "Medium"

    elif document_type == "proposal":
        recommendation.append("This appears to be a proposal form.")
        recommendation.append("Applicant details, nominee details, and declared health conditions should be verified.")

    elif document_type == "legal":
        recommendation.append("This appears to be a legal insurance document.")
        recommendation.append("Legal clauses should be reviewed carefully by an authorized person.")
        risk_level = "High"

    else:
        recommendation.append("Document type could not be clearly identified.")
        recommendation.append("Manual verification is recommended.")
        risk_level = "High"

    return {
        "recommendation": " ".join(recommendation),
        "risk_level": risk_level
    }