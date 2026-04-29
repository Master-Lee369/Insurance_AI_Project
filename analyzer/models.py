from django.db import models


class InsuranceDocument(models.Model):
    DOCUMENT_TYPES = [
        ('policy', 'Policy Document'),
        ('claim', 'Claim Document'),
        ('medical', 'Medical Record'),
        ('proposal', 'Proposal Form'),
        ('legal', 'Legal Document'),
        ('unknown', 'Unknown'),
    ]

    title = models.CharField(max_length=200)
    document = models.FileField(upload_to='insurance_documents/')
    document_type = models.CharField(
        max_length=50,
        choices=DOCUMENT_TYPES,
        default='unknown'
    )

    extracted_text = models.TextField(blank=True, null=True)

    policy_number = models.CharField(max_length=100, blank=True, null=True)
    premium_amount = models.CharField(max_length=100, blank=True, null=True)
    coverage_amount = models.CharField(max_length=100, blank=True, null=True)
    exclusions = models.TextField(blank=True, null=True)
    claim_terms = models.TextField(blank=True, null=True)

    recommendation = models.TextField(blank=True, null=True)
    risk_level = models.CharField(max_length=50, blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title