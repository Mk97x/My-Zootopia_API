# Website Generator - Generates HTML website from animal data
import data_fetcher

def load_html(filepath_to_html):
    """Loads HTML to put in the string"""
    with open(filepath_to_html, "r") as html:
        return html.read()

def write_new_html(html, content):
    """Takes read html document and content to replace the placeholder in html"""
    final_html = html.replace("__REPLACE_ANIMALS_INFO__", content)
    output_path = "animals.html"
    output_path = "/home/coder/zootopia_api/My-Zootopia_API/animals.html"  # this is only here for me - i need absolute paths in my ide
    with open(output_path, "w") as output_file:
        output_file.write(final_html)
    print("Website was successfully generated to the file animals.html.")

def get_details(data):
    """Reads data and builds a dict for every animal and puts it in a list 'animals'"""
    if not data:
        return []
    
    animals = []
    for animal in data:
        try:
            animal_info = {
                "name": animal.get("name", "Unknown"),
                "diet": animal.get("characteristics", {}).get("diet", "Unknown"),
                "location": ", ".join(animal.get("locations", ["Unknown"])),
                "type": animal.get("characteristics", {}).get("type", "Unknown"),
                "weight": animal.get("characteristics", {}).get("weight", "Unknown"),
                "lifespan": animal.get("characteristics", {}).get("lifespan", "Unknown"),
                "skin_type": animal.get("characteristics", {}).get("skin_type", "Unknown"),
            }
            animals.append(animal_info)
        except Exception as e:
            print(f"Error processing animal data: {e}")
    return animals

def format_animal_details(details):
    """Formats data from get_details to HTML list items"""
    if not details:
        return ""
    
    animal_details_string = '<ul class="cards">\n'
    
    for animal in details:
        animal_details_string += '  <li class="cards__item">\n'
        animal_details_string += f'    <div class="card__title">{animal["name"]}</div>\n'
        animal_details_string += '    <div class="card__text">\n'
        animal_details_string += '      <ul class="card__details">\n'
        for key, value in animal.items():
            if key != "name":
                animal_details_string += f'        <li class="card__detail-item"><strong>{key.capitalize()}:</strong> {value}</li>\n'
        animal_details_string += '      </ul>\n'
        animal_details_string += '    </div>\n'
        animal_details_string += '  </li>\n'
    
    animal_details_string += '</ul>'
    return animal_details_string

def create_error_message(animal_name):
    """Creates a simple error message when no animal is found"""
    return f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'

def get_user_input_for_animal():
    """Gets animal name from user"""
    while True:
        animal_name = input("Enter a name of an animal: ").strip()
        if animal_name:
            return animal_name
        else:
            print("Please enter a valid animal name.")

def main():
    filepath_to_html = "animals_template.html"
    filepath_to_html = "/home/coder/zootopia_api/My-Zootopia_API/animals_template.html"  # this is only here for me - i need absolute paths in my ide

    try:
        animal_name = get_user_input_for_animal()
        data = data_fetcher.fetch_data(animal_name) # Fetch data using the data_fetcher module
        html = load_html(filepath_to_html)
        
        if data and len(data) > 0:  # if data for animal input is found
            details = get_details(data)
            
            if details:  # if details are parsed
                formatted_details = format_animal_details(details)
                write_new_html(html, formatted_details)
            else:  # if data somehow is not parsed correctly
                error_content = create_error_message(animal_name)
                write_new_html(html, error_content)
        else:  # if no animal matches found
            error_content = create_error_message(animal_name)
            write_new_html(html, error_content)

    except FileNotFoundError as e:
        print(f"Error: HTML template file not found - {e}")
        print("Make sure 'animals_template.html' exists in the current directory.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()