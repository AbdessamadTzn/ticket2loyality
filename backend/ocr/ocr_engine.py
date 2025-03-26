from paddleocr import PaddleOCR

# Clearly initialize OCR engine only once here
ocr = PaddleOCR(use_angle_cls=True, lang="fr")
