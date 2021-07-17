import logging as log

import click
from ocr.ocr import scanPdf2text
from utils import (getCheckedContract, isContractChecked, isPdf,
                   isSearchablePdf, pdfText, storeContract)


@click.group()
def cli():
    pass

@click.command()
@click.option('--path', help='Path to a contract file')
def check_contract(path):
    """Checks contract in given path and stores result in .data/file_name.json"""
    if not isPdf(path):
        log.error("Not pdf file")
        return
    contract = None
    if isContractChecked(path):
        contract = getCheckedContract(path = path)
        return contract
    if isSearchablePdf(path):
        contract = pdfText(path)
    else:
        contract = scanPdf2text(path)
    contract = getCheckedContract(contract = contract)
    storeContract(path, contract)


cli.add_command(check_contract)

if __name__ == '__main__':
    cli()