from text_gen import generate_blog_post
from video_gen import create_avatar_video
from avatar_gen import create_did_avatar_video
from image_gen import generate_dalle_image
from blog_gen import assemble_blog_post
from utils import ensure_directory_exists
from conversation_engine import get_conversational_response
from utils import ensure_directory_exists

def generate_full_content_pipeline(topic):
    ensure_directory_exists("output")

    # Step 1: Generate Blog Text
    sections = {
        "Introduction": generate_blog_post(topic, structure=["Introduction"]),
        "Key Points": generate_blog_post(topic, structure=["Key Points"]),
    }

    # Step 2: Create Video with Avatar
    create_avatar_video("This is a video introduction for the topic.", avatar_id="AI_Tutor")

    # Step 3: Generate Infographic
    generate_dalle_image(topic)

    # Step 4: Assemble into Blog Post
    images = [{"alt": f"{topic} Infographic", "path": "output/dalle_image.png"}]
    videos = [{"title": f"{topic} Video Intro", "path": "output/generated_avatar_video.mp4"}]
    assemble_blog_post(f"Deep Dive into {topic}", sections, images, videos)

def generate_avatar_interaction(query):
    ensure_directory_exists("output/avatar_videos")

    # Step 1: Generate Conversational Response
    response_text = get_conversational_response(query)
    print("Generated Response:", response_text)

    # Step 2: Generate Avatar Video with D-ID
    create_did_avatar_video(response_text, output_filename="output/avatar_videos/did_avatar_video.mp4")

# Example usage
if __name__ == "__main__":
    generate_full_content_pipeline("Generative AI Trends in 2025")
