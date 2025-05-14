from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


pdfmetrics.registerFont(TTFont('Poppins', 'Poppins-Regular.ttf'))

# File setup
file_name = "Resume_Prateek_Yadav.pdf"
c = canvas.Canvas(file_name, pagesize=A4)
width, height = A4

# Layout setup
margin = 50
column_gap = 20
left_width = 0.65 * (width - 2 * margin)
right_width = 0.4 * (width - 2 * margin)

left_x = margin
right_x = margin + left_width + column_gap

# Colors
heading_color = colors.HexColor("#005A9C")  # blue
text_color = colors.HexColor("#102E50")     # dark gray
other_color = colors.HexColor('#60B5FF')

# === Optional: Add background images ===
# Replace with your image paths if you have them
top_image = "top.png"
bottom_image = "bottom.png"
c.drawImage(top_image, 0, height - 100, width=width, height=100, mask='auto')
c.drawImage(bottom_image, 0, 0, width=width, height=100, mask='auto')

# Font setup
c.setFillColor(heading_color)
c.setFont("Poppins", 24)
c.drawString(margin, height - 50, "PRATEEK YADAV")

c.setFillColor(other_color)
c.setFont("Poppins", 14)
c.drawString(margin, height - 67, "Python Developer")

# Contact info
c.setFont("Helvetica", 10)
c.setFillColor(text_color)
contact = "Phone: +91-9956049122 | Email: prateekya23@email.com | Portfolio: prateek-portfolio.onrender.com | Kanpur, U.P"
c.drawString(margin, height - 83, contact)

# Independent vertical trackers
y_left = height - 105
y_right = height - 105

# === Style for paragraphs ===
styles = getSampleStyleSheet()
para_style = styles["Normal"]
para_style.fontName = "Helvetica"
para_style.fontSize = 9
para_style.textColor = text_color
para_style.leading = 12

def draw_paragraph(text, x, y, max_width):
    para = Paragraph(text, para_style)
    w, h = para.wrap(max_width, y)
    para.drawOn(c, x, y - h)
    return h


# LEFT COLUMN: 70%
def draw_left_section(title, heading,  lines, spacing=5):
    global y_left
    c.setFont("Helvetica", 7)
    # c.setFillColor(heading_color)
    c.drawString(left_x, y_left, title)
    
    y_left -= 15
    c.setFont("Helvetica", 14)
    c.setFillColor(heading_color)
    c.drawString(left_x, y_left, heading)
    
    y_left -= spacing
    c.setFont("Helvetica", 9)
    c.setFillColor(text_color)
    for line in lines:
        # c.drawString(left_x, y_left, line)
        draw_paragraph(line, left_x, y_left, left_width)
        y_left -= 11
    y_left -= 20  # space after section
    
def draw_left_section_without_heading(title,  lines, spacing=5):
    global y_left
    c.setFont("Helvetica", 7)
    # c.setFillColor(heading_color)
    c.drawString(left_x, y_left, title)
    
    y_left -= spacing
    c.setFont("Helvetica", 9)
    c.setFillColor(text_color)
    for line in lines:
        # c.drawString(left_x, y_left, line)
        draw_paragraph(line, left_x, y_left, left_width)
        y_left -= 11
    y_left -= 20  # space after section

draw_left_section_without_heading("SUMMARY", [    
    "A strong background in Python for web crawling, scraping, and data",
    "automation. Proficient in using Python libraries such as <b>BeautifulSoup </b>, and",
    "<b>Selenium </b>to build efficient web crawlers and scrapers, extracting data from",
    "various websites including <b>Google Maps</b> and handling bulk email",
    "distribution. Skilled in developing custom web scraping solutions,",
    "automating repetitive tasks, and processing data from Excel and CSV files",
    "for enhanced accessibility and analysis.",
    "In addition to web scraping, I have hands-on experience with <b>Django</b> for",
    "building scalable web applications, and a basic understanding of <b>Express,</b>",
    "<b>Node.js</b>, and <b>API integration</b>. Currently working remotely as a <b>Front-End</b>",
    "Developer, where I focus on building responsive, user-friendly interfaces.",
    "Led the development cycle of a <b>cake delivery website</b>, covering <b>UI/UX</b>",
    "<b>design, database management (MongoDB, MySQL),</b> and API integration.",
    "Known for my strong problem-solving skills and optimizing code for",
    "performance and efficiency.",
])

draw_left_section("EXPERIENCE", "Frontend Developer", [
    "<font color='#60B5FF' >GrowUpNext</font>    10/2022 - Present    Kanpur, India",
    "It Based Company",
    "<b>• Frontend Development (Remote): </b>Currently working as a frontend",
    "  developer, designing and implementing responsive, user-friendly",
    "  interfaces for web applications.",
    "<b>• Web Scraping & Automation: </b>Leveraged Python for web scraping tasks,",
    "  including Google Maps API data extraction and bulk email distribution.",
    "<b>• Data Processing: </b>Built Python scripts to read and process data from",
    "  Excel and CSV files, improving data accessibility and analysis.",
    "<b>• Cake Delivery Website: </b>Leading the full development cycle of a cake",
    "  delivery website using Express, MongoDB, Node.js, including UI/UX",
    "  design, database management, and API integration.",
])

