from project.campaigns.base_campaign import BaseCampaign

class LowBudgetCampaign(BaseCampaign):
    type_campaign = 'LowBudgetCampaign'

    def __init__(self,campaign_id: int, brand: str, required_engagement: float):
        
        super().__init__(campaign_id, brand, 2500, required_engagement,self.type_campaign)

    def check_eligibility(self,engagement_rate: float):
        return engagement_rate >= 0.9 * self.required_engagement

