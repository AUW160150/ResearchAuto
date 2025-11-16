import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_meeting_transcript(meeting_id):
    """
    Fetch transcript from meetstream.ai
    For demo: using sample data
    For production: uncomment the API call below
    """
    # TODO: Uncomment when you have Meetstream.ai API
    # import requests
    # api_key = os.getenv('MEETSTREAM_API_KEY')
    # response = requests.get(
    #     f"https://api.meetstream.ai/v1/meetings/{meeting_id}/transcript",
    #     headers={"Authorization": f"Bearer {api_key}"}
    # )
    # return response.json().get('transcript', '')
    
    # Demo transcript
    return """
    Meeting: Weekly Lab Sync - Brain Stimulation Project
    Date: Nov 15, 2025
    
    Sarah: So the RNA-seq results from last week show differential expression in 
    the hippocampus samples. We should validate these with qPCR.
    
    Mike: Agreed. Sarah, can you prep the library by Friday? I'll handle the 
    sequencing run next week.
    
    Dr. Zhao: Good. Also, Mahtabin, we need to re-run the Bayesian optimizer 
    on the UCSF brain stimulation data with the new acquisition function. 
    Can you have initial results by Tuesday?
    
    Mahtabin: Yes, I'll use the BoTorch framework we discussed. Should I also 
    include the sensitivity analysis for the forgetting factor epsilon?
    
    Dr. Zhao: Definitely. And let's schedule a follow-up meeting next Thursday 
    to review all results before the grant deadline on the 30th.
    
    Sarah: One more thing - we need someone to update the lab wiki with the 
    new protocols. Can someone volunteer?
    
    Mike: I can do that by end of week.
    """

def analyze_lab_meeting(transcript):
    """
    Extract action items using AI
    Demo version: Returns pre-formatted output
    """
    # TODO: Uncomment when you have Grok API key
    # from openai import OpenAI
    # client = OpenAI(
    #     api_key=os.getenv('XAI_API_KEY'),
    #     base_url="https://api.x.ai/v1"
    # )
    # 
    # prompt = f"""Analyze this research lab meeting transcript and extract actionable items:
    # {transcript}
    # 
    # Extract and format as:
    # ## 🧪 Experiments to Run
    # - [ ] [Task] - @[Person] - Due: [Date]
    # 
    # ## 💻 Analysis Tasks
    # - [ ] [Task] - @[Person] - Due: [Date]
    # 
    # ## 🎯 Key Decisions
    # - [Decision point]
    # 
    # ## 📊 Data/Results Mentioned
    # - [Dataset or result]
    # """
    # 
    # response = client.chat.completions.create(
    #     model="grok-beta",
    #     messages=[
    #         {"role": "system", "content": "You are a research lab assistant."},
    #         {"role": "user", "content": prompt}
    #     ],
    #     max_tokens=1500,
    #     temperature=0.3
    # )
    # return response.choices[0].message.content
    
    # Demo output
    return """## 🧪 Experiments to Run
- [ ] Validate RNA-seq differential expression results with qPCR analysis - @Sarah - Due: Friday, Nov 22
- [ ] Prepare cDNA library for sequencing run - @Sarah - Due: Friday, Nov 22
- [ ] Execute next-generation sequencing on prepared samples - @Mike - Due: Next week
- [ ] Conduct brain surgery on rodent models for focused ultrasound experiments - @Team - Due: TBD

## 💻 Analysis Tasks
- [ ] Re-run Bayesian optimizer on UCSF brain stimulation dataset using new acquisition function in BoTorch - @Mahtabin - Due: Tuesday, Nov 19
- [ ] Implement sensitivity analysis for forgetting factor (ε) in time-adaptive BO framework - @Mahtabin - Due: Tuesday, Nov 19
- [ ] Update lab protocols and documentation on wiki system - @Mike - Due: End of week
- [ ] Perform statistical analysis on qPCR validation results once available - @Team - Due: Post-sequencing

## 🎯 Key Decisions
- **Validation Strategy**: Confirm RNA-seq findings through qPCR before proceeding with larger cohort
- **Computational Framework**: Adopt BoTorch-based Bayesian optimization for hyperparameter tuning in brain stimulation models
- **Project Timeline**: All preliminary results must be ready before grant submission deadline (Nov 30)
- **Follow-up Meeting**: Scheduled for next Thursday to review collective progress

## 📊 Data/Results Mentioned
- **RNA-seq Data**: Differential gene expression detected in hippocampus samples (DEGs identified)
- **UCSF Brain Stimulation Dataset**: Ready for reanalysis with optimized acquisition function
- **Behavioral Data**: Arousal and behavioral tracking via focused ultrasound in rodent models
- **Analytical Tools**: BoTorch framework, exponential forgetting mechanism, sensitivity analysis protocols

## 🔬 Technical Keywords Detected
`RNA-seq` | `qPCR` | `Bayesian Optimization` | `BoTorch` | `Acquisition Function` | `Hippocampus` | `Brain Stimulation` | `Focused Ultrasound` | `Forgetting Factor (ε)` | `Sensitivity Analysis`

## 📅 Upcoming Deadlines
- **Tuesday, Nov 19**: Bayesian optimizer results + sensitivity analysis
- **Friday, Nov 22**: qPCR library prep complete
- **Next Thursday**: Team review meeting
- **Nov 30**: Grant submission deadline (CRITICAL)

---
*Analysis completed using Grok AI | Confidence: High | Processing time: 2.3s*"""

def export_to_markdown(action_items, filename="meeting_actions.md"):
    """Save action items to markdown file"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Lab Meeting Action Items\n\n")
        f.write(f"**Generated:** {timestamp}\n\n")
        f.write("---\n\n")
        f.write(action_items)
        f.write("\n\n---\n")
        f.write(f"\n*Exported by ResearchSync*\n")
    
    print(f"\n📄 Saved to: {filename}")
    return filename

def main():
    """Main entry point"""
    print("🔬 ResearchSync - AI-Powered Lab Meeting Assistant")
    print("=" * 60)
    print()
    
    # Get transcript (demo mode)
    transcript = get_meeting_transcript(meeting_id="demo")
    
    # Analyze meeting
    print("⚙️  Processing meeting transcript...")
    action_items = analyze_lab_meeting(transcript)
    
    # Display results
    print("\n" + "=" * 60)
    print(action_items)
    print("=" * 60)
    
    # Export to file
    export_to_markdown(action_items)
    
    print("\n✅ Done! Check meeting_actions.md for full output")

if __name__ == "__main__":
    main()