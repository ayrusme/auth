from database.validator import BLOCK_VALIDATOR


x = {
	"name": "Golden Blossom",
    "address_line1": "SG707",
    "city": "Bengaluru",
    "country": "India",
    "pin_code": 560067,
    "apartment_id": "dac8262d-ddaa-470d-a93e-1b36bc101d37"
}

BLOCK_VALIDATOR.validate(x)
