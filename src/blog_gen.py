def assemble_blog_post(title, sections, images, videos):
    blog_post = f"# {title}\n\n"
    
    for section, content in sections.items():
        blog_post += f"## {section}\n\n{content}\n\n"
    
    # Embed images and videos
    for img in images:
        blog_post += f"![{img['alt']}]({img['path']})\n\n"
    for vid in videos:
        blog_post += f"[Video: {vid['title']}]({vid['path']})\n\n"
    
    # Save as Markdown
    with open("output/final_blog_post.md", "w") as file:
        file.write(blog_post)

    print("Blog post assembled and saved as final_blog_post.md")
    return blog_post

# Example Usage
if __name__ == "__main__":
    title = "Exploring Generative AI for 2025"
    sections = {
        "Introduction": "Introduction to generative AI advancements.",
        "Key Insights": "Detailed discussion on the latest technologies."
    }
    images = [{"alt": "AI Trends", "path": "output/infographic.png"}]
    videos = [{"title": "AI Overview", "path": "output/generated_avatar_video.mp4"}]
    
    assemble_blog_post(title, sections, images, videos)
