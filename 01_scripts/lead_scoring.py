import csv
from datetime import datetime

def calculate_lead_score(lead):
    """Calculate lead score based on various factors"""
    score = 0
    
    # Email engagement (if available)
    if lead.get('email_opened', '').lower() == 'yes':
        score += 20
    if lead.get('email_clicked', '').lower() == 'yes':
        score += 30
    if lead.get('replied', '').lower() == 'yes':
        score += 50
    
    # Phone engagement
    if lead.get('phone_answered', '').lower() == 'yes':
        score += 40
    if lead.get('interested', '').lower() == 'yes':
        score += 60
    
    # WhatsApp engagement
    if lead.get('whatsapp_replied', '').lower() == 'yes':
        score += 45
    if lead.get('whatsapp.clicked', '').lower() == 'yes':
        score += 25
    
    # Website visit
    if lead.get('visited_website', '').lower() == 'yes':
        score += 35
    
    # Budget indication
    budget = lead.get('budget', '').lower()
    if 'high' in budget or '35000' in str(lead.get('budget_amount', 0)):
        score += 40
    elif 'medium' in budget or '25000' in str(lead.get('budget_amount', 0)):
        score += 25
    elif 'low' in budget:
        score += 10
    
    # Timeline
    timeline = lead.get('timeline', '').lower()
    if 'urgent' in timeline or 'asap' in timeline:
        score += 35
    elif 'soon' in timeline or '1 week' in timeline:
        score += 25
    elif 'month' in timeline:
        score += 15
    
    # Company size
    size = lead.get('clinic_size', '').lower()
    if 'large' in size or '10+' in size:
        score += 30
    elif 'medium' in size or '5-10' in size:
        score += 20
    elif 'small' in size or '1-5' in size:
        score += 10
    
    # Decision maker
    if lead.get('is_decision_maker', '').lower() == 'yes':
        score += 40
    
    # Previous experience
    if lead.get('had_website', '').lower() == 'yes':
        score += 20
    
    # Location (Algiers = higher value)
    location = lead.get('location', '').lower()
    if 'algiers' in location or 'alger' in location:
        score += 15
    elif 'oran' in location or 'constantine' in location:
        score += 10
    
    return min(score, 100)  # Cap at 100

def get_lead_priority(score):
    """Get priority level based on score"""
    if score >= 80:
        return 'HOT'
    elif score >= 60:
        return 'WARM'
    elif score >= 40:
        return 'COLD'
    else:
        return 'DEAD'

def get_next_action(priority):
    """Get recommended next action"""
    actions = {
        'HOT': 'Call immediately, send proposal',
        'WARM': 'Follow up email, schedule call',
        'COLD': 'Add to nurture sequence',
        'DEAD': 'Archive or re-engage in 3 months'
    }
    return actions.get(priority, 'Review manually')

def score_leads(input_file, output_file):
    """Score all leads and save to new file"""
    leads = []
    
    # Load leads
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                leads.append(row)
    except Exception as e:
        print(f"Error loading leads: {e}")
        return
    
    print(f"Loaded {len(leads)} leads")
    
    # Score and categorize
    scored_leads = []
    for lead in leads:
        score = calculate_lead_score(lead)
        priority = get_lead_priority(score)
        next_action = get_next_action(priority)
        
        lead['score'] = score
        lead['priority'] = priority
        lead['next_action'] = next_action
        lead['scored_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        scored_leads.append(lead)
    
    # Sort by score (highest first)
    scored_leads.sort(key=lambda x: x.get('score', 0), reverse=True)
    
    # Save scored leads
    if scored_leads:
        fieldnames = scored_leads[0].keys()
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(scored_leads)
        
        print(f"\nSaved {len(scored_leads)} scored leads to {output_file}")
    
    # Print summary
    hot = sum(1 for l in scored_leads if l.get('priority') == 'HOT')
    warm = sum(1 for l in scored_leads if l.get('priority') == 'WARM')
    cold = sum(1 for l in scored_leads if l.get('priority') == 'COLD')
    dead = sum(1 for l in scored_leads if l.get('priority') == 'DEAD')
    
    print(f"\n=== LEAD SCORING SUMMARY ===")
    print(f"HOT leads:   {hot} ({hot/len(scored_leads)*100:.1f}%)")
    print(f"WARM leads:  {warm} ({warm/len(scored_leads)*100:.1f}%)")
    print(f"COLD leads:  {cold} ({cold/len(scored_leads)*100:.1f}%)")
    print(f"DEAD leads:  {dead} ({dead/len(scored_leads)*100:.1f}%)")
    
    print(f"\n=== TOP 10 LEADS ===")
    for i, lead in enumerate(scored_leads[:10], 1):
        name = lead.get('name', lead.get('doctor_name', 'Unknown'))
        email = lead.get('email', '')
        score = lead.get('score', 0)
        priority = lead.get('priority', '')
        print(f"{i}. {name} ({email}) - Score: {score} - Priority: {priority}")

if __name__ == "__main__":
    input_file = '03_outreach/emails/medical_email_leads_scored.csv'
    output_file = '03_outreach/emails/leads_scored_prioritized.csv'
    
    score_leads(input_file, output_file)