draw_left_section("INTERNSHIP","Jr. Python Developer", [
    "<font color='#60B5FF' >Karen Engineering Reality</font >    11/2024 - Present    Gurugram, Haryana",
    "Business Consulting Firm",
    "<b>• Web Crawling & Scraping: </b>Proficient in using Python libraries such as",
    "      BeautifulSoup, Scrapy, and Selenium to build automated web crawlers",
    "      and scrapers for data extraction from a variety of websites.",
    "<b>• Google Maps Data Extraction: </b>Built automation scripts to extract",
    "      business-related information, including emails, from Google Maps and",
    "      other websites, enhancing data collection efficiency.",
    "<b>• Custom Web Scraping Solutions: </b>Designed and implemented custom",
    "      scraping solutions to gather data from specific websites based on client",
    "      needs, ensuring accurate and relevant information.",
    "<b>• Data Automation: </b>Improved overall data handling and processing by",
    "      automating repetitive tasks, saving time and minimizing manual errors",
    "<b>• Problem Solving & Optimization: </b>Demonstrated strong problem-solving",
    "      skills by troubleshooting scraping issues and optimizing scripts for",
    "      speed and efficiency.",
])

draw_left_section("ACADEMIC PROJECT","SEP Doorstep", [
    "10/2022 - 04/2023",
    "Developed a complete e-commerce website using Django for back-end",
    "logic and HTML, CSS, and JavaScript for front-end development. The",
    "project features user authentication with session management, product",
    "management, and responsive design for optimal user experience.",
    "<b>• User Authentication: </b>Implemented user authentication with session",
    "      management, allowing secure user login, registration, and session",
    "      handling."
])

# RIGHT COLUMN: 30%
def draw_right_section(title, heading , items, spacing=5):
    global y_right
    c.setFont("Helvetica", 7)
    # c.setFillColor(heading_color)
    c.drawString(right_x, y_right, title)
    y_right -= 15
    
    c.setFont("Helvetica", 10)
    c.setFillColor(heading_color)
    c.drawString(right_x, y_right, heading)
    
    y_right -= 10
    
    c.setFont("Helvetica", 9)
    c.setFillColor(text_color)
    for item in items:
        
        c.drawString(right_x, y_right, f"{item}")
        y_right -= 10
    y_right -= 10  # space after section
    
def draw_right_section_Without_Heading(title, items, spacing=5):
    global y_right
    c.setFont("Helvetica", 7)
    # c.setFillColor(heading_color)
    c.drawString(right_x, y_right, title)
    y_right -= 15
    
    c.setFont("Helvetica", 10)
    c.setFillColor(text_color)
    for item in items:
        c.drawString(right_x, y_right, f"{item}")
        y_right -= 15
    y_right -= 10  # space after section

draw_right_section_Without_Heading("SKILLS", [
    "Python     Django     Flask ", 
    "HTML     CSS     JavaScript",
    "Pandas     MongoDB     MySQL"
])

draw_right_section("EDUCATION", "Master Of Computer Application (MCA)", [
    "Dr. A.P.J. Abdul Kalam Technical University",
    "08/2022 - 05/2024 Lucknow"
])


def draw_right_section_without_Title( heading , items, spacing=5):
    global y_right
    
    c.setFont("Helvetica", 10)
    c.setFillColor(heading_color)
    for head in heading:
        c.drawString(right_x, y_right, head)
        y_right -= 10
        
    # y_right -= 5
    
    c.setFont("Helvetica", 9)
    c.setFillColor(text_color)
    for item in items:
        c.drawString(right_x, y_right, f"{item}")
        y_right -= 10
    y_right -= 10  # space after section
    
draw_right_section_without_Title(["Bachelor of Science (B.Sc)"], [
    "Chhatrapati Shahu Ji Maharaj University",
    "08/2019 - 05/2022 Kanpur"
])

draw_right_section("CERTIFICATIONS", "Certificate Of Computer Application", [
    "GGES Education Group",
    "08/2023",
])

draw_right_section_without_Title( ["Certificate in Computer Application","Business accounting and multilingual", "DTP"], [
    "NIELIT",
    "07/2023",
])

draw_right_section_without_Title( ["Certificate in SQL for Beginners"], [
    "Scaler",
    "04/2024",
])


draw_right_section("LINKS", "github.com/prateek-gith", [
])
draw_right_section_without_Title(["linkedin.com/in/prateek-yadav-46b3882a3"], [
])

draw_right_section("LANGUAGES", "Hindi", [
])
draw_right_section_without_Title(["English"], [
])

# Save PDF
c.save()
print("Resume PDF Create")
