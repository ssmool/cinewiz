import requests
import sys

# --- Configuration ---
# IMPORTANT: Replace these with your actual credentials
API_KEY = "YOUR_GOOGLE_API_KEY"
CX = "YOUR_CUSTOM_SEARCH_ENGINE_CX"
# ---------------------

def google_image_search(keyword, num_results=10):
    """
    Searches Google Images via the Custom Search Engine API and prints
    results to the console in a numbered, field-separated format.
    """
    if API_KEY == "YOUR_GOOGLE_API_KEY" or CX == "YOUR_CUSTOM_SEARCH_ENGINE_CX":
        print("🚨 ERROR: Please configure API_KEY and CX with your actual Google credentials.")
        print("   - API Key: Get from Google Cloud Console.")
        print("   - CX ID: Get from Google Custom Search Engine.")
        return

    print(f"Searching Google Images for: '{keyword}'...")
    print("-" * 30)

    try:
        # Google Custom Search API endpoint
        url = "https://www.googleapis.com/customsearch/v1"
        
        # API request parameters
        params = {
            'key': API_KEY,
            'cx': CX,
            'q': keyword,
            'searchType': 'image', # Essential parameter for image search
            'num': num_results
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        
        data = response.json()

        if 'items' not in data:
            # The 'items' key is missing if no results are found
            print(f"No image results found for '{keyword}'.")
            return

        photos = data['items']
        
        print(f"Displaying first {len(photos)} results:")
        print("=" * 30)
        
        # Iterate over the results and print them in the requested format
        for i, item in enumerate(photos):
            image_info = item.get('image', {})
            
            # 1. Numbered List and Title Field
            print(f"\n{i+1}. 🖼️ Source Title: **{item.get('title', 'No Title')}**")
            
            # 2. Item info separated by fields
            print(f"   Image URL: {item.get('link', 'N/A')}")
            print(f"   Context Page: {image_info.get('contextLink', 'N/A')}")
            print(f"   Dimensions: {image_info.get('width', 'N/A')}px x {image_info.get('height', 'N/A')}px")
            print(f"   File Size: {image_info.get('byteSize', 'N/A')} bytes")

    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during the API request. Check your key/CX or connection: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python google_search_images.py <keyword>")
        sys.exit(1)
    
    # Get the keyword from command line arguments (joining multiple words)
    search_keyword = " ".join(sys.argv[1:])
    
    # Set the maximum number of results to display (max is 10 per API call)
    RESULTS_LIMIT = 10
    
    google_image_search(search_keyword, RESULTS_LIMIT)
