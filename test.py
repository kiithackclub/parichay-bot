from airtable import Airtable
from dotenv import load_dotenv
import os


load_dotenv()

airtable = Airtable(os.getenv('AIRTABLE_API_KEY'), os.getenv('AIRTABLE_BASE_URL'), "appqLAIXpfmBRorop")

print(airtable.get_members_by_discord_id("abhishekraj272#6496", "tblB9sWiSRn2pVG2E").body)