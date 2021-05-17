from docCreator import create_schema_and_load_docs
from search import write_results

if __name__ == '__main__':
    create_schema_and_load_docs()

    print("Welcome to Beauty Regimen! \nWe will try and give you the best possible regimen for your skin concerns\n"
          "Tell us your current skin concerns or search for product types: ")
    input_query = input()
    print("Please provide a location folder where the results will be stored: ")
    file_destination = input()
    search_query = input_query.split(" and ")

    # perform search and write results
    write_results(search_query, file_destination, input_query)
