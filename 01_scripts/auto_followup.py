import smtplib
import csv
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

# Gmail SMTP Config
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL = "zakariakhalfa98@gmail.com"
APP_PASSWORD = "oitu oddc vcho npmz"

# Follow-up templates
FOLLOWUP_TEMPLATES = {
    1: {
        "subject": "متابعة: هل شفت موقعنا التجريبي؟ — Med Bot by Zakaria",
        "body": """مرحبا {name},

أتواصل معك بخصوص رسالتي السابقة عن موقعنا التجريبي لعيادة {clinic}.

هل شفت الموقع؟ هل عندك أي أسئلة أو ملاحظات؟

الموقع التجريبي: https://zaki4457.github.io/medical-clinic-demos/

نتمناو نتعاونو معاكم باش نطلقو موقع احترافي لعيادتكم.

تحياتنا,
Zakaria — Med Bot by Zakaria
📧 zakariakhalfa98@gmail.com
📱 +213 XXX XXX XXX
🌐 @khalfa.zakaria_34"""
    },
    2: {
        "subject": "عرض خاص: خصم 10% لـ 48 ساعة فقط — Med Bot by Zakaria",
        "body": """مرحبا {name},

حبيت ن informsك بخصوص عرض خاص:
✅ خصم 10% على أي باقة
✅ صلاحية 48 ساعة فقط

الباقة العادية: 25,000 DA → 22,500 DA
الباقة المميزة: 35,000 DA → 31,500 DA

العرض ينتهي بعد 48 ساعة. لا تفوته!

للتواصل:
📧 zakariakhalfa98@gmail.com
📱 +213 XXX XXX XXX

تحياتنا,
Zakaria — Med Bot by Zakaria"""
    },
    3: {
        "subject": "آخر فرصة: العرض ينتهي اليوم — Med Bot by Zakaria",
        "body": """مرحبا {name},

هذا آخر تواصل بخصوص العرض الخاص.

اليوم آخر يوم للخصم 10%. بعدها الأسعار ترجع عادية.

لا تفوّت الفرصة:
✅ موقع احترافي
✅ سعر مناسب
✅ دفع بالتقسيط
✅ دعم مجاني 30 يوم

للتواصل:
📧 zakariakhalfa98@gmail.com
📱 +213 XXX XXX XXX

تحياتنا,
Zakaria — Med Bot by Zakaria"""
    }
}

def load_leads():
    """Load leads from CSV"""
    leads = []
    try:
        with open('03_outreach/emails/medical_email_leads_scored.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                leads.append(row)
    except Exception as e:
        print(f"Error loading leads: {e}")
    return leads

def load_sent_log():
    """Load sent emails log"""
    sent = []
    try:
        with open('03_outreach/emails/sent_log.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                sent.append(row)
    except Exception as e:
        print(f"Error loading sent log: {e}")
    return sent

def get_followup_leads(leads, sent_log):
    """Get leads that need follow-up"""
    followup_leads = []
    
    # Get leads that were sent but haven't replied
    sent_emails = {}
    for entry in sent_log:
        email = entry.get('email', '')
        if email not in sent_emails:
            sent_emails[email] = []
        sent_emails[email].append(entry)
    
    # Check for leads that need follow-up
    for lead in leads:
        email = lead.get('email', '')
        if email in sent_emails:
            sent_count = len(sent_emails[email])
            if sent_count < 3:  # Max 3 follow-ups
                # Check when last email was sent
                last_sent = sent_emails[email][-1].get('timestamp', '')
                if last_sent:
                    try:
                        last_sent_date = datetime.strptime(last_sent, '%Y-%m-%d %H:%M:%S')
                        days_since = (datetime.now() - last_sent_date).days
                        
                        # Send follow-up every 3 days
                        if days_since >= 3:
                            followup_leads.append({
                                'lead': lead,
                                'followup_number': sent_count + 1,
                                'days_since_last': days_since
                            })
                    except:
                        pass
    
    return followup_leads

def send_followup(email, name, clinic, followup_number):
    """Send follow-up email"""
    if followup_number not in FOLLOWUP_TEMPLATES:
        print(f"No template for follow-up #{followup_number}")
        return False
    
    template = FOLLOWUP_TEMPLATES[followup_number]
    
    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL
    msg['To'] = email
    msg['Subject'] = template['subject']
    
    body = template['body'].format(name=name, clinic=clinic)
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, APP_PASSWORD)
            server.send_message(msg)
        
        # Log the email
        log_sent_email(email, followup_number)
        print(f"✓ Follow-up #{followup_number} sent to {email}")
        return True
        
    except Exception as e:
        print(f"✗ Error sending to {email}: {e}")
        return False

def log_sent_email(email, followup_number):
    """Log sent email"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('03_outreach/emails/sent_log.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([email, timestamp, f'followup_{followup_number}', ''])

def main():
    print("=== MED BOT BY ZAKARIA — AUTO FOLLOW-UP SYSTEM ===")
    print()
    
    # Load data
    leads = load_leads()
    sent_log = load_sent_log()
    
    print(f"Loaded {len(leads)} leads")
    print(f"Loaded {len(sent_log)} sent emails")
    
    # Get follow-up leads
    followup_leads = get_followup_leads(leads, sent_log)
    
    print(f"\nFound {len(followup_leads)} leads needing follow-up")
    print()
    
    # Send follow-ups
    sent_count = 0
    for item in followup_leads:
        lead = item['lead']
        followup_num = item['followup_number']
        
        email = lead.get('email', '')
        name = lead.get('name', lead.get('doctor_name', ''))
        clinic = lead.get('clinic_name', lead.get('name', ''))
        
        if email and name and clinic:
            if send_followup(email, name, clinic, followup_num):
                sent_count += 1
                time.sleep(2)  # Rate limiting
        
        if sent_count >= 10:  # Max 10 follow-ups per run
            print("\nReached max follow-ups for this run")
            break
    
    print(f"\n=== COMPLETE ===")
    print(f"Sent {sent_count} follow-up emails")

if __name__ == "__main__":
    main()
