import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import base64
from io import BytesIO

# Add this function at the top of your file
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Set page config to wide layout
st.set_page_config(layout="wide")

# Add custom CSS for max-width on body
st.markdown("""
<style>
    .main {
        max-width: 1400px;  /* Set your desired max-width */
        margin: 0 auto;     /* Center the content */
    }
    .rounded-image img {
        border-radius: 15px;
        object-fit: cover;
    }
    .card-container {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 2rem;
    }
    .profile-card {
        max-height: 200px;
        width: 450px;
        border-radius: 0.75rem;
        border: 1px solid #334155;
        background-color: #1e293b;
        display: flex;
        align-items: center;
        gap: 1.25rem;
        padding: 1.25rem;
        transition: transform 0.3s;
    }
    .profile-card:hover {
        transform: scale(1.025);
        cursor: pointer;
    }
    .avatar {
        width: 100px !important;
        height: 100px !important;
        border-radius: 100%;
        overflow: hidden;
        border: 2px solid #475569;
        background: #e9e9e9;
    }
    .avatar img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .profile-info {
        color: #f8fafc;
    }
    .profile-info p:first-child {
        font-size: 1.25rem;
        margin-bottom: 0.25rem;
    }
    .profile-info p:nth-child(2) {
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
    }
    .project-count {
        display: inline-block;
        background-color: #dbeafe;
        color: #1e40af;
        padding: 0.25rem 0.625rem;
        border-radius: 0.25rem;
        font-size: 0.875rem;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Check if 'selected_menu' is already in the session state
if 'selected_menu' not in st.session_state:
    selected_menu = "Overview"

# Sidebar navigation using buttons
menu_options = ["Overview", "Personal", "Work / Business", "Contact"]

# Horizontal menu
selected_menu = option_menu(None, menu_options, 
    icons=['house', 'person', 'briefcase', 'envelope'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

# Display content based on selected menu
if selected_menu == "Overview":
    st.header("Overview")
    
    # Profile image with rounded corners and centered
    try:
        st.markdown(f'''
            <div style="display: flex; justify-content: center; align-items: center;">
                <div style="width: 150px; height: 150px; border-radius: 50%; overflow: hidden;">
                    <img src="https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/socials/jim_profile.jpg" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
            </div>
        ''', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("Profile image not found. Please check the file path.")
    except Exception as e:
        st.error(f"An error occurred while loading the image: {e}")
    
    # Centered full name and title with improved styling
    st.markdown('<h2 style="text-align: center; font-size: 2rem; color: #3b82f6;">James Alein R. Ocampo</h2>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center; font-size: 1.5rem; color: #94a3b8;">BSIT-4 Student</h3>', unsafe_allow_html=True)
    
    # Justified long texts
    st.markdown("<p style='text-align: justify;'>Hello, I'm James, a BSIT-4 student with a passion for technology and entrepreneurship. Over the past few years, I've immersed myself in the world of software development, turning ideas into functional, user-friendly solutions. My journey started with a curiosity about how things work, which quickly evolved into a career path that blends creativity, technical skill, and a drive for innovation.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>As an entrepreneur, I've been involved in multiple side projects that challenge me to think outside the box and solve real-world problems. These projects have not only expanded my skill set but have also given me valuable insights into the fast-paced world of tech startups.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>In addition to my studies and entrepreneurial ventures, I've freelanced as a Full Stack Web Developer, where I've had the privilege to work with clients from various industries. This experience has sharpened my ability to deliver high-quality web solutions, from front-end design to back-end development.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>I'm also the owner of a low-key software company, where I oversee projects that range from simple web applications to complex systems. This role has taught me the importance of leadership, time management, and the ability to adapt quickly to new challenges.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: justify;'>Looking ahead, my goal is to leverage my skills and experiences to make a meaningful impact on the lives of many people. I'm driven by a passion for creating innovative solutions that can improve the way we live and work, and I'm excited about the opportunities the future holds.</p>", unsafe_allow_html=True)
    
    # Create two profile cards
    st.markdown("<h2 style='text-align: center;'>Schools Attended</h2>", unsafe_allow_html=True)

    cards_html = """
    <div class="card-container">
        <div class="profile-card">
            <div class="avatar">
                <img src="https://usjr.edu.ph/wp-content/uploads/2016/05/USJR1.png"  alt="Profile">
            </div>
            <div class="profile-info">
                <p>University of San Jose - Recoletos</p>
                <span class="project-count">SY 2009-2019</span>
            </div>
        </div>
        <div class="profile-card">
            <div class="avatar">
                <img src="https://the-post-assets.sgp1.digitaloceanspaces.com/2020/10/Cebu-Institute-of-Technology-University.jpg" alt="Profile">
            </div>
            <div class="profile-info">
                <p>Cebu Institute of Technology - University</p>
                <span class="project-count">SY 2019 - 2025</span>
            </div>
        </div>
    </div>
    """

    st.markdown(cards_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # Add space after Overview section

elif selected_menu == "Personal":
    st.header("Personal")
    st.write("I'm a man of many hobbies because I love to explore new things and dive deep into anything that piques my curiosity. Whether it's traveling to new places, immersing myself in music, learning about business strategies, or staying up-to-date with the latest in technology, I find joy in constantly expanding my horizons.")

    # About Me Section
    st.subheader("About Me")

    # Array of data for About Me section
    about_me_data = [
        {
            "title": "Traveling",
            "icon": "✈️", 
            "description": "Exploring new places, cultures, and cuisines keeps me inspired and broadens my perspective on life."
        },
        {
            "title": "Music",
            "icon": "🎵", 
            "description": "Music fuels my creativity and provides me with a sense of relaxation. I enjoy both listening to and discovering new genres."
        },
        {
            "title": "Business",
            "icon": "💼",
            "description": "I have a strong passion for entrepreneurship. I love learning about market trends and creating innovative business strategies."
        },
        {
            "title": "Technology",
            "icon": "💻", 
            "description": "Technology is a big part of my life. I'm fascinated by how it evolves and continues to shape the future of our world."
        }
    ]

    # Create About Me section using Streamlit columns
    cols = st.columns(4)
    for i, item in enumerate(about_me_data):
        with cols[i % 4]:
            st.markdown(f"<h1 style='text-align: center; font-size: 3rem;'>{item['icon']}</h1>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center;'>{item['title']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align: center; font-size: 0.9rem;'>{item['description']}</p>", unsafe_allow_html=True)

    # Gallery Section with Flex Wrap
    st.subheader("Gallery")
    st.write("Here, you'll find a collection of images that capture my experiences, projects, and moments that inspire me. Each image tells a story and reflects my journey through various interests and endeavors.")

    # Import os module to work with file paths
    import os

    # Get all image files from the gallery folder
    gallery_folder = "images/gallery"
    gallery_images = [f for f in os.listdir(gallery_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Create 3-column grid for gallery
    col1, col2, col3 = st.columns(3)
    
    for i, image_file in enumerate(gallery_images):
        with [col1, col2, col3][i % 3]:
            image_path = os.path.join(gallery_folder, image_file)
            st.image(image_path, use_column_width=True)
    st.markdown("<br>", unsafe_allow_html=True)  # Add space after Personal section

elif selected_menu == "Work / Business":
    st.header("Work/Business")
    st.write("I'm a visionary with a passion for turning ideas into reality. Over the years, I've freelanced as a Full Stack Web Developer, founded my own software company, and created various digital projects that reflect my drive for innovation. My work spans from building client-focused web solutions to launching platforms that push the boundaries of technology and user experience. This section highlights my journey, showcasing the key ventures that define my professional and entrepreneurial path.")
    
    
    
    # Personal Projects
    st.subheader("Personal Projects")
    col1, col2, col3 = st.columns(3)
    
    projects = [
        {
            "name": "JimTech Solutions",
            "description": "A web solutions agency that focuses on creating software as a service businesses.",
            "status": "Active",
            "status_color": "#00FF00",
            "icon": "https://www.jimtech.solutions/favicon.ico",
            "url": "https://www.jimtech.solutions"
        },
        {
            "name": "MrJim Development",
            "description": "My freelancing portfolio as a Full Stack Web Developer, showcasing various web development projects and services.",
            "status": "Active",
            "status_color": "#00FF00",
            "icon": "https://mrjim.dev/src/img/favicon.png", 
            "url": "https://mrjim.dev" 
        },
        {
            "name": "ChitChat",
            "description": "ChitChat brings you closer to your loved ones through fun, thought-provoking games and questions.",
            "status": "Active",
            "status_color": "#00FF00",
            "icon": "https://chitchat.cards/favicon.ico",
            "url": "https://chitchat.cards"
        },
        {
            "name": "Flexmo",
            "description": "Flex your projects and collaborations to elevate your online presence.",
            "status": "Active",
            "status_color": "#00FF00",
            "icon": "https://www.flexmo.io/images/flexmo.png",
            "url": "https://www.flexmo.io"
        },
        {
            "name": "Featurize",
            "description": "Give Your Users a Voice and Elevate Your Product! Featurize is the ultimate platform that enables startups, software developers, and businesses to seamlessly set up a feature request system.",
            "status": "Active",
            "status_color": "#00FF00",
            "icon": "https://www.featurize.io/logo.png",  # Assuming the favicon exists at this URL
            "url": "https://featurize.io"
        },
        {
            "name": "TemplatePod",
            "description": "Discover a curated collection of cutting-edge, developer-friendly templates built on the latest frameworks and libraries.",
            "status": "On hold",
            "status_color": "#3399FF",
            "icon": "https://templatepod.com/favicon.ico",
            "url": "https://templatepod.com"
        },
        
        {
            "name": "MemoVault",
            "description": "A platform dedicated to saving and cherishing the memories of loved ones.",
            "status": "On hold",
            "status_color": "#3399FF",
            "icon": "https://img.icons8.com/color/48/000000/memory.png",  # Placeholder icon
            "url": "#"  # Assuming this is the URL
        },
    ]


    for i, project in enumerate(projects):
        with [col1, col2, col3][i % 3]:
            st.markdown(f"""
            <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <img src="{project['icon']}" style="width: 24px; height: 24px; margin-right: 10px;">
                    <h3 style="color: #FFFFFF; margin: 0;">{project['name']}</h3>
                </div>
                <p style="color: #CCCCCC; font-size: 14px;">{project['description']}</p>
                <div style="display: flex; gap: 10px;">
                    <span style="color: {project['status_color']};">● {project['status']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Client Projects
    st.subheader("Client Projects")
    col1, col2, col3 = st.columns(3)
    
    client_projects = [
        {
            "name": "CryptoCino - Crypto-Betting HTML5 Template",
            "description": "CryptoCino is an HTML5 template for building professional crypto-betting sites. This template has been carefully crafted to provide a seamless and intuitive user experience, with a modern and stylish design that is sure to impress.",
            "status": "Completed",
            "status_color": "green",
            "image": "https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/projects/thumbnail/CryptoCino-Thumbnail-large.png"
        },
        {
            "name": "HostCamp - Web Hosting HTML5 Template",
            "description": "HostCamp is a high-quality hosting template ideal for any hosting company or business. The template features a modern style and a professional appearance. It's a simple-to-use, mobile-friendly, SEO-friendly domain hosting template.",
            "status": "Completed",
            "status_color": "green",
            "image": "https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/projects/thumbnail/HostCamp-Thumbnail_scaled.png"
        },
        {
            "name": "MyLinks - Creator's Profile",
            "description": "Put together all your social links on one page with MyLinks. Show your followers your aesthetic custom profile page that could serve as a landing page.",
            "status": "Completed",
            "status_color": "green",
            "image": "https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/projects/thumbnail/MyLinks_Scaled_Thumbnail.png"
        },
        {
            "name": "Visualry Designs",
            "description": "Visualry Designs was a captivating web development project that aimed to showcase the exceptional talent of a skilled graphic designer.",
            "status": "Completed",
            "status_color": "green",
            "image": "https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/projects/thumbnail/VisualryDesigns.png"
        },
        {
            "name": "Online Attendance",
            "description": "Online Attendance is a comprehensive management dashboard designed to simplify and enhance the process of tracking class attendance.",
            "status": "Completed",
            "status_color": "green",
            "image": "https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/projects/thumbnail/attendees.png"
        },
        {
            "name": "Red Star Profiles",
            "description": "Red Star Profiles is a groundbreaking Sports Events Management System tailored to the Canadian sports landscape. This comprehensive platform empowers convenors, coaches, players, and schools to seamlessly organize, coordinate, and participate in sports events.",
            "status": "Completed",
            "status_color": "green",
            "image": "https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/projects/thumbnail/RedStarProfiles-Mockup-min.png"
        },
        {
            "name": "KetoPlans",
            "description": "Ketoplans is a groundbreaking online platform dedicated to the world of Indian Keto Ingredients and Recipes.",
            "status": "Completed",
            "status_color": "green",
            "image": "https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/projects/thumbnail/KetoPlans-compressed.png"
        },
        {
            "name": "National Justice Museum",
            "description": "The National Justice Museum is a remarkable school project that showcases the power of HTML and CSS in creating a visually engaging and informative website.",
            "status": "Completed",
            "status_color": "green",
            "image": "https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/projects/thumbnail/NJM_Mockup-min.png"
        },
        {
            "name": "NBUGOS Portfolio",
            "description": "NBUGOS Portfolio is an exceptional showcase of the work and expertise of a Full Stack MERN (MongoDB, Express.js, React, Node.js) Developer.",
            "status": "Completed",
            "status_color": "green",
            "image": "https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/projects/thumbnail/NBUGOS-min.png"
        }
    ]



    for i, project in enumerate(client_projects):
        with [col1, col2, col3][i % 3]:
            st.markdown(f"""
            <div style="background-color: #1E1E1E; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
                <img src="{project['image']}" style="width: 100%; border-radius: 5px; margin-bottom: 10px;">
                <h3 style="color: #FFFFFF; margin: 0;">{project['name']}</h3>
                <p style="color: #CCCCCC; font-size: 14px;">{project['description']}</p>
                <div style="display: flex; gap: 10px;">
                    <span style="color: {project['status_color']};">● {project['status']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # Add space after Work/Business section

elif selected_menu == "Contact":
    st.markdown("""
    <style>
    .contact-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 2rem;
        background-color: #0f172a;
        border-radius: 10px;
    }
    .profile-image-container {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        overflow: hidden;
        margin-bottom: 1rem;
    }
    .profile-image-container img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .contact-info {
        text-align: center;
    }
    .social-links {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin: 1rem 0;
    }
    .social-link {
        background-color: #1e293b;
        color: #94a3b8;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        text-decoration: none;
        font-size: 20px;
    }
    .other-link {
        background-color: #1e293b;
        color: #94a3b8;
        text-decoration: none;
        padding: 10px 20px;
        border-radius: 5px;
        display: block;
        margin-bottom: 10px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown('''
            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center;">
                <div style="width: 150px; height: 150px; border-radius: 50%; overflow: hidden;">
                    <img src="https://gtzjphqvqypihgwyvbrl.supabase.co/storage/v1/object/public/socials/jim_profile.jpg" style="width: 100%; height: 100%; object-fit: cover;">
                </div>
                <div class="contact-info" style="text-align: center;">
                    <h1 style='color: #3b82f6; font-size: 24px;'>JAMES OCAMPO</h1>
                    <p style='color: #94a3b8; font-size: 16px;'>FOUNDER & ENTREPRENEUR</p>
                </div>
            </div>
        ''', unsafe_allow_html=True)

        social_links = [
            {"icon": "🌐", "url": "https://jimtech.solutions"},
            {"icon": "f", "url": "#"},
            {"icon": "x", "url": "#"},
            {"icon": "🪪", "url": "https://www.linkedin.com/in/james-alein-ocampo-8b3478245/"},
            {"icon": "✉️", "url": "mailto:jarocampooo@gmail.com"},
        ]

        st.markdown('<div class="social-links">' + 
                    ''.join([f'<a href="{link["url"]}" class="social-link">{link["icon"]}</a>' for link in social_links]) + 
                    '</div>', unsafe_allow_html=True)

        st.markdown("<h3 style='text-align: center; color: #94a3b8; margin-top: 1rem;'>OTHER LINKS</h3>", unsafe_allow_html=True)

        other_links = [
            {"name": "JimTech Solutions", "url": "https://jimtech.solutions"},
            {"name": "MrJim Development", "url": "https://mrjim.dev"},
            {"name": "Flexmo", "url": "https://www.flexmo.io"},
            {"name": "Featurize", "url": "https://featurize.io"},
        ]

        for link in other_links:
            st.markdown(f'<a href="{link["url"]}" class="other-link">{link["name"]}</a>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)  # Add space after Contact section
