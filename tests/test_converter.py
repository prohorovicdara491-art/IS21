import pytest
from src.modul_a import convert_number, batch_convert

def test_convert_number_bin_to_dec():
    assert convert_number("1010", 2, 10) == "10"
    assert convert_number("1111", 2, 10) == "15"
    assert convert_number("0", 2, 10) == "0"

def test_convert_number_hex_to_dec():
    assert convert_number("FF", 16, 10) == "255"
    assert convert_number("A", 16, 10) == "10"

def test_convert_number_dec_to_hex():
    assert convert_number("255", 10, 16) == "FF"
    assert convert_number("16", 10, 16) == "10"

def test_convert_number_dec_to_bin():
    assert convert_number("10", 10, 2) == "1010"

def test_batch_convert():
    numbers = ["1010", "FF", "777"]
    results = batch_convert(numbers, 16, 10)
    assert len(results) == 3

def test_convert_number_invalid():
    result = convert_number("GHI", 16, 10)
    assert "Ошибка" in result