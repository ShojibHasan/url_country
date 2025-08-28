# URL Country

A Python package to determine the country of a URL/domain using multiple methods including TLD analysis, WHOIS lookup, DNS resolution, and GeoIP geolocation.

## Features

- **Multiple Detection Methods**: Combines TLD analysis, WHOIS lookup, DNS resolution, and GeoIP geolocation
- **Confidence Scoring**: Provides confidence levels (high, medium, none) based on the reliability of detected signals
- **Voting System**: Uses a weighted voting system to determine the most likely country
- **Easy to Use**: Simple API with just one main function
- **Comprehensive Coverage**: Handles various domain formats and edge cases

## Installation

```bash
pip install url_country
```

## Quick Start

```python
from url_country import get_region

# Get country information for a domain
result = get_region("x.com")
print(result)
# Output: {'final_alpha2': 'US', 'confidence': 'medium', 'votes': {'US': 2}}

# Get country information for a full URL
result = get_region("https://www.google.co.uk")
print(result)
# Output: {'final_alpha2': 'GB', 'confidence': 'high', 'votes': {'GB': 4}}
```

## API Reference

### `get_region(domain: str) -> Dict[str, Any]`

Determines the country of a domain or URL.

**Parameters:**

- `domain` (str): The domain or URL to analyze

**Returns:**

- `Dict[str, Any]`: A dictionary containing:
  - `final_alpha2` (str): The ISO 3166-1 alpha-2 country code
  - `confidence` (str): Confidence level ('high', 'medium', or 'none')
  - `votes` (Dict[str, int]): Voting results for each detected country

**Example:**

```python
from url_country import get_region

result = get_region("example.com")
print(f"Country: {result['final_alpha2']}")
print(f"Confidence: {result['confidence']}")
print(f"Votes: {result['votes']}")
```

## How It Works

The package uses a multi-layered approach to determine the country of a domain:

1. **TLD Analysis**: Extracts country information from the top-level domain (e.g., `.uk` → GB, `.de` → DE)
2. **WHOIS Lookup**: Queries WHOIS databases for domain registration information
3. **DNS Resolution**: Resolves domain to IP addresses
4. **GeoIP Lookup**: Uses MaxMind's GeoLite2 database to determine the geographic location of IP addresses
5. **Voting System**: Combines all signals with weighted voting to determine the final result

## Dependencies

- `tldextract`: TLD extraction and analysis
- `dnspython`: DNS resolution
- `python-whois`: WHOIS lookup
- `geoip2`: GeoIP geolocation
- `pycountry`: Country code utilities

## Requirements

- Python 3.7 or higher
- Internet connection for WHOIS and DNS lookups
- GeoLite2-Country.mmdb database file (included in the package)

## Development

To set up the development environment:

```bash
git clone https://github.com/ShojibHasan/url_country.git
cd url_country
pip install -e ".[dev]"
```

## Testing

```bash
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

**Mahfujul Hasan** - [shojibhasan15@gmail.com](mailto:shojibhasan15@gmail.com)

## Support

If you encounter any issues or have questions, please:

1. Check the [documentation](https://github.com/ShojibHasan/url_country#readme)
2. Search [existing issues](https://github.com/ShojibHasan/url_country/issues)
3. Create a [new issue](https://github.com/ShojibHasan/url_country/issues/new) if your problem isn't already reported
