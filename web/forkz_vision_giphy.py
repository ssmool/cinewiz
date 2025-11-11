import requests
import sys

# --- Configuration ---
# IMPORTANT: Replace this with your actual GIPHY API Key
# You can use the general 'GIPHY SDK Key' (often 'dc6zaTOxFJmzC') for testing, 
# but a personalized Beta Key is recommended.
API_KEY = "YOUR_GIPHY_API_KEY"
# ---------------------

def giphy_search(keyword, num_results=10):
    """
    Searches GIPHY for GIFs matching the keyword and prints the results
    to the console in a numbered, field-separated format.
    """
    if API_KEY == "YOUR_GIPHY_API_KEY":
        print("🚨 ERROR: Please configure API_KEY with your actual GIPHY credentials.")
        return

    print(f"Searching GIPHY for: '{keyword}'...")
    print("-" * 30)

    try:
        # GIPHY Search API endpoint
        url = "https://api.giphy.com/v1/gifs/search"
        
        # API request parameters
        params = {
            'api_key': API_KEY,
            'q': keyword,
            'limit': num_results,
            'rating': 'g', # Restrict to 'G' rated content
            'lang': 'en'
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        
        data = response.json()

        if 'data' not in data or not data['data']:
            print(f"No GIFs found for '{keyword}'.")
            return

        gifs = data['data']
        
        print(f"Displaying first {len(gifs)} results:")
        print("=" * 30)
        
        # Iterate over the results and print them in the requested format
        for i, gif in enumerate(gifs):
            # The GIPHY API provides a 'url' (GIPHY page) and 'images' (direct file links)
            
            # 1. Numbered List and Title Field
            print(f"\n{i+1}. 🖼️ Title/Slug: **{gif.get('title', 'No Title')} / {gif.get('slug', 'N/A')}**")
            
            # 2. Item info separated by fields
            print(f"   GIF ID: {gif.get('id', 'N/A')}")
            print(f"   Username: {gif.get('username', 'Anonymous') if gif.get('username') else 'Anonymous'}")
            print(f"   Imported: {gif.get('import_datetime', 'N/A')}")
            
            # Direct link to the image file (using a standard medium size)
            if 'images' in gif and 'original' in gif['images']:
                print(f"   Direct URL: {gif['images']['original']['url']}")
            else:
                print(f"   GIPHY Page: {gif.get('url', 'N/A')}")


    except requests.exceptions.RequestException as e:
        print(f"❌ An error occurred during the API request. Check your key or connection: {e}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# --- Main execution block ---
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python giphy_search.py <keyword>")
        sys.exit(1)
    
    # Get the keyword from command line arguments (joining multiple words)
    search_keyword = " ".join(sys.argv[1:])
    
    # Set the number of results to display
    RESULTS_LIMIT = 5 
    
    giphy_search(search_keyword, RESULTS_LIMIT)
