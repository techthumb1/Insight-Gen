import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# D-ID API key
DID_API_KEY = os.getenv("DID_API_KEY")

def create_did_avatar_video(response_text, avatar_id="default", output_filename="output/avatar_videos/did_avatar_video.mp4"):
    """
    Generates a video using the D-ID API where an avatar speaks the provided text.
    :param response_text: The text for the avatar to speak.
    :param avatar_id: The ID or preset name of the avatar (provided by D-ID).
    :param output_filename: The file path to save the output video.
    """
    # Define D-ID API endpoint and headers
    url = "https://api.d-id.com/v1/talks"
    
    # Ensure DID_API_KEY is loaded correctly
    if DID_API_KEY is None:
        print("Error: DID_API_KEY is not set. Check your .env file.")
        return None

    # Use the API key as a Bearer token in the Authorization header
    headers = {
        "Authorization": f"Bearer {DID_API_KEY}",
        "Content-Type": "application/json"
    }

    # Payload with text and avatar settings
    payload = {
        "script": {
            "type": "text",
            "input": response_text,
            "provider": {"type": "d-id"}
        },
        "avatar": {
            "preset": avatar_id
        },
        "config": {
            "stitch": True
        }
    }

    # Send request to D-ID API
    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        # Get the URL of the generated video
        video_url = response.json().get("result_url")

        # Download and save the video
        video_data = requests.get(video_url).content
        with open(output_filename, "wb") as video_file:
            video_file.write(video_data)

        print(f"Avatar video saved to {output_filename}")
        return output_filename
    elif response.status_code == 401:
        print("Error: Unauthorized. Check your API key.")
    elif response.status_code == 403:
        print("Error: Forbidden. This typically indicates a problem with the Authorization header.")
    else:
        print(f"Error creating D-ID avatar video: {response.status_code} - {response.text}")
    
    return None

# Run the function with a sample response text
if __name__ == "__main__":
    response_text = "Random Forest is a versatile algorithm for classification and regression tasks. It builds multiple decision trees and aggregates their results for better accuracy."
    create_did_avatar_video(response_text)
