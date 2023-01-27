from pdf2image import convert_from_path
import pytesseract
import util
from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nitish.panda\AppData\Local\Tesseract-OCR\tesseract.exe'


def extract(file_path, file_format):
    pages = convert_from_path(file_path)
    document_text = ""
    if len(pages)>0:
        page = pages[0]
        processed_image = util.process_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text = "/n" + text

    if file_format == "patient_details":
        extracted_data = PatientDetailsParser(document_text).parse()
    elif file_format == "prescription":
        extracted_data = PrescriptionParser(document_text).parse()
    else :
        raise Exception(f'Invalid document format : {file_format}')
    return extracted_data


if __name__ == "__main__":
    data = extract("../resources/patient_details/pd_2.pdf", 'patient_details')
    print(data)
