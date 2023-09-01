from process_data import *
import zipfile
import logging


# Basic configuration for the logging system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%d-%m-%Y %H:%M:%S')


def extract_zip(zip_file, destination_path):
    """
    Extracts the contents of a ZIP archive to the specified destination path

    Args:
    - zip_file (str): The path to the ZIP archive file
    - destination_path (str): The directory where the contents of the ZIP archive will be extracted

    Returns:
    - None: The function extracts the ZIP contents but does not return a value.
    """
    try:
        with zipfile.ZipFile(zip_file, "r") as file_zip:
            file_zip.extractall(path=destination_path)
        logging.info("The ZIP file has been decompressed")

    except zipfile.BadZipFile:
        logging.error("The ZIP file is damaged or invalid")

    except Exception as e:
        logging.error(f"An exception was generated during the process. Exception: {str(e)}")


def main():

    zip_file = 'data/archive.zip'
    destination_path_zip = 'data'
    csv_path_file = 'data/50000 Sales Records.csv'

    # Zip file decompression
    extract_zip(zip_file, destination_path_zip)

    # Generate folder directory
    process_dataset_by_year_by_month(csv_path_file)


if __name__ == "__main__":
    main()