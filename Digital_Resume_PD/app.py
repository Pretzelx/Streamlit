
from pathlib import Path
import streamlit as st
from PIL import Image

#---PATH SETTINGS---

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css.css"
cv_file = current_dir / "Assets" / "Prerna_Duhan_CV_.pdf"
profile_pic = current_dir / "Assets" / "Prerna_Pic_copy.jpg"


#---GENERAL SETTINGS---

PAGE_TITLE = " Digstital Resume | Prerna Duhan "
PAGE_ICON = ":random:"
NAME = "Prerna Duhan"
DESCRIPTION = """
👩‍💻Tech savvy MSc. Medical Informatics Student, searching for an opportunity to hone my skills and gain professional experience in digital upskilling, digitization and data analaysis
"""
EMAIL = "duhanprerna11@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/prerna-duhan/",
    "GitHub": "https://github.com/Pretzelx",
}

#---LOAD CSS FILE, PDF & PROFILE PIC---

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown("<style>{}</style".format(f.read()), unsafe_allow_html=True)
with open(cv_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#---Image Settings---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=240)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄Download Resume",
        data=PDFbyte,
        file_name="prerna_duhan_cv.pdf",
        mime= "application"
        )
    st.write("📧",EMAIL)
    
#---SOCIAL--
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

#---EXPERIENCE & QUAIFICATIONS---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✅ Strong hands on experience and knowledge in MS Excel, PowerBI and Tableau
    - ✅ Programming Experience in Python and R 
    - ✅ Proficient with Microsoft, Google and Adobe Suite 
    - ✅ Team player displaying a strong sense of initiative on tasks 
    - ✅ 5 years of combined academic and professional experience extracting insights from data
    - ✅ Passionate about Real World Data, AI and Deep learning, and their applications in digitalization of industries$
    - 🌏 Global individual with strong communication and presentation skills
    - 🗣️ English (Native), German(B1-B2), French (A2), Hindi (Native)"""
)

#---SKILLS---
st.write("#")
st.subheader("Skills")
st.write(
    """
    - 💻 Programming: Python (Scikit-learn, Pandas, NumPy), R
    - 📊 Data Visualization: Power BI, Tableau, MS Excel
    - 🤖 Modelling: Logistic regression, Linear regression, Decision trees, SVM
    - 🧬 Bioinformatics: Sequence searching, protein database and genome browsers, phylogenetics, functional genomics, variation and disease studies, visualisation and clustering, network analysis, logical and metabolic modelling, biostatistics.
    - 🧪 Cheminformatics: DataWarrior, SureChEMBL, CAS Scifinder, RDKit and MCPairs. 
    """
)

#---CERTIFICATIONS---
st.write("#")
st.subheader("Certifications")
st.write(
    """
    - 📃 Good Clinical Practice (ICH-GCP), 09/2022
    - 📃 Finance Foundations, LinkedIn, 09/2021
    - 📃 Tobacco Product Regulation, WHO, 09/2020
    - 📃 Occupational Health and Safety for Health Workers, WHO, 09/2022
    """ )



#---WORK HISTORY---

st.write("#")
st.subheader("Work Experience")
st.write("---")

#---JOB 1---

st.write("💼CRO INTERN – FEASIBILITY AND DOCUMENT CURATION")
st.write("Easthorn Clinical Services | Cologne, Germany")
st.write("09/2022 – 11/2022")
st.write(
    """
    - ▶️ Performed feasibility studies with recruitment data, data management (eCRF setup and query management) and document management (Trial Master Files and Investigator site files). Additionally, I learned about safety submissions to regulatory authorities and ethics committees.
    - ▶️ Completed ICH-GCP (Good Clinical Practice) certification and Standard Operating Procedures (SOP) training. 
    - ▶️ Improved critical clinical research skills and gained experience in clinical trial operations, clinical protocol and study start up
"""
)

#---JOB 2---
st.write("💼NIBR INTERN")
st.write("Novartis Pharma AG | Basel, Switzerland")
st.write("09/2022 – 11/2022")
st.write(
    """
    - ▶️ Internship in the Clinical Sciences and Investigation (CS&I) department at the Novartis Institute of Biomedical Research (NIBR) where I prepared research scope documentation, a Clinical Protocol Sheet, and an Informed Consent Form (ICF) for a medical devices digital case study.
    - ▶️ Included a 2-week rotation exploring biomedical science research, chemical research, and finance. This piqued my interest in the business side of the industry.
    
    """
    )

#---EDUCATION---
st.write("#")
st.subheader("Education")
st.write("---")

#---EDUCATION 1---
st.write("🎓MSc. Medical Informatics")
st.write("The University of Applied Sciences and Arts (FHNW) | Basel, Switzerland")
st.write("09/2023 – Present")

#---EDUCATION 2---
st.write("🎓MSci. Biomedical Sciences")
st.write("The University of Manchester | Manchester, United Kingdom")
st.write("09/2018 – 06/2022")

#---PROJECTS---
st.write("#")
st.subheader("Academic Projects")
st.write("---")
st.write(
    """
    - 🔬Thesis: The Analysis of a Molecular Generator based on Matched-Molecular Pair Analysis, and explore its application in de novo Drug Design: 
        - Under the supervision of Dr. Andrew Leach (Division of Pharmacy and Optometry), analysed and trained a molecular generator, exploring its ability to predict a novel series of compounds using input training data from patent chemistry. 
        - Worked with two biological targets- Diacylglycerol Acyltransferase 1 (DGAT1) and Glucokinase.
        - Generated DGAT1 and Glucokinase molecules through Matched Molecular Pair Analysis and identified connections between current DGAT1 and Glucokinase patent literature.
    - 🔬Mechanism of Action and Efficacy of Agents Targeting the Interferon Pathway in the Treatment of Systemic Lupus Erythematosus; Supervisor - Prof. Ian Bruce (Chair of Rheumatology & Director of National Institute of Health Research Manchester)
    - 🔬The impact of caffeine and caffeine like cognitive enhancers on neural correlates (CA1 and CA3) of cognitive activity in acute mouse hippocampal slices in vitro; Supervisor - Dr. Jon Turner (Dept. of Neuroscience and Experimental Psychology). 
    """
)

st.write("#")
st.subheader("Activities, Volunteering and Other Interests")
st.write("---")

