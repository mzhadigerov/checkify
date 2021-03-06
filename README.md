# Installation

1. Go to your project directory (where this repository is cloned)
2. Go to `checkify` package (where `ocr` and `data` packages located).
3. Download `roberta-base.zip` from [here](https://zenodo.org/record/4599830/files/roberta-base.zip) and extract it to `models` package.
4. Download `Tesseract` from [here](Download Tesseract from https://github.com/UB-Mannheim/tesseract/wiki)
5. Substitute `tess.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"` in `.\checkify\ocr\ocr.py` with `path\to\your\tesseract.exe`.
6. Download all the neccesary libraries from `toml` file.
7. Run `preparation.sh` (make sure that you have `nltk` downloaded).

# Test

`python .\main.py check-contract --path=test_file.pdf`

# Description

![Diagram](https://user-images.githubusercontent.com/55549813/126024422-ede64a36-b7ac-423a-a9f5-deb29d733385.png)

This program adds OCR layer upon [robera-base model](https://zenodo.org/record/4599830#.YPJSk-hKjIU) by [TheAtticusProject](https://github.com/TheAtticusProject/cuadTheAtticusProject). The model was fine-tuned using contract documents, manually annotated by Law students. Detailed description of CUAD dataset and annotation process can be found [here](https://huggingface.co/datasets/cuad).

For further fine-tuning, new data can be annotated using [SQuAD format](https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v2.0.json). Code for training can be found in [the original repository](https://github.com/TheAtticusProject/cuadTheAtticusProject).

[eBrevia](https://ebrevia.com/) can be used for data annotation as stated [here](https://huggingface.co/datasets/cuad), under `Annotations` section.

Code for prediction was taken from [this repository](https://github.com/marshmellow77/cuad-demo/blob/main/scripts/predict.py).
