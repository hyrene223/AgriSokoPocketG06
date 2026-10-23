from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
EVIDENCE = ROOT / "evidence"
DOCS.mkdir(exist_ok=True)
EVIDENCE.mkdir(exist_ok=True)

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="CoverTitle", parent=styles["Title"],
    alignment=TA_CENTER, fontSize=21, leading=27, spaceAfter=14
))
styles.add(ParagraphStyle(
    name="CoverSub", parent=styles["Normal"],
    alignment=TA_CENTER, fontSize=12, leading=18
))
styles.add(ParagraphStyle(
    name="SmallText", parent=styles["BodyText"],
    fontSize=8, leading=11
))
styles.add(ParagraphStyle(
    name="TableText", parent=styles["BodyText"],
    fontSize=8, leading=10
))

def P(text, style="BodyText"):
    return Paragraph(text, styles[style])

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.grey)
    canvas.drawString(20 * mm, 12 * mm, "AgriSoko Pocket G06")
    canvas.drawRightString(190 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()

def make_pdf(path, story):
    doc = SimpleDocTemplate(
        str(path), pagesize=A4,
        rightMargin=20*mm, leftMargin=20*mm,
        topMargin=18*mm, bottomMargin=20*mm
    )
    doc.build(story, onFirstPage=footer, onLaterPages=footer)

# 1. TECHNICAL REPORT
story = [
    Spacer(1, 28*mm),
    P("AgriSoko Pocket", "CoverTitle"),
    P("Group G06 — Technical Report", "CoverSub"),
    Spacer(1, 8*mm),
    P("Mobile application with an AI-powered text-matching service", "CoverSub"),
    Spacer(1, 12*mm),
    P("<b>Group members</b>", "Heading2"),
    P("Nsabimana Irene (25/27790)<br/>"
      "Uwimbabazi Aimerance (25/28028)<br/>"
      "Ishimwe Alphaxad (25/27565)<br/>"
      "Muram Yaser (25/28164)<br/>"
      "Umutoniwase Alice (25/28026)<br/>"
      "Doris Kelly (24/23813)"),
    Spacer(1, 10*mm),
    P("Prepared for academic submission. Confirm all project details and "
      "complete the outstanding evidence before submitting.", "Italic"),
    PageBreak(),
    P("1. Project Overview", "Heading1"),
    P("AgriSoko Pocket G06 is a group project designed to help users search "
      "team-member information through a mobile interface backed by a text-matching service."),
    P("2. Objectives", "Heading1"),
    P("• Provide a mobile search interface.<br/>"
      "• Compare user queries with approved member information.<br/>"
      "• Return a match when the similarity is sufficient.<br/>"
      "• Avoid treating similarity as proof that a result is correct.<br/>"
      "• Validate backend behaviour using automated tests."),
    P("3. System Architecture", "Heading1"),
    P("The project uses a React Native application built with Expo and a Python "
      "FastAPI backend. The mobile application sends search requests to the backend. "
      "The backend provides GET /health, GET /model-info, and POST /search."),
    P("4. AI Matching Approach", "Heading1"),
    P("The matching service uses TF-IDF text representation and cosine similarity "
      "to compare a search query with available member information. A similarity "
      "threshold helps determine whether a match is suitable. Results depend on the "
      "accuracy and completeness of the approved records."),
    P("5. Mobile Application", "Heading1"),
    P("The documented interface includes a search input, search action, loading "
      "feedback, result details, error handling, and project information. The project "
      "is configured for Android builds through Expo Application Services (EAS). "
      "A successful final APK installation and end-to-end device test still need to "
      "be confirmed and evidenced."),
    P("6. Backend Testing", "Heading1"),
    P("The recorded pytest run completed with 7 passed, 1 warning, and 0 failed. "
      "The warning concerned Starlette test-client integration with httpx. This "
      "records the backend automated tests only; it does not verify all mobile or "
      "deployment requirements."),
    P("7. Responsible Use and Limitations", "Heading1"),
    P("• Member records should be verified before use.<br/>"
      "• Text similarity can produce incorrect or incomplete matches.<br/>"
      "• A similarity score is not proof of factual correctness.<br/>"
      "• The API address must be appropriate for the deployment environment.<br/>"
      "• Search results should be checked against approved information.<br/>"
      "• Backend tests alone do not establish that the complete Android app works."),
    P("8. Collaboration and Evidence", "Heading1"),
    P("The group should complete the contribution record using each member's actual "
      "work and evidence. Obtain real tester feedback, capture screenshots and the "
      "actual test output, and record the final Android build and installation checks. "
      "Do not submit placeholders as completed evidence."),
    P("9. Conclusion", "Heading1"),
    P("AgriSoko Pocket combines a mobile search interface with an AI text-matching "
      "backend. Before final submission, verify the final application build, mobile-to-"
      "backend connectivity, assignment requirements, and supporting evidence.")
]
make_pdf(DOCS / "COMBO_A3_G06_REPORT.pdf", story)

# 2. GROUP CONTRIBUTIONS
members = [
    ("Nsabimana Irene", "25/27790"),
    ("Uwimbabazi Aimerance", "25/28028"),
    ("Ishimwe Alphaxad", "25/27565"),
    ("Muram Yaser", "25/28164"),
    ("Umutoniwase Alice", "25/28026"),
    ("Doris Kelly", "24/23813"),
]
rows = [[P("<b>Member</b>", "TableText"),
         P("<b>Registration</b>", "TableText"),
         P("<b>Actual tasks completed</b>", "TableText"),
         P("<b>Evidence / PR</b>", "TableText"),
         P("<b>Signature</b>", "TableText")]]
for name, reg in members:
    rows.append([
        P(name, "TableText"), P(reg, "TableText"),
        P("To be completed by the group", "TableText"),
        P("To be added", "TableText"),
        P("Pending", "TableText")
    ])
contrib = [
    P("AgriSoko Pocket G06", "Title"),
    P("Group Contributions Record", "Heading1"),
    P("Complete this table together. Record only work each member actually "
      "completed or reviewed. Each member should check their entry and sign the final record."),
    Spacer(1, 5*mm),
    Table(rows, colWidths=[34*mm, 24*mm, 46*mm, 34*mm, 25*mm], repeatRows=1),
    Spacer(1, 8*mm),
    P("<b>Group confirmation</b>", "Heading2"),
    P("We confirm that the contribution descriptions in the completed version accurately "
      "represent the work performed by each group member."),
    Spacer(1, 5*mm),
    P("Group representative: __________________________________________"),
    Spacer(1, 4*mm),
    P("Date: _____________________"),
    Spacer(1, 4*mm),
    P("Signatures: attach or provide the genuine signatures of the group members.")
]
make_pdf(EVIDENCE / "CONTRIBUTIONS.pdf", contrib)

# 3. TEST LOG
test_story = [
    P("AgriSoko Pocket G06", "Title"),
    P("Backend Test Log", "Heading1"),
    P("<b>Recorded date:</b> 23 October 2026"),
    P("<b>Working directory:</b><br/>"
      "C:\\Users\\Shami\\AgriSokoPocketG06\\ai-api"),
    P("<b>Command:</b>"),
    P(r"<font name='Courier'>.\.venv\Scripts\python.exe -m pytest -q</font>"),
    Spacer(1, 4*mm),
    P("Recorded result", "Heading2"),
    P("<b>7 passed, 1 warning, 0 failed.</b>"),
    P("The warning concerned Starlette's test-client integration with httpx. "
      "It did not cause the recorded test run to fail."),
    P("Scope and limitations", "Heading2"),
    P("This is a record of the backend automated test run only. It does not confirm "
      "Android installation, mobile-to-backend connectivity, or completion of every "
      "assignment requirement."),
    P("Evidence to retain", "Heading2"),
    P("Attach a screenshot of the actual terminal output showing the test command and "
      "result. Rerun the tests before submission if the code has changed since this run.")
]
make_pdf(EVIDENCE / "TEST_LOG.pdf", test_story)

# 4. FEEDBACK TEMPLATE — intentionally contains no invented responses
feedback = [
    P("AgriSoko Pocket G06", "Title"),
    P("User Testing and Feedback Form", "Heading1"),
    P("Use this form during a real test of the application. The tester should complete "
      "it honestly after trying the app. Do not fill it with invented feedback."),
    Spacer(1, 5*mm),
    P("Tester name or anonymous identifier: __________________________________"),
    Spacer(1, 4*mm),
    P("Date of test: ____________________   Device / Android version: ____________________"),
    Spacer(1, 5*mm),
    P("Test performed", "Heading2"),
    P("Search query entered: __________________________________________________"),
    Spacer(1, 4*mm),
    P("What happened? _______________________________________________________"),
    Spacer(1, 8*mm),
    P("Feedback questions", "Heading2"),
    P("1. Was the app easy to understand?  Yes / No / Partly"),
    Spacer(1, 4*mm),
    P("Comments: ___________________________________________________________"),
    Spacer(1, 6*mm),
    P("2. Did the search result appear relevant?  Yes / No / Partly / Not tested"),
    Spacer(1, 4*mm),
    P("Comments: ___________________________________________________________"),
    Spacer(1, 6*mm),
    P("3. Did you encounter an error or confusing behaviour?  Yes / No"),
    Spacer(1, 4*mm),
    P("Details: ______________________________________________________________"),
    Spacer(1, 6*mm),
    P("4. What improvement would you recommend?"),
    Spacer(1, 4*mm),
    P("______________________________________________________________________"),
    Spacer(1, 4*mm),
    P("______________________________________________________________________"),
    Spacer(1, 8*mm),
    P("Group member who observed the test: ___________________________________"),
    Spacer(1, 5*mm),
    P("Evidence captured (screenshot / notes): _________________________________"),
    Spacer(1, 8*mm),
    P("Status: Blank template — genuine tester feedback still needs to be collected.")
]
make_pdf(EVIDENCE / "FEEDBACK.pdf", feedback)

print("PDF files created:")
for path in [
    DOCS / "COMBO_A3_G06_REPORT.pdf",
    EVIDENCE / "CONTRIBUTIONS.pdf",
    EVIDENCE / "TEST_LOG.pdf",
    EVIDENCE / "FEEDBACK.pdf",
]:
    print(f"{path} | {path.stat().st_size:,} bytes")
